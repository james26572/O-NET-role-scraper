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
task_corrs = np.load('matrix_data_working.npy')/100



skills_corrs = get_occ_skill_corrs()
work_activities_corrs = get_work_activities_corrs()

abilities = get_abilities_corrs()
knowledge = get_knowledge_corrs()



#avg_occ_corrs = (tech_skills_corrs+detailed_work_activities_corrs+task_corrs+skills_corrs+work_activities_corrs+abilities)/600


avg_occ_corrs = task_corrs

occs = ['Business Intelligence Analysts', 'Biostatisticians', 'Clinical Data Managers',
         'Financial Quantitative Analysts', 'Management Analysts', 'Mathematicians',
           'Operations Research Analysts', 'Advertising and Promotions Manager',
             'Market Research Analysts and Marketing Specialists']

# Create the heatmap using seaborn
ax = sns.heatmap(
    avg_occ_corrs,
    vmin=0, vmax=1, 
    cmap=sns.diverging_palette(20, 220, n=200),
    square=True,
    xticklabels=occs,  # Set custom tick labels for columns
    yticklabels=occs  # Set custom tick labels for rows
)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=15,
    fontsize = 5,
    horizontalalignment='right'
)


plt.show()  # Display the heatmap






