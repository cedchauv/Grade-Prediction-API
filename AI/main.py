import AI.GradeAI as GradeAI
import AI.DataProcesser as DataProcessor
import numpy as np

dataset = np.loadtxt('Dataset\\processed-tdata2.csv', delimiter=',',skiprows=1)

trainingData, labelData = DataProcessor.generate_training_and_label_data(dataset, 0)
print(trainingData[0])
fixedData = []
for i in range(len(trainingData)):
    fixedData.append(np.delete(trainingData[i], 10))
    print(fixedData[i])

fixedData = np.array(fixedData)


model = GradeAI.create_model(len(fixedData[0]))
GradeAI.start_training_session(model, fixedData, labelData, 720, 10)
model.save("model.h5")