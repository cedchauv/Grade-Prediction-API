import numpy as np
from keras.models import Sequential
from keras.layers import Dense


dataset = np.loadtxt('processed-tdata2.csv', delimiter=',',skiprows=1)
x = dataset[:-10,0:15]
y = dataset[:-10,15]

model = Sequential()
model.add(Dense(25,input_dim = 15, activation='relu'))
model.add(Dense(75,activation='relu'))
model.add(Dense(125,activation='relu'))
model.add(Dense(50,activation='relu'))
model.add(Dense(1,activation='relu'))

model.compile(loss='mean_square_logarithmic_error',optimizer='adam',metrics=['accuracy'])

model.fit(x, y, epochs=1200, batch_size=5)

_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

predictions = model.predict(dataset[-10:, 0:15])
for i in range(len(predictions)):
    print(predictions[i], dataset[-(10-i), 15])


