import pandas as pd

biostat_tasks = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Biostatisticians/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
bis_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Business Intelligence Analysts/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
clin_data_managers = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Clinical Data Managers/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
market = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Market Research Analysts and Marketing Specialists/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
advertising = pd.read_csv("C:/Users/buckl\SkillsTrust\O-NET-role-scraper\occupations\Advertising and Promotions Managers/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
fin_quan_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Financial Quantitative Analysts/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
man_analyst = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Management Analysts/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
mathematicians = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Mathematicians/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')
ops_research_analysts = pd.read_csv("C:/Users/buckl/SkillsTrust/O-NET-role-scraper/occupations/Operations Research Analysts/knowledge.csv", header=0, encoding='utf-8', encoding_errors='replace')


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


def compare_knowledge(occ1,occ2):
    matches = 0
    knowledge_ratings = occ1['Importance'].tolist()

    num_occ1_knowledge_over_50 = len([val for val in knowledge_ratings if val >=50])

    

    for tech_skill1,importance in zip(occ1['Knowledge'].tolist(),occ1['Importance'].tolist()):
        for tech_skill2,importance2 in zip(occ2['Knowledge'].tolist(),occ2['Importance'].tolist()):
                if tech_skill1 == tech_skill2:
                    if abs(importance-importance2)<=5:
                        if importance >=50 and importance2>=50:
                     
            
                            matches += 1
    
                    
    return matches,round((matches/num_occ1_knowledge_over_50)*100,2)


import numpy as np

def get_knowledge_corrs():
    corr_matrix = []  # Initialize as a list

    for occ1_name, occ1_df in occupations_tasks_dict.items():
        corrs = []
        for occ2_name, occ2_df in occupations_tasks_dict.items():
            matches, percentage_matching = compare_knowledge(occ1_df, occ2_df)
            corrs.append(percentage_matching)
        corr_matrix.append(corrs)  # Use the list append method

    return np.array(corr_matrix)  # Convert the list to a NumPy array



