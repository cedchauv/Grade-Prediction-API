import AI.GradeAI as GradeAI
import AI.DataProcesser as DataProcessor
import AI.Advisor as Advisor
import numpy as np

def test():
    generate_model()
    # Advisor.generate_improvement_list([0,16,0,1,2,0,0,0,0,0,3,2,1,2,5], 18)

def generate_model():
    dataset = np.loadtxt('Dataset\\processed-tdata2.csv', delimiter=',',skiprows=1)

    trainingData, labelData = DataProcessor.generate_training_and_label_data(dataset, 0)

    model = GradeAI.create_model(len(trainingData[0]))
    GradeAI.start_training_session(model, trainingData, labelData, 720, 10)
    model.save("model.h5")

test()
