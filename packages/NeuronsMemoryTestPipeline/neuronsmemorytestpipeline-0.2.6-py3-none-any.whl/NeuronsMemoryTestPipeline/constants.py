# MRT MODULE
MRT_COLUMNS = ['reason_to_end_the_behavioral_task_code', #'participant_quality', 
           'participant_id', 'group_id', 'provider_id', 'module_name',
           'project_identifier', 'reaction_time', 'task_name', 'trial_name','given_response_label_presented', 'procedure_name',
           'trial_stimulus_category','expected_response', 'given_response_accuracy', 'given_response_label_english', 'Gender', 'Age'
          ]
PROJECT = 'neurons-ml'
LOCATION = 'us-central1'

MODEL_TYPE = "gemini-2.5-flash-lite"
PARAMETERS = {
    "candidate_count": 1,
    "max_output_tokens": 32,
    "temperature": 0.5,
}

# FRT MODULE

FRT_COLUMNS_RENAME = {
    'procedure_stimulus' : 'frt_stimulus',
    'trial_association_english' : 'frt_association',
    'given_response_label_english': 'frt_response'
}

SPELLCHECK_PROMPT_TEMPLATE = """
You are a **Brand Name Spell Checker**.

## Task
Given:
- A list of valid brand names:  
  **potential_responses = {potential_responses}**

- A single input to validate:  
  **brand_to_check = {brand_to_check}**

Determine if `brand_to_check` approximately matches any entry in `potential_responses` using:
- Spelling similarity ≥ 98%
- Edit distance ≤ 2
- Semantic similarity ≥ 90%

## Output Rules
- If a close match exists, return only the **closest valid brand name** from `potential_responses`.
- If no suitable match exists, return exactly: **"Not Found"**

## Examples
- "Addidas" → "Adidas"
- "Nke" → "Nike"
- "uma" → "Puma"
- "Bang" → "Bang & Olufsen"
- "Can't remember" → "Not Found"
- "I don't know" → "Not Found"
- "Life" → "Not Found"

## Response Template
example 1: Prada
example 2: Not Found
"""
