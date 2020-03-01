# Diamonds-project

Create different machine learning models to study Machine Learning Supervised Regression.

1. Explore the dataset to know which columns are in, which types of data, nulls, duplicates, unique values for categorical and correlated.

* Cut, color and clarity are object series.
* There is no null
* There is no duplicated
* Create a correlation matrix and plot it to see which series are correlated


2. Before dropping any column, I select RandomForest Regression to train the model with all series. Finally, I drop series id, x, y and z to train again Random Forest Regression.

3. Training the model with different estimators, max and min depth. Minimum RMSE was with 86 estimators, 21 max depth and 3 min depth.

4. Including Normalized and StandardScaler to train again RandomForest. Something was wrong. Score was up to 5455 :(. I need to inverse the DataFrame but 

