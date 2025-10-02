# ==== Fast, grounded-first brand cleaner (final) ====
import re, unicodedata
from collections import defaultdict
import pandas as pd
from rapidfuzz import process, fuzz
from rapidfuzz.distance import Levenshtein
from tqdm.auto import tqdm
from NeuronsMemoryTestPipeline.constants import SPELLCHECK_PROMPT_TEMPLATE

# ------------------- helpers -------------------
GENERIC_NOT_FOUND = {
    "idk","i don't know","dont know","can't remember","cant remember",
    "no idea","nothing","na","n/a","none","other","others"
}

def normalize(s: str) -> str:
    if not isinstance(s, str): return ""
    s = unicodedata.normalize("NFKC", s)
    s = s.strip()
    s = re.sub(r"\s+", " ", s)     
    s = s.lower()
    s = re.sub(r"[^\w\s&+]", "", s)  
    return s

def nospace(s: str) -> str: return re.sub(r"\s+", "", s)
def and_equiv(s: str) -> str: return re.sub(r"\band\b", "&", s)
def compress_runs(s: str) -> str: return re.sub(r"(.)\1+", r"\1", s)
def tokens(s: str):
    return [t for t in re.split(r"\s+", s.strip()) if t]

def looks_like_acronym_input(s: str) -> bool:
    s = s.strip()
    if len(s) < 2 or len(s) > 6:
        return False
    no_space = " " not in s
    has_dots = "." in s
    mostly_upper = sum(c.isupper() for c in s) >= max(1, int(0.6*len([c for c in s if c.isalpha()])))
    return (no_space and (has_dots or mostly_upper)) or has_dots

def abbr_of(phrase: str) -> str:
    return "".join(w[0].upper() for w in re.split(r"\s+", (phrase or "").strip()) if w)

def bigrams(s: str):
    return {s[i:i+2] for i in range(len(s)-1)} if len(s) > 1 else set()

# ------------------- indices -------------------
def build_indices(brands_presented):
    brands_presented = list(dict.fromkeys(brands_presented))  
    norm_to_orig = {normalize(b): b for b in brands_presented}
    norm_names = list(norm_to_orig.keys())

    abbr_map = defaultdict(list)
    for b in brands_presented:
        abbr_map[abbr_of(b)].append(b)

    # exact-equivalence maps
    ns_map  = {nospace(k): v for k, v in norm_to_orig.items()}
    and_map = {nospace(and_equiv(k)): v for k, v in norm_to_orig.items()}
    cr_map  = {compress_runs(k): v for k, v in norm_to_orig.items()}

    cr_ns_map = {nospace(compress_runs(k)): v for k, v in norm_to_orig.items()}
    ns_cr_map = {compress_runs(nospace(k)): v for k, v in norm_to_orig.items()}
    
    return (brands_presented, norm_to_orig, norm_names, abbr_map,
            ns_map, and_map, cr_map, cr_ns_map, ns_cr_map)

# ------------------- grounded match -------------------
def grounded_match(user_text: str,
                   norm_to_orig, norm_names, abbr_map,
                   ns_map, and_map, cr_map, cr_ns_map, ns_cr_map):
    raw = user_text or ""
    raw_norm = normalize(raw)

    # obvious not-found
    if raw_norm in GENERIC_NOT_FOUND or raw_norm == "":
        return "", "not_match"

    # exact normalized
    if raw_norm in norm_to_orig:
        return norm_to_orig[raw_norm], "exact"
    #token match
    toks = tokens(raw_norm)
    if toks:
        tok_set = set(toks)
        for bn, orig in norm_to_orig.items():
            if bn in tok_set:
                return orig, "brand_token"
            
    # exact-equivalence: nospace / and<->& / compressed runs
    k = nospace(raw_norm)
    if k in ns_map: return ns_map[k], "exact_nospace"

    k2 = nospace(and_equiv(raw_norm))
    if k2 in and_map: return and_map[k2], "exact_and_equiv"

    k3 = compress_runs(raw_norm)
    if k3 in cr_map: return cr_map[k3], "exact_compress"
            
    # NEW: combined exact maps (handles "go dady" -> "godaddy" via compress + nospace)
    k4 = nospace(compress_runs(raw_norm))
    if k4 in cr_ns_map: return cr_ns_map[k4], "exact_compress_nospace"
    k5 = compress_runs(nospace(raw_norm))
    if k5 in ns_cr_map: return ns_cr_map[k5], "exact_nospace_compress"

    # abbreviation (TIGHTENED without removing prior logic)
    ab = abbr_of(raw)
    # NEW: require the input to look like an acronym; ignore 1-letter abbreviations
    if looks_like_acronym_input(raw) and len(ab) >= 2:
        if ab in abbr_map and len(abbr_map[ab]) == 1:
            return abbr_map[ab][0], "abbreviation"
        elif ab in abbr_map and len(abbr_map[ab]) > 1:
            # NEW: avoid risky tie-breaks — defer to AI instead of forcing a brand
            return "", "maybe"

    # fuzzy (strict, short-string aware)
    choice, score, _ = process.extractOne(raw_norm, norm_names, scorer=fuzz.ratio)
    if not choice:
        return "", "maybe"

    cand_norm = choice
    cand_orig = norm_to_orig[cand_norm]
    Lx, Ly = len(raw_norm), len(cand_norm)
    len_delta = abs(Lx - Ly)
    edit_dist = Levenshtein.distance(raw_norm, cand_norm)
    bx = bigrams(raw_norm); by = bigrams(cand_norm)
    bigram_overlap = len(bx & by)
    first_letter_ok = (Lx == 0 or cand_norm[:1] == raw_norm[:1])

    if Lx <= 4:
        pass_threshold = (score >= 97) and (edit_dist <= 1) and first_letter_ok and (len_delta <= 1) and (bigram_overlap >= 1)
    elif Lx <= 6:
        pass_threshold = (score >= 94) and (edit_dist <= 2) and first_letter_ok and (len_delta <= 2) and (bigram_overlap >= 1)
    else:
        pass_threshold = (score >= 90) and (edit_dist <= 3) and (len_delta <= 3)

    if pass_threshold:
        return cand_orig, "fuzzy"
    return "", "maybe"

# ------------------- junk filters (numbers/gibberish) -------------------
VOWELS = set("aeiou")

def is_numeric_like(s: str) -> bool:
    s = (s or "").strip()
    if not s: return True
    d = sum(c.isdigit() for c in s)
    return s.isdigit() or (len(s) >= 4 and d / len(s) >= 0.5)

def looks_like_gibberish(s: str) -> bool:
    t = re.sub(r"[^a-z]", "", normalize(s))  # letters only
    if len(t) == 0: return True
    if len(t) >= 6 and not (set(t) & VOWELS): return True
    if len(t) >= 7 and (sum(ch in VOWELS for ch in t) / len(t) <= 0.1): return True
    if re.search(r"(.)\1{3,}", t): return True
    raw = normalize(s)
    non_alnum = sum(not c.isalnum() and not c.isspace() for c in raw)
    return len(raw) >= 6 and non_alnum / len(raw) > 0.3

def is_candidate_for_ai(s: str) -> bool:
    s = (s or "").strip()
    return bool(s) and s.lower() not in GENERIC_NOT_FOUND and not is_numeric_like(s) and not looks_like_gibberish(s)

# ------------------- ADDED: AI distance prefilter -------------------
# configurable gates (kept separate; nothing removed)
AI_MIN_RATIO     = 75      # min fuzz.ratio to nearest brand
AI_MAX_EDIT_FRAC = 0.25    # max Levenshtein distance as fraction of input length
AI_MIN_BIGRAMS   = 1       # require >=1 bigram overlap for len>=4

def _bigrams(s: str):
    return {s[i:i+2] for i in range(len(s)-1)} if len(s) > 1 else set()

def close_enough_to_brand(s: str, norm_names) -> bool:
    """Additional distance-based gate to avoid very-far pairs (e.g., 'Volvo' vs 'Citroen')."""
    sx = normalize(s)
    if not sx: return False
    hit = process.extractOne(sx, norm_names, scorer=fuzz.ratio)
    if not hit: return False
    cand_norm, ratio, _ = hit
    edit = Levenshtein.distance(sx, cand_norm)
    L = len(sx)
    max_edit = max(2, int(round(AI_MAX_EDIT_FRAC * L)))
    bg_ok = (L < 4) or (len(_bigrams(sx) & _bigrams(cand_norm)) >= AI_MIN_BIGRAMS)
    first_letter_ok = (L == 0) or (cand_norm[:1] == sx[:1])
    return (ratio >= AI_MIN_RATIO) and (edit <= max_edit) and bg_ok and first_letter_ok

# ------------------- AI fallback -------------------
def ai_spellcheck_batch(candidates_unique, brands_presented, norm_names, model, prompt_template, max_words=4):
    clean_candidates = [c for c in candidates_unique if is_candidate_for_ai(c)]
    near_candidates = [c for c in clean_candidates if close_enough_to_brand(c, norm_names)]
    print(f"[AI] candidates (post-filter): {len(near_candidates)} / {len(candidates_unique)} "
          f"(junk-kept: {len(clean_candidates)})")
    if (model is None) or (len(near_candidates) == 0):
        print(f"AI skipped. Model={model is not None}, candidates kept={len(near_candidates)}")
        return pd.DataFrame(columns=["given_response_label_presented","corrected","method"])

    rows = []
    for item in tqdm(near_candidates, desc="AI spellcheck", leave=False):
        prompt = prompt_template.format(
            potential_responses=brands_presented,
            brand_to_check=item
        )
        try:
            res = model.generate_content(prompt)
            txt = (res.candidates[0].text or "").strip()
        except Exception:
            txt = "Not Found"

        if len(txt.split()) > max_words:
            txt = "Not Found"

        if txt != "Not Found":
            rows.append({
                "given_response_label_presented": item,
                "corrected": txt,
                "method": "ai"
            })
    return pd.DataFrame(rows)

# ------------------- main CALL -------------------
def clean_free_recall_fast(df: pd.DataFrame, brands_presented, model=None, use_ai=True):
    (brands_presented, norm_to_orig, norm_names, abbr_map,
        ns_map, and_map, cr_map, cr_ns_map, ns_cr_map) = build_indices(brands_presented)

    out = df.copy()
    if "given_response_label_presented" not in out.columns:
        raise ValueError("Input df must have 'given_response_label_presented'")

    out["given_response_label_presented"] = out["given_response_label_presented"].astype(str).str.strip()
    out.loc[out["given_response_label_presented"].eq(""), "given_response_label_presented"] = pd.NA

    out["method"] = ""
    out["corrected"] = ""

    results = out["given_response_label_presented"].apply(
        lambda x: grounded_match(x, norm_to_orig, norm_names, abbr_map, ns_map, and_map, cr_map, cr_ns_map, ns_cr_map)
        if pd.notna(x) else ("","not_match")
    )
    out[["corrected","method"]] = pd.DataFrame(results.tolist(), index=out.index)

    mask_others = out["given_response_label_presented"].astype(str).str.lower().isin({"other","others"})
    out.loc[mask_others, "method"] = "not_match"

    if use_ai:
        if model is None:
            raise ValueError("use_ai=True but model is None")
        maybes = (out.loc[out["method"] == "maybe", "given_response_label_presented"]
                    .dropna().map(str).map(str.strip))
        maybes = [m for m in maybes if m]
        ai_df = ai_spellcheck_batch(maybes, brands_presented, norm_names, model, SPELLCHECK_PROMPT_TEMPLATE)

        if not ai_df.empty:
            out = out.merge(ai_df, on="given_response_label_presented", how="left", suffixes=("","_ai"))
            fill = out["corrected_ai"].notna()
            out.loc[fill, "corrected"] = out.loc[fill, "corrected_ai"]
            out.loc[fill, "method"]    = "ai"
            out = out.drop(columns=["corrected_ai","method_ai"], errors="ignore")

        out.loc[out["method"] == "maybe", "method"] = "not_match"

    return out


def calculate_corrected_brands_fast(df: pd.DataFrame, brands_presented):
    valid = set(brands_presented)
    count_df = df[df["corrected"].isin(valid)].drop_duplicates(["participant_id","corrected","method"])
    return (
        count_df.groupby(["group_id","method"])["corrected"]
        .value_counts()
        .rename("count")
        .reset_index()
    )
