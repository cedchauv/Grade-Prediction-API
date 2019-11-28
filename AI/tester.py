from gradepredictor import GradePredictor
import numpy as np

model = GradePredictor('predictormodelY.h5')
model2 = GradePredictor()
x = np.array([[0,18,0,2,2,0,1,0,0,0,3,4,1,1,3]])
x = np.loadtxt('./csv/processed-tdataP - copy.csv', delimiter=',',skiprows=1)
# print(model.predict_np(x))
# print(model2.predict_csv('processed-tdataP - copy.csv'))
# model2.evaluate_csv('processed-tdataP.csv',15)
#model.append_dataset_csv('./csv/processed-tdataP - copy.csv')
print(model.predict_json('jsonExample.json'))