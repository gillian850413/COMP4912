# COMP4912
This is a pokemon combat data analysis project.
Techniques: Python, Scikit-Learn, Pandas, Numpy, Matplotlib, Clustering, Random Forest

## Table of Contents
1. Base Stat Analysis
   - Data Cleaning
   - Principal Component Analysis
      - Preprocessing Data
      - Perfrom PCA
      - Data Visualization
2. Clustering
   - Mean Shift Clustering
   - Outlier Analysis
      - Analyze Cluster 2
      - Analyze Cluster 3
   - Kmeans
3. Data Training 1
   - Data Preprocessing
      - Preprocess Base Stats
      - Preprocess Clustering Result
   - Data Training only with Base Stats
      - Training Set : Testing Set = 0.75 : 0.25
      - Training Set : Testing Set = 0.5 : 0.5
      - Training Set : Testing Set = 0.25 : 0.75
   - Data Training only with Kmeans Clustering Result
   - Data Training with Base Stats and Kmeans Clustering Result
4. Type / First Attack Analysis
   - Type Advantage
   - First Attack Advantage
   - First Attacker and Type Advantage
5. Data Training 2
   - Data Preprocessing
   - Data Training with Type Effectiveness
      - Training Set : Testing Set = 0.75 : 0.25
      - Random Forest Feature Importance
      - Training Set : Testing Set = 0.5 : 0.5
      - Training Set : Testing Set = 0.25 : 0.75
      - Decision Tree Feature Importance
6. Pokemon Combat Prediction
   - Random Forest Classification
      - Parameter Tuning
      - Random Forest
   - Data Visualization
   - Predict tests.csv With Random Forest
