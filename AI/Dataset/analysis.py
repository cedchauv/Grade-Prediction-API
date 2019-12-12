import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('./csv/processed-tdataP.csv')
df2 = pd.read_csv('./csv/processed-tdata2.csv')
df3 = pd.read_csv('./csv/complete-processed.csv')

#plt.hist(df['G3'], label='portugese data')
#plt.hist(df2['G3'],label='math data')
#plt.title('Grade Distribution')
#plt.xlabel('G3 score')
#plt.ylabel('Amount of Students')
#plt.legend(loc='upper left')
# plt.show()
plt.figure(figsize=(10,8))
corr = abs(df3.corr())
sns.heatmap(corr, square=True)
plt.title('Correlation heatmap - Complete Dataset')
plt.show()





