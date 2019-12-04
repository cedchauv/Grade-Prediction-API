def generate_training_and_label_data(data, validation_data_size):
    training_data = data[:-(validation_data_size + 1), 0:-1]
    label_data = data[:-(validation_data_size + 1), -1]

    return training_data, label_data


def generate_validation_and_label_data(data, validation_data_size):
    validation_data = data[-validation_data_size:, 0:len(data[0])-1]
    label_data = data[-validation_data_size:, len(data[0])-1]

    return validation_data, label_data
