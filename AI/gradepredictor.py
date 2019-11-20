from keras.models import Sequential
import pandas as pd
from keras.models import load_model
import numpy as np
import json


class GradePredictor:

    def __init__(self, modelpath ='predictormodel.h5'):
        self.model = load_model(modelpath)
        #self.training_data = './csv/processed-tdataP.csv'

    # method with numpy array input
    def predict_np(self, student_data):
        return np.concatenate(self.model.predict(student_data).round())

    # method with csv file input
    def predict_csv(self, student_csv):
        return self.model.predict(np.loadtxt(student_csv, delimiter=',', skiprows=1))

    def json_convert(self, jsonobject):
        with open(jsonobject) as f:
                data = json.load(f)
        data = data["studentProfile"]
        data.pop("userId")
        print(data)
        for x, y  in data.items():
            if y == 'M' or  y == 'R' or y == True:
                data[x] = 1
            elif y == 'F' or y == 'U' or y == False:
                data[x] = 0
        numpy = np.fromiter(data.values(), dtype=float)
        numpy = np.append(numpy, 1)
        numpy = np.asmatrix(numpy)
        return numpy

    def predict_json(self, student_json):
        return self.model.predict(self.json_convert(student_json))

    def evaluate_csv(self, student_csv, variables):
        dataset = np.loadtxt(student_csv, delimiter=',', skiprows=1)
        a = dataset[:, 0:variables]
        b = dataset[:, variables]
        predictions = self.model.predict(a)
        error = 0
        for i in range(len(predictions)):
            print(predictions[i].round(), dataset[i, variables])
            error += abs(predictions[i].round() - dataset[i, variables])
            error = error / len(predictions)
        _, accuracy = self.model.evaluate(a, b)
        print('Pinpoint Accuracy: %.2f' % (accuracy * len(predictions)), '/', len(predictions))
        print('Percentage accuracy: %.2f' % (accuracy * 100))
        print("Average error %.2f" % error)

    def append_dataset_csv(self, data):
        df = pd.read_csv('./csv/processed-tdataP - Copy.csv')
        df2 = pd.read_csv(data)
        df = df.append(df2, ignore_index=True)
        df.to_csv('./csv/appendeddata.csv', index=False)

    def append_dataset_np(self,data):
        df = pd.read_csv('./csv/processed-tdataP - Copy.csv')
        df2 = data
        df = df.append(df2)
        df.to_csv('./csv/appendeddata.csv')

    def retrain_model(self):
        print('hej')

