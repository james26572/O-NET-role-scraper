import pandas as pd

biostat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Biostatisticians/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
bis_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Business Intelligence Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
clin_data_managers = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Clinical Data Managers/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
market = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Market Research Analysts and Marketing Specialists/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
advertising = pd.read_csv("C:/Users/buckl\SkillsTrust\O-NET-role-scraper\occupations\Advertising and Promotions Managers/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
fin_quan_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Financial Quantitative Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
man_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Management Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
mathematicians = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Mathematicians/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')
ops_research_analysts = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Operations Research Analysts/work_activities.csv", header=0, encoding='utf-8', encoding_errors='replace')





def compare_work_activities(occ1,occ2):
    matches = 0
    work_ratings = occ1['Importance'].tolist()

    num_work_ratings_over_50 = len([val for val in work_ratings if val >=50])
    

    for work_activity1,importance in zip(occ1['Work Activity'].tolist(),occ1['Importance'].tolist()):
        for work_activity2,importance2 in zip(occ2['Work Activity'].tolist(),occ2['Importance']):
                if work_activity1 == work_activity2:
                     if abs(importance-importance2)<=5:
                        if importance >=50 and importance2>=50:
            
                            matches += 1
    return matches,round((matches/num_work_ratings_over_50)*100,2)





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