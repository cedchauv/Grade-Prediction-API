import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot as plt
dataset = np.loadtxt('./csv/complete-processed.csv', delimiter=',',skiprows=1)
split = 1
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

history = model.fit(x, y, epochs=400,batch_size=5, validation_split=0.20)
model.save('predictormodelComplete.h5')

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

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