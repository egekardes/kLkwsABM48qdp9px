# kLkwsABM48qdp9px

In this task, I used a neural network approach to predict desired feature Y. I tried using 'binary_crossentropy' and 'squared_hinge' loss funtions and chose 'binary_crossentropy' as my loss function. For feature engineering, I created and made observations from correlation matrix of the dataset. Hence I did not used X2 and X4 columns due to their low correlation with Y, on the other hand I added columns with values such that X1/X5, X1/X6, X1xX5, and X1xX6 , since correlation values between X1-X6 and X1-X5 were the maximum correlation values in the matrix. I have implemented the model by using several combinations of those 4 extra attributes and found out it is the best to use them all together. By using such an augmented dataset, the model has operated with around %70 accuracy. Unfortunately, it can not be said that every evaluation has reached an accuracy over %73 as desired. However I beleive that model has promising results and mentality which would have much better results if it has trained and tested using more data.  

Descriptions of the files under the repo can be found below, please be aware of the comments in the files as well.


##ACME-HappinessSurvey2020.csv
It is the dataset that consists of 6 attributes and 1 result label rows and 126 data rows.

##create_correlation.py
Python script to create correlation matrix of dataset and convert to a csv file namely "Correlation Matrix.csv". That csv file ist used to drop unnecessary columns from dataset.

##create_model.py
This python script defines and compiles neural network model to predict desired attribute.

##format_input.py
It is the python script that is responsible for removing undesired columns, adding extra attributes using observations from "Correlation Matrix.csv" to provide a better prediction accuracy to model. It also oversamples the dataset.

##fit.py
It simply calls fit() method with the training data derived from by "format_input.py".

##evaluate.py
It evaluates model with the test data derived from by "format_input.py".

##main.sh
This shell script is used for a automated pipelining of the process. It runs the python scripts in order to train and evaluate the model successfully.




