import pandas as pd

df = pd.read_csv('./csv/student-por.csv')

#code below for reduced dataset

#df1 = df[['sex','age','address','traveltime','studytime','failures','schoolsup','activities','internet','romantic',
# 'freetime','goout','Dalc','Walc','health','G3']]
#df1.to_csv('./csv/trainingdataP.csv',index=False)

#df2 = pd.read_csv('./csv/trainingdataP.csv')
# removes students who score 0
# df = df[df.G3 != 0]

# We need to process the data so everything becomes integers able to be used by numpy
# this replaces non-integer values in column 0 and 2 with 1 or 0
#df2.iloc[:,0] = df2.iloc[:,0].replace('F',0,regex=True)
#df2.iloc[:,0] = df2.iloc[:,0].replace('M',1,regex=True)
#df2.iloc[:,2] = df2.iloc[:,2].replace('U',0,regex=True)
#df2.iloc[:,2] = df2.iloc[:,2].replace('R',1,regex=True)
# columns 6 to 9 all have yes or no values, which we replace with 1 and 0
#for x in range(6,10):
    #df2.iloc[:,x] = df2.iloc[:,x].replace('yes',1, regex=True)
    #df2.iloc[:,x] = df2.iloc[:,x].replace('no',0,regex=True)

#df.to_csv('./csv/processed-tdataP.csv', index=False)

# -----------------------------------------------------------------------
# code below for complete dataset
df = df[df.G3 != 0]

df.iloc[:,0] = df.iloc[:,0].replace('GP',0, regex=True)
df.iloc[:,0] = df.iloc[:,0].replace('MS',1, regex=True)


df.iloc[:,1] = df.iloc[:,1].replace('F',0,regex=True)
df.iloc[:,1] = df.iloc[:,1].replace('M',1,regex=True)
df.iloc[:,3] = df.iloc[:,3].replace('U',0,regex=True)
df.iloc[:,3] = df.iloc[:,3].replace('R',1,regex=True)

df.iloc[:,4] = df.iloc[:,4].replace('GT3',1, regex=True)
df.iloc[:,4] = df.iloc[:,4].replace('LE3',0, regex=True)
df.iloc[:,5] = df.iloc[:,5].replace('A',1, regex=True)
df.iloc[:,5] = df.iloc[:,5].replace('T',0, regex=True)
df.iloc[:,8] = df.iloc[:,8].replace('at_home',0, regex=True)
df.iloc[:,8] = df.iloc[:,8].replace('health',1, regex=True)
df.iloc[:,8] = df.iloc[:,8].replace('other',2, regex=True)
df.iloc[:,8] = df.iloc[:,8].replace('services',3, regex=True)
df.iloc[:,8] = df.iloc[:,8].replace('teacher',4, regex=True)
df.iloc[:,9] = df.iloc[:,9].replace('at_home',0, regex=True)
df.iloc[:,9] = df.iloc[:,9].replace('health',1, regex=True)
df.iloc[:,9] = df.iloc[:,9].replace('other',2, regex=True)
df.iloc[:,9] = df.iloc[:,9].replace('services',3, regex=True)
df.iloc[:,9] = df.iloc[:,9].replace('teacher',4, regex=True)
df.iloc[:,10] = df.iloc[:,10].replace('home',0, regex=True)
df.iloc[:,10] = df.iloc[:,10].replace('course',1, regex=True)
df.iloc[:,10] = df.iloc[:,10].replace('reputation',2, regex=True)
df.iloc[:,10] = df.iloc[:,10].replace('other',3, regex=True)
df.iloc[:,11] = df.iloc[:,11].replace('mother',0, regex=True)
df.iloc[:,11] = df.iloc[:,11].replace('father',1, regex=True)
df.iloc[:,11] = df.iloc[:,11].replace('other',2, regex=True)


for x in range(15,23):
    df.iloc[:,x] = df.iloc[:,x].replace('yes',1, regex=True)
    df.iloc[:,x] = df.iloc[:,x].replace('no',0,regex=True)


df.to_csv('./csv/complete-processed.csv',index=False)