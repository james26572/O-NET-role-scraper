import pandas as pd

biostat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Biostatisticians/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
bis_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Business Intelligence Analysts/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
clin_data_managers = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Clinical Data Managers/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
market = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Market Research Analysts and Marketing Specialists/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
advertising = pd.read_csv("C:/Users/buckl\SkillsTrust\O-NET-role-scraper\occupations\Advertising and Promotions Managers/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
fin_quan_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Financial Quantitative Analysts/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
man_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Management Analysts/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
mathematicians = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Mathematicians/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
ops_research_analysts = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Operations Research Analysts/detailed_work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')




def compare_work_activities(occ1,occ2):
    
    matches = 0
    num_BI_skills = len(occ2['Detailed Work Activity'].tolist())
    

    for work_activity1 in occ1['Detailed Work Activity'].tolist():
        if work_activity1 in occ2['Detailed Work Activity'].tolist():
            
                matches += 1
    return matches,round((matches/num_BI_skills)*100,2)





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



import numpy as np
def get_occ_detailed_work_activities_corrs():
    corr_matrix = []  # Initialize as a list

    for occ1_name, occ1_df in occupations_tasks_dict.items():
        corrs = []
        for occ2_name, occ2_df in occupations_tasks_dict.items():
            matches, percentage_matching = compare_work_activities(occ1_df, occ2_df)
            corrs.append(percentage_matching)
        corr_matrix.append(corrs)  # Use the list append method

    return np.array(corr_matrix)  # Convert the list to a NumPy array




  