import numpy as np
from keras.models import Sequential
from keras.layers import Dense

dataset = np.loadtxt('./csv/complete-processed.csv', delimiter=',',skiprows=1)
split = 130
#15 reduced, 32 complete
variables = 32

x = dataset[:-split,0:variables]
y = dataset[:-split,variables]

#def baseline_model():
model = Sequential()
model.add(Dense(25,input_dim = variables,kernel_initializer='normal', activation='relu'))
model.add(Dense(55,activation='relu'))
model.add(Dense(125,activation='relu'))
model.add(Dense(70,activation='relu'))
model.add(Dense(40,activation='relu'))
model.add(Dense(40,activation='relu'))


model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])

model.fit(x, y, epochs=720,batch_size=5)
model.save('predictormodelComplete.h5')

a = dataset[-split:,0:variables]
b = dataset[-split:,variables]

predictions = model.predict(a)
error = 0
for i in range(len(predictions)):
    print(predictions[i].round(), dataset[-(split-i), variables])
    error += abs(predictions[i].round() - dataset[-(split-i),variables])

error = error / split

_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))

_, accuracy = model.evaluate(a, b)
print('Pinpoint Accuracy: %.2f' % (accuracy*split), '/', split)
print('Percentage accuracy: %.2f' % (accuracy*100))
print("Average error %.2f" % error)