from fuzzywuzzy import fuzz
import pandas as pd
import numpy as np
similar_tasks = []

biostat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Biostatisticians/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
stat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Statisticians/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
bis_analyst =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Business Intelligence Analysts/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
clin_data_managers =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Clinical Data Managers/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
remote_sensing_scientist =  pd.read_csv("C:/Users/buckl\SkillsTrust\O-NET-role-scraper\occupations\Remote Sensing Scientists and Technologists/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
doc_man_spec =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Document Management Specialists/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
fin_quan_analyst =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Financial Quantitative Analysts/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
man_analyst =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Management Analysts/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
mathematicians =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Mathematicians/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')
ops_research_analysts =  pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Operations Research Analysts/tasks.csv",header=0, encoding='utf-8',encoding_errors='replace')


def compare_occupations(occ_df1,occ_df2):
    token_set_ratios = []
    token_sort_ratios = []
    ratios = []
    partial_ratios = []
    partial_token_set_ratios = []
    partial_token_sort_ratios = []
    for occ1_task in occ_df1['Task'].tolist():
        for occ2_task in occ_df2['Task'].tolist():
            token_set_ratio = fuzz.token_set_ratio(occ1_task,occ2_task)
            token_sort_ratio = fuzz.token_sort_ratio(occ1_task,occ2_task)
            ratio = fuzz.ratio(occ1_task,occ2_task)
            partial_ratio = fuzz.partial_ratio(occ1_task,occ2_task)
            partial_token_set_ratio = fuzz.partial_token_set_ratio(occ1_task,occ2_task)
            partial_token_sort_ratio = fuzz.partial_token_sort_ratio(occ1_task,occ2_task)

            token_set_ratios.append(token_set_ratio)
            token_sort_ratios.append(token_sort_ratio)
            ratios.append(ratio)
            partial_ratios.append(partial_ratio)
            partial_token_set_ratios.append(partial_token_set_ratio)
            partial_token_sort_ratios.append(partial_token_sort_ratio)

    # Calculate the averages of the lists
    avg_token_set_ratio = sum(token_set_ratios) / len(token_set_ratios)
    avg_token_sort_ratio = sum(token_sort_ratios) / len(token_sort_ratios)
    avg_ratio = sum(ratios) / len(ratios)
    avg_partial_ratio = sum(partial_ratios) / len(partial_ratios)
    avg_partial_token_set_ratio = sum(partial_token_set_ratios) / len(partial_token_set_ratios)
    avg_partial_token_sort_ratio = sum(partial_token_sort_ratios) / len(partial_token_sort_ratios)

    

    avg_token_set_ratio = np.median(token_set_ratios)
    avg_token_sort_ratio = np.median(token_sort_ratios)
    

    # Print the calculated averages
    print("Average Token Set Ratio:", avg_token_set_ratio)
    print("Average Token Sort Ratio:", avg_token_sort_ratio)

    return avg_token_set_ratio,avg_token_sort_ratio
    #print("Average Ratio:", avg_ratio)
    #print("Average Partial Ratio:", avg_partial_ratio)
    #print("Average Partial Token Set Ratio:", avg_partial_token_set_ratio)
    #print("Average Partial Token Sort Ratio:", avg_partial_token_sort_ratio)



occupations_tasks_dict = {
    'Biostatisticians': biostat_tasks,
    'Statisticians': stat_tasks,
    'Business Intelligence Analysts': bis_analyst,
    'Clinical Data Managers': clin_data_managers,
    'Remote Sensing Scientists and Technologists': remote_sensing_scientist,
    'Document Management Specialists': doc_man_spec,
    'Financial Quantitative Analysts': fin_quan_analyst,
    'Management Analysts': man_analyst,
    'Mathematicians': mathematicians,
    'Operations Research Analysts': ops_research_analysts
}


def tasks_below_avg_ratio(occ_df1,occ_df2,avg_ratio,sort):
    num = 0
    for occ1_task in occ_df1['Task'].tolist():
        for occ2_task in occ_df2['Task'].tolist():
            if sort:
                token_sort_ratio = fuzz.token_sort_ratio(occ1_task,occ2_task)
                if token_sort_ratio<avg_ratio:
                    num+=1
                
            else:
                token_set_ratio = fuzz.token_set_ratio(occ1_task,occ2_task)
                if token_set_ratio <avg_ratio:
                    num+=1
    return num

def tasks_above_avg_ratio(occ_df1,occ_df2,avg_ratio,sort):
    num = 0
    for occ1_task in occ_df1['Task'].tolist():
        for occ2_task in occ_df2['Task'].tolist():
            if sort:
                token_sort_ratio = fuzz.token_sort_ratio(occ1_task,occ2_task)
                if token_sort_ratio>avg_ratio:
                    num+=1
                
            else:
                token_set_ratio = fuzz.token_set_ratio(occ1_task,occ2_task)
                if token_set_ratio > avg_ratio:
                    num+=1
    return num

def get_plus_minus_one_avg(occ_df1,occ_df2,avg_ratio,sort):
    num = 0
    for occ1_task in occ_df1['Task'].tolist():
        for occ2_task in occ_df2['Task'].tolist():
            if sort:
                token_sort_ratio = fuzz.token_sort_ratio(occ1_task,occ2_task)
                if abs(token_sort_ratio-avg_ratio) <=1:
                    num+=1
                
            else:
                token_set_ratio = fuzz.token_set_ratio(occ1_task,occ2_task)
                if abs(token_set_ratio-avg_ratio) <=1:
                    num+=1
    return num



def token_set_q3(occ_df1,occ_df2):

    token_set_ratios = []
    matches  = 0
    for occ1_task in occ_df1['Task'].tolist():
        for occ2_task in occ_df2['Task'].tolist():
            token_set_ratio = fuzz.token_set_ratio(occ1_task,occ2_task)
            token_set_ratios.append(token_set_ratio)
            if token_set_ratio > 60:
                #print(token_set_ratio)
                #print(occ1_task)
                #print(occ2_task)
                #print()
                matches+=1
                break
    
    
    return matches, matches/len(occ_df1['Task'].tolist())*100
        

        
            
    

def amount_above_q3_token_set(occ_df1,occ_df2,q3):
    num = 0
    for occ1_task in occ_df1['Task'].tolist():
        for occ2_task in occ_df2['Task'].tolist():
            token_set_ratio = fuzz.token_set_ratio(occ1_task,occ2_task)
            if token_set_ratio > q3:
                num+=1
    return num



'''
for var_name, df in occupations_tasks_dict.items():
    if var_name == 'Business Intelligence Analysts':
        continue
    print(f"Comparing: {var_name} to Business Intelligence Analyst")
    print()
    token_set_ratio,token_sort_ratio = compare_occupations(df,occupations_tasks_dict['Business Intelligence Analysts'])
    
    num_below_token_set_ratio = tasks_below_avg_ratio(df,occupations_tasks_dict['Business Intelligence Analysts'],token_set_ratio,sort = False)
    num_below_token_sort_ratio = tasks_below_avg_ratio(df,occupations_tasks_dict['Business Intelligence Analysts'],token_sort_ratio,sort = True)
    print(f'Number of pairs below average token set ratio: {num_below_token_set_ratio}')
    print(f'Number of pairs below average token sort ratio: {num_below_token_sort_ratio}')


    num_above_token_set_ratio = tasks_above_avg_ratio(df,occupations_tasks_dict['Business Intelligence Analysts'],token_set_ratio,sort = False)
    num_above_token_sort_ratio = tasks_above_avg_ratio(df,occupations_tasks_dict['Business Intelligence Analysts'],token_sort_ratio,sort = True)
    #print(f'Number of pairs above average token set ratio: {num_above_token_set_ratio}')
    #print(f'Number of pairs above average token sort ratio: {num_above_token_sort_ratio}')

    plus_minus_one_token_set_avg = get_plus_minus_one_avg(df,occupations_tasks_dict['Business Intelligence Analysts'],token_set_ratio,sort = False)
    plus_minus_one_token_sort_avg = get_plus_minus_one_avg(df,occupations_tasks_dict['Business Intelligence Analysts'],token_sort_ratio,sort = True)
    #print(f'Number of pairs plus or minus one of average token set ratio: {plus_minus_one_token_set_avg}')
    #print(f'Number of pairs plus or minus one of average token sort ratio: {plus_minus_one_token_sort_avg}')
    q3_token_set_ratio = token_set_q3(df,occupations_tasks_dict['Business Intelligence Analysts'])
    num_above_q3_token_set_ratio = amount_above_q3_token_set(df,occupations_tasks_dict['Business Intelligence Analysts'],q3_token_set_ratio)
    print(f'Number of pairs above token set 95th percentile: {num_above_q3_token_set_ratio}')
    print()


'''            



import numpy as np
def get_task_corrs():
    corr_matrix = []  # Initialize as a list

    for occ1_name, occ1_df in occupations_tasks_dict.items():
        corrs = []
        for occ2_name, occ2_df in occupations_tasks_dict.items():
            matches, percentage_matching = token_set_q3(occ1_df, occ2_df)
            corrs.append(percentage_matching)
        corr_matrix.append(corrs)  # Use the list append method

    return np.array(corr_matrix)  # Convert the list to a NumPy array






        

