import numpy as np
import matplotlib.pyplot as plt
import ipdb
from keras.models import model_from_json

y_test = np.load("data/y_test.npy")
x_test = np.load("data/x_test.npy")
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

print("load the model")
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
loaded_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("")


# print("evaluate the model")
# loss, accuracy = loaded_model.evaluate(x_test, y_test)
# print("loss: {}".format(loss))
# print("accuracy: {} %".format(100*accuracy))


def predit_test_point(data_index, x_test, y_test):
    """
        text if the model predicts
        the correct class
        for a given datapoint from
        the mnist database.
    """
    nb_test_data = x_test.shape[0]
    if data_index > nb_test_data:
        raise ValueError(f"data index too large : only {nb_test_data} test samples available")

    print(f"test data point {data_index}")
    true_label = y_test[data_index]

    # prediction of the model
    pred = loaded_model.predict(x_test[data_index].reshape(1, 28, 28, 1))
    predicted_label = pred.argmax()
    if true_label == predicted_label:
        print(f"correct prediction: {predicted_label}")
        title = f"testing point: {data_index}\ntrue label: {true_label}\npredicted label: {predicted_label} \nOK"
    else:
        print(f"-- ! wrong prediction: {predicted_label} instead of {true_label}")
        title = f"testing point: {data_index}\ntrue label: {true_label}\npredicted label: {predicted_label}\nMISTAKE"

    # print the result
    image = x_test[data_index][:, :, 0]
    plt.imshow(image, cmap="Greys")
    plt.title(title)
    plt.savefig("images/prediction_{data_index}.pdf")
    plt.close()


predit_test_point(1278, x_test, y_test)
predit_test_point(178, x_test, y_test)
predit_test_point(18, x_test, y_test)
predit_test_point(17, x_test, y_test)
predit_test_point(278, x_test, y_test)
predit_test_point(7278, x_test, y_test)
predit_test_point(9278, x_test, y_test)
predit_test_point(4275, x_test, y_test)
