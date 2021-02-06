#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.callbacks import EarlyStopping
from format_input import create_train_data
from math import floor


filename = 'formatted.csv' # TO BE CHANGED
num_rows = 0
for row in open(filename):
    num_rows += 1

ratio = 0.85 ## percentage of data in dataset to be used as training data

num_rows = floor(num_rows*ratio)

model = load_model('cust_happiness')

X, Y = create_train_data(filename, num_rows)

#es = EarlyStopping(monitor='accuracy', patience=100, mode='max')
model.fit(x=X,y=Y,shuffle=True,validation_split=0.15,batch_size=2,epochs=130,verbose=2)

model.save('cust_happiness')