import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./csv/processed-tdataP.csv')
df2 = pd.read_csv('./csv/processed-tdata2.csv')

plt.hist(df['G3'], label='por')
plt.hist(df2['G3'],label='mat')
plt.title('Histogram')
plt.xlabel('score')
plt.ylabel('Students')
plt.legend(loc='upper left')
plt.show()


