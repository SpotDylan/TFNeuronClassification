#This file is meant to import our neuron data, clean it, and build a model to which we can train and test.
import numpy as np
import tensorflow as tf
from numpy import loadtxt

from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.metrics import binary_crossentropy
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Import data from our local CSV files for training our model and testing it
dataset_testing = loadtxt('B:/Pycharm/Neuromorphology/testingdataset.csv', delimiter=',', skiprows=1)
dataset_training = loadtxt('B:/Pycharm/Neuromorphology/trainingdataset.csv', delimiter=',', skiprows=1)

x_test = dataset_testing[:,0:21]
y_test = dataset_testing[:,21].reshape(-1,1)
x_train = dataset_training[:,0:21]
y_train = dataset_training[:,21].reshape(-1,1)

def buildmodel(nhidden1, nhidden2, nhidden3):
    model = Sequential()
    model.add(Dense(nhidden1, input_dim=21, activation='relu'))
    model.add(Dense(nhidden2, activation='relu'))
    model.add(Dense(nhidden3, activation='relu'))
    model.add(Dense(1, activation='relu'))
    optimizer = Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=0, decay=0.00, amsgrad=False)
    model.compile(loss='mean_squared_error', optimizer = optimizer)
    history = model.fit(x_train, y_train, epochs=500, batch_size=10, validation_data=[x_test,y_test]) #validation_data = [x_test,y_train] later
    return np.min(history.history['val_loss']), model
