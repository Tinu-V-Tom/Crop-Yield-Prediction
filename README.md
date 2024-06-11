# Crop-Yield-Prediction
This project mainly aims to predict the yield of a certain crop using Decision Tree Regression. 
year,rainfall,pesticides,temperature,area,crop item  are the features related to the crop yield production.
So after importing the file I cleaned the dataset by removing null values and then removed unwanted columns by selecting these related 
fields. After the EDA process I split the data using train_test_split function from Sklearn.modelselection. Then after checking for different
regression models such as LinearRegression,KNN,DecisionTree etc., Decision tree performed well in terms of accuracy. So i fitted that model and deploy the particular model by developing a web application using streamlit. 

