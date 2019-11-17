import keras
from numpy import loadtxt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten
import pandas as pd

data = pd.read_csv("C:\\Users\\Frunkles\\Desktop\\student-mat.csv", delimiter=',',
                   usecols=(["sex", "age", "address", "traveltime", "studytime", "failures", "activities", "internet", "romantic", "schoolsup", "goout", "Dalc", "Walc", "health", "G3"]))
data = data.values

for x in range(len(data)):
    for y in range(len(data[0])):
        if y == 0:
            if data[x][y] == "M":
                data[x][y] = 1
            else:
                data[x][y] = 0
        if y == 2:
            if data[x][y] == "U":
                data[x][y] = 1
            else:
                data[x][y] = 0
        if y == 6 or y == 7 or y == 8 or y == 9:
            if data[x][y] == "yes":
                data[x][y] = 1
            else:
                data[x][y] = 0

X = data[:-10,0:14]
y = data[:-10,14]

model = Sequential()
model.add(Dense(25, input_dim=14, activation='relu'))
model.add(Dense(75, activation="relu"))
model.add(Dense(125, activation="relu"))
model.add(Dense(50, activation="relu"))
model.add(Dense(1, activation='relu'))

model.compile(loss='mean_absolute_error', optimizer="adam", metrics=['accuracy'])
model.fit(X, y, epochs=2000, batch_size=5)

_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(data[-10:, 0:14])
for i in range(len(predictions)):
    print(predictions[i], data[-(10-i), 14])

myData = np.array([[1, 18, 1, 5, 5, 4, 0, 0, 1, 0, 5, 5, 1, 1]])
predictions = model.predict(myData)
print(predictions)

top = []
for element in data:
    if element[14] >= 19:
        top.append(element)

leastDiff = 0
topDiff = 0

for i in range(len(top)):
    diff = 0
    for j in range(len(top[0]) - 1):
        if j == 1:
            diff += abs(((top[i][j] - 15) / 7) - ((myData[0][j] - 15) / 7))
        elif j == 3 or j == 4 or j == 10 or j == 11 or j == 12 or j == 13:
            diff += abs(((top[i][j] - 1) / 4) - ((myData[0][j] - 1) / 4))
        elif j == 5:
            diff += abs((top[i][j] / 4) - (myData[0][j] / 4))
        else:
            diff += abs(top[i][j] - myData[0][j])
    print(diff)
    if diff < topDiff or topDiff == 0:
        topDiff = diff
        leastDiff = top[i]

print(leastDiff)
print(myData[0])

pos = 0
mostDiff = 0
for i in range(len(myData[0])):
    diff = 0
    if i == 1:
        diff = abs(((myData[0][i] - 15) / 7) - ((leastDiff[i] - 15) / 7))
    elif i == 3 or i == 4 or i == 10 or i == 11 or i == 12 or i == 13:
        diff = abs(((myData[0][i] - 1) / 4) - ((leastDiff[i] - 1) / 4))
    elif i == 5:
        diff = abs((myData[0][i] / 4) - (leastDiff[i]  / 4))
    else:
        diff = abs(myData[0][i] - leastDiff[i])
    if diff > mostDiff:
        mostDiff = diff
        pos = i

print("improve value of position", pos)