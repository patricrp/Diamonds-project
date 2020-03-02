import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, AdaBoostRegressor, BaggingRegressor
from sklearn.metrics import *
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

def algoModel(di, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    for k,v in di.items():
        score = v.score(X_test,y_test)
        rmse = np.sqrt(mean_squared_error(y_test, v.predict(X_test)))
        y_pred = v.predict(X_test)
        
        print(k)
        print('Score is ', score)
        print('RMSE is ', rmse)
        sns.scatterplot(y_pred, y_test)
        plt.xlabel("Predicted price")
        plt.ylabel("Real price")
        plt.show()