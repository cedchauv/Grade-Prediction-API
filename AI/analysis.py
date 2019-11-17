import pandas as pd

df = pd.read_csv('trainingdata.csv')

# We need to process the data so everything becomes integers able to be used by numpy
# this replaces non-integer values in column 0 and 2 with 1 or 0

df = df[df.G3 != 0]
df.iloc[:,0] = df.iloc[:,0].replace('F',0,regex=True)
df.iloc[:,0] = df.iloc[:,0].replace('M',1,regex=True)
df.iloc[:,2] = df.iloc[:,2].replace('U',0,regex=True)
df.iloc[:,2] = df.iloc[:,2].replace('R',1,regex=True)
# columns 6 to 9 all have yes or no values, which we replace with 1 and 0
for x in range(6,10):
    df.iloc[:,x] = df.iloc[:,x].replace('yes',1, regex=True)
    df.iloc[:,x] = df.iloc[:,x].replace('no',0,regex=True)


df.to_csv('processed-tdata2.csv', index=False)

#df1 = df[['sex','age','address','traveltime','studytime','failures','schoolsup','activities','internet','romantic',
# 'freetime','goout','Dalc','Walc','health','G3']]
#df1.to_csv('trainingdata.csv',index=False)