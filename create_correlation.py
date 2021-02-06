#!/usr/bin/env python3
import pandas as pd

filename = 'ACME-HappinessSurvey2020.csv'

df = pd.read_csv(filename)
corr = df.corr(method='pearson')
corr.to_csv("Correlation Matrix.csv", index =False)