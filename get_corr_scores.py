from occupations.tech_skills_matching import get_occ_tech_skills_corrs
from occupations.skills_matching import get_occ_skill_corrs
from occupations.work_activities_matching import get_work_activities_corrs
from occupations.detailed_work_activities_matching import get_occ_detailed_work_activities_corrs
from occupations.task_matching import get_task_corrs
from occupations.abilities_matching import get_abilities_corrs
from occupations.knowledge_matching import get_knowledge_corrs

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


tech_skills_corrs = get_occ_tech_skills_corrs()
detailed_work_activities_corrs = get_occ_detailed_work_activities_corrs()
task_corrs = np.load('matrix_data_working.npy')




skills_corrs = get_occ_skill_corrs()
work_activities_corrs = get_work_activities_corrs()

abilities = get_abilities_corrs()
#knowledge = get_knowledge_corrs()



avg_occ_corrs = (0.9*tech_skills_corrs+
                 0.9*detailed_work_activities_corrs+
                 0.9*task_corrs+
                 0.9*skills_corrs+
                 1.5*work_activities_corrs+
                 0.9*abilities)/600


    



occs =  [
    "BIA",   # Business Intelligence Analyst
    "BIOSTA",  # Biostatistician
    "CDM",   # Clinical Data Manager
    "FQA",   # Financial Quantitative Analyst
    "MA",    # Management Analyst
    "MATH",  # Mathematician
    "ORA",   # Operations Research Analyst
    "APM",   # Advertising and Promotions Manager
    "MRAM"   # Market Research Analysts and Marketing Specialists
]

# Create the heatmap using seaborn
ax = sns.heatmap(
    avg_occ_corrs,
    vmin=0, vmax=1, 
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,
    annot = True,
    fmt = ".2f",
    xticklabels=occs,  # Set custom tick labels for columns
    yticklabels=occs  # Set custom tick labels for rows
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=30,
    fontsize = 10,
    horizontalalignment='right'
)


plt.show()  # Display the heatmap






