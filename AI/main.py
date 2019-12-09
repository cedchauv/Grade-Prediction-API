import AI.GradeAI as GradeAI
import AI.DataProcesser as DataProcessor
import AI.Advisor as Advisor
import numpy as np

def test():
    Advisor.generate_improvement_list([0,16,0,1,2,0,0,0,0,0,3,2,1,2,5], 18)

def generate_model():
    dataset = np.loadtxt('Dataset\\processed-tdata2.csv', delimiter=',',skiprows=1)

    trainingData, labelData = DataProcessor.generate_training_and_label_data(dataset, 0)
    print(trainingData[0])
    fixedData = []
    for i in range(len(trainingData)):
        fixedData.append(np.delete(trainingData[i], 10))
        print(fixedData[i])

    fixedData = np.array(fixedData)


    model = GradeAI.create_single_layer_model(len(fixedData[0]))
    GradeAI.start_training_session(model, fixedData, labelData, 5000, 10)
    model.save("weights.h5")

test()
