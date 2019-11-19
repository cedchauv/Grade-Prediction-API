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

    def predict_json(self, student_json, studentamount, variables):
        with open('jsonExample.json') as f:
                data = json.load(f)
        #npayy = np.empty(shape=(studentamount,variables))
#        for x in data:
            #npayy[x] += data[x]
            #s = str(data[x])
       # ayy = np.array([[v for _,v in sorted(d["sex"].items())] for d in data] )
        print(data)

        #print(ayy)
        #return self.model.predict(np.asarray(data))

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

