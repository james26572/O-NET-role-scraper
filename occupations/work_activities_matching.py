import pandas as pd

biostat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Biostatisticians/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
stat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Statisticians/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
bis_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Business Intelligence Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
clin_data_managers = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Clinical Data Managers/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
remote_sensing_scientist = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Remote Sensing Scientists and Technologists/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
doc_man_spec = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Document Management Specialists/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
fin_quan_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Financial Quantitative Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
man_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Management Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
mathematicians = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Mathematicians/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
ops_research_analysts = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Operations Research Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
def compare_work_activities(occ1,occ2):
    matches = 0
    num_BI_skills = len(occ2['Work Activity'].tolist())
    

    for work_activity1 in occ1['Work Activity'].tolist():
        if work_activity1 in occ2['Work Activity'].tolist():
            
                matches += 1
    return matches,round((matches/num_BI_skills)*100,2)





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


import numpy as np
def get_work_activities_corrs():
    corr_matrix = []  # Initialize as a list

    for occ1_name, occ1_df in occupations_tasks_dict.items():
        corrs = []
        for occ2_name, occ2_df in occupations_tasks_dict.items():
            matches, percentage_matching = compare_work_activities(occ1_df, occ2_df)
            corrs.append(percentage_matching)
        corr_matrix.append(corrs)  # Use the list append method

    return np.array(corr_matrix)  # Convert the list to a NumPy array





#print(get_work_activities_corrs())