#!/usr/bin/env python3
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.metrics import binary_crossentropy, squared_hinge

model = Sequential([
        Dense(units=4,input_shape=(8,), activation='relu'),
        Dense(units=8,activation='relu'),
        Dense(units=16,activation='relu'),
        Dense(units=32,activation='relu'),
        Dense(units=8,activation='relu'),
        Dense(units=4,activation='relu'),
        Dense(units=1,activation='sigmoid')] #tanh
    )

#'binary_crossentropy' 'squared_hinge'

model.compile(loss='binary_crossentropy', optimizer='Adam', metrics=['accuracy'])

model.save('cust_happiness')