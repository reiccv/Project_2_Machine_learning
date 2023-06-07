# Project 2 Machine learning

## NBA Player Prediction Model using Neural Networks

This repository contains a neural network model capable of predicting the number of points and assists 
for the NBA player Nikola Jokić. By leveraging historical statistical data and advanced machine learning techniques, 
this model aims to provide insights that can potentially be used to gain an advantage in over/under betting scenarios.

## Table of Contents
* [Installation Guide](#installation-guide)
* [Data Collection and Clean up](#data-Collection-and-Clean-up)
* [Data Intergration](#data-Intergration)
* [Creating, Compiling, Fitting and running Neural Network model](#creating,-Compiling,-Fitting-and-running-Neural-Network-model)
* [Alternate Model](#alternate-Model)
* [Contributors](#contributors)



## Installation Guide

Before Installing the required libraries and 
dependecies to run our project first you must have Pyhton installed on your system
You can download the latest version of Python from the official Python website at python.org. 
Follow the installation instructions specific to your operating system.

`import numpy as np`,

`import pandas as pd`,

`from pathlib import Path`,

`import tensorflow as tf`,

`from tensorflow.keras.layers import Dense`,

`from tensorflow.keras.models import Sequential`,

`from sklearn.model_selection import train_test_split`,

`from sklearn.preprocessing import StandardScaler, OneHotEncoder`

In order to have these imports you must install each library by using

`pip install numpy`,

`pip install pandas`,

`pip install tensorflow`,

`pip install scikit-learn`


## Data Collection and Clean up

The data was collected from reputable sources such as official NBA websites, sports statistics websites, and basketball databases.
We started collecting all of Nikola Jokics full seasons ranging from the 2019 NBA season to the most recent 2023 NBA Season including playoffs.
The collected data encompasses a wide range of performance metrics, including points, rebounds, assists, shooting percentages, and more.


Data Extraction: The collected data was extracted from the original sources and converted into CSV files.

Data Parsing: The extracted data was parsed and converted into a structured format that could be easily manipulated and analyzed. 
This process involved handling missing or incomplete data, converting data types, and resolving any inconsistencies.


The DataFrames were then all saved into one CSV making it our ultimate CSV, we used this bit of code to do so:
`jokic_ultimate.to_csv('jokic_ultimate.csv', index=False)`

The same process was repeated for seasons 2019-2022

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/data1.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/data2.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/data3.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/data4.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/data5.PNG)

## Data Intergration

Intergrate data

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/dataint1.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/dataint2.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/dataint3.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/dataint4.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/dataint5.PNG)


## Creating, Compiling, Fitting and running Neural Network model

split the dataset into training and testing sets using the train_test_split function:


Scale the feature data using StandardScaler:

Define and compile the neural network model:


Train the model using the training data:


Evaluate the model's performance using the testing data:

Once trained and evaluated, you can use the model to make predictions for new data by passing the scaled feature data through the model:

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/model1.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/model2.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/model3.PNG)

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/model4.PNG)



### Points Prediction Results

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/pointsresults1.PNG)

mse: 2.2233

## Alternate Model

The alternate model was created using the same data provided just only focusing on 
the assists portion of the data.

split the dataset into training and testing sets using the train_test_split function:


Scale the feature data using StandardScaler:

Define and compile the neural network model:


Train the model using the training data:


Evaluate the model's performance using the testing data:

Once trained and evaluated, you can use the model to make predictions for new data by passing the scaled feature data through the model:

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/modelA1.PNG)

### Assist Prediction Results

![](https://github.com/reiccv/Project_2_Machine_learning/blob/main/images/assistsresults1.PNG)

mse: 3.9174


## Conclusion


The model's predictions can be interpreted by comparing them with Jokić's actual points per game. 
It is crucial to note that while the model strives for accurate predictions, it is not guaranteed to be 100% accurate. 
Factors such as injuries, team dynamics, and opponent strength may influence Jokić's performance, which the model may not capture fully.





## Contributors

Nahin Hayat, Christian Hernandez, Monica Estrada.