#!/usr/bin/env python3

from format_input import create_test_data
from math import floor
from  tensorflow.keras.models import load_model

filename = 'formatted.csv'
num_rows = 0
for row in open(filename):
    num_rows += 1

ratio = 0.85 ## percentage of data in dataset to be used as training data

num_rows = floor(num_rows*ratio)

TX, TY = create_test_data(filename, 1, num_rows-1)

model = load_model('cust_happiness')

_, accuracy = model.evaluate(TX, TY)
print('Accuracy: %.2f' % (accuracy*100))
