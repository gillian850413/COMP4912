# COMP4912
This is a pokemon combat data analysis project. 


Table of Contents
1  Base Stat Analysis
  1.1  Data Cleaning
  1.2  Principal Component Analysis
    1.2.1  Preprocessing Data
    1.2.2  Perfrom PCA
    1.2.3  Data Visualization
2  Clustering
2.1  Mean Shift Clustering
2.1.1  Outlier Analysis
2.1.1.1  Analyze Cluster 2
2.1.1.2  Analyze Cluster 3
2.2  Kmeans
3  Data Training 1
3.1  Data Preprocessing
3.1.1  Preprocess Base Stats
3.1.2  Preprocess Clustering Result
3.2  Data Training only with Base Stats
3.2.1  Training Set : Testing Set = 0.75 : 0.25
3.2.2  Training Set : Testing Set = 0.5 : 0.5
3.2.3  Training Set : Testing Set = 0.25 : 0.75
3.3  Data Training only with Kmeans Clustering Result
3.4  Data Training with Base Stats and Kmeans Clustering Result
4  Type / First Attack Analysis
4.1  Type Advantage
4.2  First Attack Advantage
4.3  First Attacker and Type Advantage
5  Data Training 2
5.1  Data Preprocessing
5.2  Data Training with Type Effectiveness
5.2.1  Training Set : Testing Set = 0.75 : 0.25
5.2.2  Random Forest Feature Importance
5.2.3  Training Set : Testing Set = 0.5 : 0.5
5.2.4  Training Set : Testing Set = 0.25 : 0.75
5.2.5  Decision Tree Feature Importance
6  Pokemon Combat Prediction
6.1  Random Forest Classification
6.1.1  Parameter Tuning
6.1.2  Random Forest
6.2  Data Visualization
6.3  Predict tests.csv With Random Forest
