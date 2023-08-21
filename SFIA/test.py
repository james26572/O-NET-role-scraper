import pandas as pd

# Specify the 'replace' option for the errors parameter to handle non-UTF-8 characters
df = pd.read_csv('SFIA\level_1.csv', header=0, encoding='utf-8',encoding_errors='replace')

print(df['Autonomy'][0])
