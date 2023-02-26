import numpy as np
import tensorflow as tf
from tensorflow.keras import regularizers
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import csv

# Load training data from CSV file
train_data = pd.read_csv('FinalNeuroMorphologicalTRAINING.csv')
#Substitute whatever your file name is, assuming your file is in the same directory
x_train = train_data.iloc[:, :21].values
y_train = train_data.iloc[:, 21:].values

# Load testing data from CSV file
test_data = pd.read_csv('FinalNeuroMorphologicalTEST.csv')
#Substitute whatever your file name is, assuming your file is in the same directory
x_test = test_data.iloc[:, :21].values
y_test = test_data.iloc[:, 21:].values

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001), input_shape=(21,)),
    tf.keras.layers.Dense(64, activation='relu', kernel_regularizer=regularizers.l2(0.001)),
    tf.keras.layers.Dense(147, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'],)

#Intialize headers into our file
with open('trialRuns.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header row to the file
    writer.writerow(['Test Accuracy', 'Accuracy', 'Mean Squared Error', 'R-squared', 'Mean Absolute Error', 'F1 Score'])

# Train and test the model 100 different times in order to average results
for i in range(100):
    # Train the model
    model.fit(x_train, y_train, epochs=500, batch_size=32)

    # Evaluate the model using the .evaluate
    test_loss, test_acc = model.evaluate(x_test, y_test)

    # Use of Sci-Kit Libraries
    prediction = model.predict(x_test)
    prediction = np.argmax(model.predict(x_test), axis=-1)
    mse = mean_squared_error(y_test, prediction)
    r2 = r2_score(y_test, prediction)
    mae = mean_absolute_error(y_test, prediction)
    acc = accuracy_score(y_test, prediction)
    f1 = f1_score(y_test, prediction, average='macro')

    #Print out the statistical analysis
    print('Accuracy (Using .evaluate)', test_acc)
    print("Accuracy (Using .predict):", acc)
    print("Mean Squared Error:", mse)
    print("R-squared:", r2)
    print("Mean Absolute Error:", mae)
    print("F1 Score:", f1)

    #Store the results in an array to print into our csv file
    results = [test_acc, acc, mse, r2, mae, f1]
    with open('trialRuns.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the results to the file as a row
        writer.writerow(results)

