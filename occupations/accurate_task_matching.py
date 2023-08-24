import openai
import pandas as pd
import numpy as np



openai.api_key = "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"



biostat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Biostatisticians/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
bis_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Business Intelligence Analysts/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
clin_data_managers = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Clinical Data Managers/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
market = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Market Research Analysts and Marketing Specialists/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
advertising = pd.read_csv("C:/Users/buckl\SkillsTrust\O-NET-role-scraper\occupations\Advertising and Promotions Managers/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
fin_quan_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Financial Quantitative Analysts/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
man_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Management Analysts/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
mathematicians = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Mathematicians/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')
ops_research_analysts = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Operations Research Analysts/tasks.csv", header=0, encoding='utf-8', encoding_errors='replace')



occupations_tasks_dict = {

    'Business Intelligence Analysts': bis_analyst,
    'Biostatisticians': biostat_tasks,
    'Clinical Data Managers': clin_data_managers,
    'Financial Quantitative Analysts': fin_quan_analyst,
    'Management Analysts': man_analyst,
    'Mathematicians': mathematicians,
    'Operations Research Analysts': ops_research_analysts,
    'Advertising and Promotions Manager':advertising,
    'Market Research Analysts and Marketing Specialists':market
}

import time


def do_tasks_match(task1,task2):
    # Define the system message
    system_msg = 'You are a helpful assistant who understands job tasks.'

# Define the user message
    user_msg = f'''Tell me whether these tasks are the same. If both tasks involve acheiving
      the same goals, are in the same industries, and the specific skills and responsibilities required
      are the same, output "Match". Otherwise output "Not a match". Task 1: {task1}
     Task 2: {task2}. The output has to be either "Match" or "Not a match", do not give an explanation
     or output anything else.
      
'''
    retries = 3
    while retries > 0:
        try:
# Create a dataset using GPT
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            request_timeout = 15,
                                        messages=[{"role": "system", "content": system_msg},
                                         {"role": "user", "content": user_msg}],
                                         )
    
            match = response["choices"][0]["message"]["content"]

    
    

            print(match)
            return match
            
        except Exception as e:    
         if e: 
             print(e)   
             print('Timeout error, retrying...')    
             retries -= 1    
             time.sleep(5)    
         else:    
             raise e    
    return "not working"

#print(do_tasks_match(task1,task2))



def compare_tasks(occ1_df,occ2_df):
    matches = 0

    for task1 in occ1_df['Task'].tolist():
        for task2 in occ2_df['Task'].tolist():
            print()
            print(task1)
            print(task2)
            do_match =  do_tasks_match(task1,task2)
            if do_match.lower() == "match":
                print("Match")
                
                
                matches+=1
                break
            elif do_match.lower() == "do not match":
                print("Do not match")
            else:
                print(do_match)
            
    return matches, (matches/len(occ1_df['Task'].tolist()))*100


def get_task_corrs():
    corr_matrix = []
    for occ1_name, occ1_df in occupations_tasks_dict.items():
        corrs = []
        for occ2_name, occ2_df in occupations_tasks_dict.items():
            matches, percentage_matching = compare_tasks(occ1_df, occ2_df)
            corrs.append(percentage_matching)
        corr_matrix.append(corrs)  # Use the list append method

    

    output =  np.array(corr_matrix)  # Convert the list to a NumPy array
    np.save('matrix_data_working.npy', output)
    return output


print(get_task_corrs())