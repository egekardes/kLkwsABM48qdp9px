#!/usr/bin/env python3

import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from pandas.core.indexes.base import Index

def format_csv(filename):

    df = pd.read_csv(filename)

    df = df.assign( X1dX5 = df['X1'] / df['X5'])
    df = df.assign( X1dX6 = df['X1'] / df['X6'])
    df = df.assign( X1xX5 = df['X1'] * df['X5'])
    df = df.assign( X1xX6 = df['X1'] * df['X6'])

    columns =['Y', 'X1','X3', 'X5', 'X6', 'X1dX5', 'X1dX6', 'X1xX5', 'X1xX6']
    formatted = df[columns]

    pd.DataFrame(formatted).to_csv("formatted.csv", index = False)

def create_train_data(filename, rows):

    df = pd.read_csv(filename, nrows=rows)

    labels = df.iloc[:,[0]].copy()
    labels = np.array(labels)

    features = df.iloc[:, 1:].copy()
    features = np.array(features)

    oversample = RandomOverSampler(sampling_strategy='all')
    features_over, labels_over = oversample.fit_resample(features, labels)

    return features_over, labels_over

def create_test_data(filename, start, end):

    df = pd.read_csv(filename)

    df = df.drop([start, end])

    labels = df.iloc[:,[0]].copy()
    labels = np.array(labels)

    features = df.iloc[:, 1:].copy()
    features = np.array(features)

    return features, labels


fname='ACME-HappinessSurvey2020.csv' ## to be changed in case of change in input file name

format_csv(fname)



