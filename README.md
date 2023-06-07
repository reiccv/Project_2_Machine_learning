# Project 2 Machine learning

## NBA Player Peformance Predictor Bot


## Table of Contents
* [Installation Guide](##installation-guide)
* [Data Collection and Clean up](##data-Collection-and-Clean-up)




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


The DataFrames were then all saved into one CSV making it our ultimate CSV, we used this bit of code to do so:
`jokic_ultimate.to_csv('jokic_ultimate.csv', index=False)`

