from occupations.tech_skills_matching import get_occ_tech_skills_corrs
from occupations.skills_matching import get_occ_skill_corrs
from occupations.work_activities_matching import get_work_activities_corrs
from occupations.detailed_work_activities_matching import get_occ_detailed_work_activities_corrs
from occupations.task_matching import get_task_corrs

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


tech_skills_corrs = get_occ_tech_skills_corrs()
detailed_work_activities_corrs = get_occ_detailed_work_activities_corrs()
task_corrs = get_task_corrs()



skills_corrs = get_occ_skill_corrs()
work_activities_corrs = get_work_activities_corrs()



avg_occ_corrs = (tech_skills_corrs+detailed_work_activities_corrs+task_corrs+skills_corrs+work_activities_corrs)/500


occs = ['Biostatisticians', 'Statisticians', 'Business Intelligence Analysts', 'Clinical Data Managers', 'Remote Sensing Scientists and Technologists', 'Document Management Specialists', 
        'Financial Quantitative Analysts', 'Management Analysts', 'Mathematicians', 'Operations Research Analysts']

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






