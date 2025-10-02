#%%
import pandas as pd
import numpy as np
pd.options.display.show_dimensions = False
pd.set_option('display.width', 1000)
pd.options.mode.copy_on_write = True
pd.set_option('display.max_rows', 15)
pd.set_option('display.max_columns', None)

import vertexai
from vertexai.generative_models import GenerativeModel
from NeuronsMemoryTestPipeline import constants
import NeuronsMemoryTestPipeline.MRT_free_recall_metric as MRT_free_recall_metric
import NeuronsMemoryTestPipeline.MRT_recognition_metric as MRT_recognition_metric

PROJECT = constants.PROJECT
LOCATION = constants.LOCATION

vertexai.init(project=PROJECT, location=LOCATION)
model = GenerativeModel(constants.MODEL_TYPE)

# ************** DOWNLOAD FILES FROM THE SCRIPT ************
############################################################    

#%%
def create_combined_score(freerecall, recognition, type=[]):
    wide_df = recognition.pivot_table(index=['group_id', 'mrt_stimulus'] + type, columns='mrt_association', values=['mrt_score_recognition'], aggfunc='first', observed=False)
    wide_df.columns = [f'{col[1]}' for col in wide_df.columns]
    wide_df.reset_index(drop=False, inplace=True)
    df_updated = freerecall.merge(wide_df, on = ['group_id', 'mrt_stimulus'] + type, how = 'outer')
    df_updated['Brand&Freerecall AVG'] = ((df_updated['Freerecall'] + df_updated['Which Brand?']) / 2)
    df_updated['Brand&Freerecall AVG'] = df_updated['Brand&Freerecall AVG'].clip(0, 100)
    #df_updated['Overall_Score'] = (alpha * (df_updated['Brand&Freerecall AVG']) + beta * df_updated['Remember Ad?']) / 2
    #df_updated['Overall_Score'] = df_updated['Overall_Score'].clip(0, 100)
    col1 = ['group_id', 'project_identifier', 'total_participants','mrt_stimulus']
    col2 = ['position_mean', 'brand_count', 'recall_%', 'Freerecall', 'Which Brand?', 'Brand&Freerecall AVG']
    df_updated = df_updated[col1 + type + col2].copy()
    return df_updated

def update_data(df, extra_df=None, type = None):
    return_df = pd.DataFrame()
    project = df['project_identifier'].dropna().unique()[0]
    for gr in df['group_id'].unique():
        check_df = df[df['group_id'] == gr].copy()
        uncheck_df = check_df[~check_df['project_identifier'].isna()]
        check_df = check_df[check_df['project_identifier'].isna()]
        check_df.project_identifier = project
        check_df['recall_%']=0
        check_df['position_mean']='na'
        check_df['brand_count']=0
        check_df['Freerecall']=0
        
        if type is not None and type in df.columns:
            check_df = check_df.merge(extra_df, how='left', on=['group_id', type])
            check_df['total_participants'] = check_df['count']
            check_df.drop('count', axis=1, inplace=True)
        else:
            check_df.drop('total_participants', axis=1, inplace=True)
            check_df = check_df.merge(extra_df, how='left', on='group_id')

        return_df = pd.concat([return_df, uncheck_df, check_df], axis=0, ignore_index=True)
        return_df.total_participants = return_df.total_participants.astype(int)
    return return_df

#%%
#PATHS and FILES FOR WINDOWS
#project_path = r'G:\Shared drives\HQ - Projects\Active Internal Projects\82025-0005_Brand_Recall_Carousel\\'
#path_output = project_path + r'Analysis_(DS)\Scores\Videos\\'
#cleaned_df_file = r"QA\Videos\Day2\G3\QA_Outputs\cleaned_df.csv"
#alias_map_file = "Target_Stimuli\Stimuli_Map\Videos\82025-0005_Brand_Recall_Carousel_Videos_map_G3.csv"

# for testing purposes
irina_path = r'/Users/irinakw/Library/CloudStorage/GoogleDrive-i.white@neuronsinc.com/Shared drives/HQ - Projects /'
project_path = irina_path + r'Active Internal Projects/82025-0005_Brand_Recall_Carousel/'
path_output = project_path + r'Analysis_(DS)/Scores/'
cleaned_df_file = f'QA/Videos/Day2/G3/QA_Outputs/cleaned_df.csv'
alias_map_file = "Target_Stimuli/Stimuli_Map/Videos/82025-0005_Brand_Recall_Carousel_Videos_map_G3.csv"
#demographics_df_file = r'2_Fieldwork/QA/Demographics_GoodIDs.xlsx'


#DOWNLOAD DEMOGRAPHICS, DATASET AND QA
df = pd.read_csv(project_path+cleaned_df_file, low_memory = True)
alias_data = pd.read_csv(project_path + alias_map_file, low_memory = True)

# Excluding bad IDs if necessary
# path_meta_RealEye = r"G:\Shared drives\HQ - Projects\Active External Projects\Standard Explore Projects\90696-0004_Teads_DE_TVAdTest_SamsungFold_AdEffectiveness\QA\Day7\TestGroup\ET\ET_QA_report.xlsx"
# df_meta_RE = pd.read_excel(path_meta_RealEye, sheet_name='Good IDs', header=0)
# df_meta_RE.rename(columns={"participant_id":'participant_id'}, inplace=True) # rename id column if necessary
# df_meta_RE['participant_id'] = df_meta_RE['participant_id'].astype(str)
# df = df[df['participant_id'].isin(df_meta_RE['participant_id'])]

# %% 
#CLEANED DATA
df.group_id = df.group_id.astype(int)
df.group_id = df.group_id.astype(str)
print("Group IDs in this study are: ", df.group_id.unique())
print('==='*30)
print('\nNumber of participants per group in the analyzed study:')
print(df.groupby('group_id')['participant_id'].nunique())
print('DATA is UPLOADED and READY for ANALYSIS!')
print("CHANGE THE GROUP_ID?")

# %% 
####################################################################################
# ************** POST SURVEY - FAMILIARITY, RELEVANCE, PREFERENCE **************
####################################################################################

try: 
    df_survey = df[df['trial_name'] == 'Survey_Question_Association_Data'].copy()

    if not df_survey.empty:
        df_survey['survey_question_association_text_english'] = df_survey['survey_question_association_text_english'].replace({
            'brand-familiarity': 'Brand Familiarity',
            'brand-preference': 'Brand Preference',
            'brand-relevance': 'Brand Relevance'
        })

        survey_pivot = df_survey.pivot_table(index = ['group_id', 'survey_question_association_text_english'],
                                            columns = 'trial_stimulus',
                                            values = 'survey_question_association_response_numeric',
                                            aggfunc = 'mean',
                                            fill_value = 0, observed = False)
        survey_pivot.index.name = None
        survey_pivot = survey_pivot.round(2)

        survey_exists = True
        print('\n ***** SURVEY DONE! *****')
    else:
        survey_exists = False
        print('\n ***** NO SURVEY DATA FOUND! *****')

except Exception as e: 
    survey_exists = False
    print(f'\n ***** AN ERROR OCCURRED IN SURVEY PROCESSING: {e} *****')
    pass

# if CHANGE_GROUP_ID not in df.group_id.unique():
#     print(f"Changed group_id to {CHANGE_GROUP_ID}")
#     df.group_id = CHANGE_GROUP_ID
#     df["group_id"] = pd.to_numeric(df["group_id"], errors="coerce").astype("Int64")
#     df["group_id"] = df["group_id"].astype(str)

#%%
# ************** MANUAL CORRECTION **************
#################################################
manual_correction = {
}
apply_manual_correction = False

# ************** PREPARE DATA **************
############################################
alias_data = MRT_free_recall_metric.alias_group_define(alias_data)
alias_data = alias_data.loc[alias_data['role']!='Distractor'].copy()
alias_data = alias_data[['group_id', 'brand_name', 'alias']].reset_index(drop=True).copy()
alias_data.columns = ['group_id', 'mrt_stimulus', 'mrt_stimulus_ad']
alias_data = alias_data[alias_data['group_id'].isin(df['group_id'].unique())].reset_index(drop=True).copy()
print('==='*30)
print('\nList of stimulus used in the study per analyzed Group:')
print(alias_data)

#%%
df = df[constants.MRT_COLUMNS]
df["Age_Group"] = pd.cut(x=df['Age'], bins=3, labels=["Younger","Mid","Older"])
df = df.loc[df['reason_to_end_the_behavioral_task_code']==13]
df.group_id = df.group_id.astype('str')
df.drop('reason_to_end_the_behavioral_task_code', axis = 1, inplace=True)
try: 
    df = df.loc[df['participant_quality'] == 1.0]
except: 
    pass
df['total_participants'] = df.groupby('group_id')['participant_id'].transform('nunique')
df = df.loc[df.module_name == 'MRT']

if apply_manual_correction:
    print('==='*30)
    print('\n***** Manual corrections to Free Recall applied *****\n')
    df['given_response_label_presented'] = df['given_response_label_presented'].replace(manual_correction)
else:
    print('==='*30)
    print('\nNo Manual Correction applied to the Free Recall entries.\n')

#%%
############################################
# ************** DEMOGRAPHICS **************
############################################
stat_age, stat_gender, stat_age_group = MRT_recognition_metric.produce_demographics(df)

stat_g = stat_gender.reset_index(drop=False)[['group_id','Gender','count']]
stat_g.columns = ['group_id','split','count']

stat_a = stat_age_group.reset_index(drop=False)[['group_id','Age_Group','count']]
stat_a.columns = ['group_id','split','count']

#%%
###########################################################
# ************** CALCULATE FREE RECALL SCORE **************
###########################################################

df_free_recall, corrected_pairs, not_match = MRT_free_recall_metric.process_recall(df,'Free Recall', model, alias_df = alias_data)
responses1=not_match[not_match['given_response_label_presented'].str.strip().str.split(' ').str.len() ==1]['given_response_label_presented'].reset_index(drop=True)
responses2=not_match[not_match['given_response_label_presented'].str.strip().str.split(' ').str.len() ==2]['given_response_label_presented'].reset_index(drop=True)
responses3plus=not_match[not_match['given_response_label_presented'].str.strip().str.split(' ').str.len() >2]['given_response_label_presented'].reset_index(drop=True)
corrected_pairs = corrected_pairs.drop_duplicates().dropna().sort_values(['method','given_response_label_presented']).reset_index(drop=True)
#%%
corrected_pairs
#%%
not_match
#%%
#Filter the responses we need to calculate
df_free_recall= df_free_recall[df_free_recall.corrected.isin(alias_data['mrt_stimulus'].unique())].reset_index(drop=True)
free_recall_scores = MRT_free_recall_metric.compute_scores(df_free_recall)
print('==='*30)
print('Free Recall scores are calculated!')
free_recall_scores


#%%
df_a = df_free_recall.merge(stat_a[['group_id', 'split', 'count']], how='left', left_on=['group_id','Age_Group'], right_on=['group_id','split'])
df_a['total_participants'] = df_a['count']
df_g = df_free_recall.merge(stat_g[['group_id', 'split', 'count']], how='left', left_on=['group_id', 'Gender'], right_on=['group_id','split'])
df_g['total_participants'] = df_g['count']
#%%
# DEMOGRAPHICS RESULTS FOR FREE RECALL
split_column_group = ['group_id', 'project_identifier', 'task_name', 'total_participants', 'corrected']
free_recall_scores_age = MRT_free_recall_metric.compute_scores(df_a, group = split_column_group + ['Age_Group'])
free_recall_scores_gender = MRT_free_recall_metric.compute_scores(df_g, group = split_column_group + ['Gender'])

# %%
############################################################
# **************  CALCULATE RECOGNITION RATES **************
############################################################

df_ad_recognition = df.loc[(df['task_name'] =='Ad Recognition') & (df['trial_name'] =='Presentation')].reset_index(drop=True)
df_ad_recognition['given_response_accuracy'] = df_ad_recognition['given_response_accuracy'].map({'Wrong': 'No', 'Correct': 'Yes'})

#%%
df_brand_recognition = df.loc[(df['task_name'] =='Ad Recognition') & (df['trial_name'] =='Recognition')].reset_index(drop=True)
df_brand_recognition['given_response_accuracy'] = df_brand_recognition['given_response_accuracy'].map({'Wrong': 'No', 'Correct': 'Yes'})

df_ad_recognition['mrt_association'] = 'Remember Ad?'
df_brand_recognition['mrt_association'] = 'Which Brand?'

mrt_column_rename = { 
    'expected_response' : 'mrt_stimulus',
    'given_response_accuracy': 'mrt_response'
    }
df_recognition = pd.concat([df_ad_recognition, df_brand_recognition], axis=0, ignore_index=True)
df_recognition.rename(columns = mrt_column_rename, inplace = True)
df_recognition_all = MRT_recognition_metric.recognition_scores(df_recognition).reset_index(drop=False)
df_recognition_all.rename(columns={'mrt_score': 'mrt_score_recognition'}, inplace=True)
df_recognition_gender = MRT_recognition_metric.split_score(df_recognition, ['Male', 'Female'], 'Gender').reset_index(drop=False)
df_recognition_gender.rename(columns={'mrt_score': 'mrt_score_recognition'}, inplace=True)
df_recognition_age = MRT_recognition_metric.split_score(df_recognition, ["Younger","Mid","Older"], 'Age_Group').reset_index(drop=False)
df_recognition_age.rename(columns={'mrt_score': 'mrt_score_recognition'}, inplace=True)



#%%
df_brand_recognition_dis = df_brand_recognition.drop_duplicates(subset=['expected_response', 'participant_id'])
df_brand_recognition_dis = df_brand_recognition.groupby(['group_id', 'expected_response', 'given_response_label_presented']).size().reset_index(name='count')
df_brand_recognition_dis['percentage'] = df_brand_recognition_dis.groupby(['group_id', 'expected_response'])['count'].transform(lambda x: (x / x.sum()) * 100)

#%% 
############################################################
# **************  MERGING ALL SCORES INTO ONE **************
############################################################
col = ['group_id', 'mrt_association', 'mrt_stimulus', 'mrt_score_recognition']

def filter_result(df, alias_data, col):
    merged_df = df.merge(alias_data, left_on=['group_id', 'mrt_stimulus'], right_on=['group_id', 'mrt_stimulus_ad'], how='left', suffixes=('', '_alias'))
    merged_df['mrt_stimulus'] = merged_df['mrt_stimulus_alias'].combine_first(merged_df['mrt_stimulus'])
    df_filtered = merged_df[col].copy()
    return df_filtered

df_recognition_all = filter_result(df_recognition_all, alias_data, col)
df_recognition_all = df_recognition_all.sort_values('group_id').reset_index(drop=True)
df_recognition_age = filter_result(df_recognition_age, alias_data, col = col+['Age_Group'])
df_recognition_gender = filter_result(df_recognition_gender, alias_data, col = col+['Gender'])

final_all = create_combined_score(free_recall_scores, df_recognition_all)
final_all_gender = create_combined_score(free_recall_scores_gender, df_recognition_gender, type = ['Gender'])
final_all_age = create_combined_score(free_recall_scores_age, df_recognition_age, type = ['Age_Group'])

#check for empty rows
age= stat_age_group[['group_id','Age_Group','count']].copy()
gender= stat_gender.reset_index(drop=False)[['group_id','Gender','count']].copy()
total_number = stat_gender.reset_index(drop=False)[['group_id','total_participants']].drop_duplicates().reset_index(drop=True).copy()
final_all = update_data(final_all, total_number)
final_all_age = update_data(final_all_age, age, 'Age_Group')
final_all_gender = update_data(final_all_gender, gender, 'Gender')


#%%
###################################################
# ************** AVERAGE POSITIONING **************
###################################################
print('==='*30)
df_entries = df[(df.task_name == 'Free Recall' )& (df.given_response_label_presented.notna())].copy()
df_free_recall[df_free_recall.participant_id == '3sM8K44fLRcUoPrenHHhMH'].reset_index(drop=True)
ratio_df = pd.DataFrame(index=df_free_recall['participant_id'].value_counts().index)
ratio_df['Targeted Entries'] = df_free_recall['participant_id'].value_counts()
ratio_df['All Entries'] = df_entries['participant_id'].value_counts()
ratio_df['Ratio'] = ratio_df['Targeted Entries'] / ratio_df['All Entries']
ratio_df = ratio_df.rename(columns={'index': 'participant_id'}).reset_index()
ratio_df = ratio_df.merge(df[['participant_id', 'group_id']].drop_duplicates(), on='participant_id', how='left')
ratio_df = ratio_df.groupby('group_id').agg({'Ratio': 'mean', 'Targeted Entries': 'mean', 'All Entries': 'mean'})

#%%
##########################################
# **************  REPORTING **************
##########################################
#path_output = ''  # For testing purposes

df_fr = pd.DataFrame({'Data':["Free Recall correction using fuzzy and AI"]})
with pd.ExcelWriter(path_output + f'MRT_Scores_Videos_G3.xlsx') as writer:
    stat_age.to_excel(writer,sheet_name = 'Demographics', index = True, startcol = 0)
    stat_age_group.to_excel(writer,sheet_name = 'Demographics', index = False, startcol = 6)
    stat_gender.to_excel(writer,sheet_name = 'Demographics', index = True, startcol = 14)
    final_all.set_index(['group_id', 'mrt_stimulus']).to_excel(writer, sheet_name = "MRT Scores Final", startrow = 0, startcol = 0, index = True) 
    ratio_df.to_excel(writer,sheet_name = 'MRT Scores Final', index = True, startrow = 0, startcol = 15)
    final_all_age.set_index(['group_id', 'mrt_stimulus','Age_Group']).to_excel(writer, sheet_name = "MRT Scores Final Age Split", startrow = 0, startcol = 0, index = True)
    final_all_gender.set_index(['group_id', 'mrt_stimulus','Gender']).to_excel(writer, sheet_name = "MRT Scores Final Gender Split", startrow = 0, startcol = 0, index = True)
    if survey_exists:
        survey_pivot.to_excel(writer, sheet_name = "Post-Survey", index = True)

with pd.ExcelWriter(path_output + f'MRT_ExtraSheets_Videos_G3.xlsx') as writer:
    alias_data.to_excel(writer,sheet_name = 'Stimulus', index=False)
    corrected_pairs.set_index(['group_id', 'method']).to_excel(writer, sheet_name = "Free Text Correction", startrow = 0, startcol = 0, index = True)  
    responses1.to_excel(writer, sheet_name = "FreeRecall Responses", index = False, startcol = 0)
    responses2.to_excel(writer, sheet_name = "FreeRecall Responses", index = False, startcol = 3) 
    responses3plus.to_excel(writer, sheet_name = "FreeRecall Responses", index = False, startcol = 6)
    df_brand_recognition_dis.to_excel(writer, sheet_name = "Brand Recognition Responses", index = False, startcol = 0)


print('***** MRT REPORT IS DONE! *****')
# %%
