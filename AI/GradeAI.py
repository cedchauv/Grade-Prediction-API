from keras import Sequential
from keras.layers import Dense
from keras.models import load_model
import requests
import pandas as pd
import json
import numpy as np
import os

def get_model():
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'model.h5')
    model = load_model(filename)
    return model

def create_model(num_variables):
    model = Sequential()
    model.add(Dense(25, input_dim=num_variables, kernel_initializer='normal', activation='relu'))
    model.add(Dense(55, activation='relu'))
    model.add(Dense(125, activation='relu'))
    model.add(Dense(70, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(40, activation='relu'))
    model.add(Dense(1, activation='linear'))

    model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    return model


def start_training_session(model, training_data, label_data, epochs, batch_size):
    model.fit(training_data, label_data, epochs=epochs, batch_size=batch_size)
    model.save('model.h5')


# method with numpy array input
def predict_np(model, data):
    return model.predict(data)


def evaluate_dataset(model, dataset):
    data = dataset[:,0:-1]
    labels = dataset[:,-1]
    _, accuracy = model.evaluate(data, labels)
    return accuracy


def get_weights(model):
    return 0
