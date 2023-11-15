import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR


class ml:
    def runQuery(self,x):
        df=pd.read_csv('water_potability.csv')
        df = df[(df["ph"] > 4.0) & (df["ph"] < 6.5)]
        df.reset_index(drop=True, inplace=True)
        df.index += 1
        # plt.figure(figsize=(20, 4))     
        # x_ = [i for i in range(1, 337)]
        # y = df['ph']
        # plt.scatter(x_, y)
        # plt.xlabel('X-axis Label')
        # plt.ylabel('Y-axis Label')
        # plt.title('Scatter Plot of pH')
        forecast_col = 'ph'
        forecast_out = int(np.ceil(0.01 * len(df)))
        df['label'] = df[forecast_col].shift(-forecast_out)

        df.dropna(inplace=True)
        X = df[['ph']].values
        y = df['label'].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

        clf = SVR(kernel='poly')
        clf.fit(X_train, y_train)


        X_lately = X[-x:]
        forecast_set = clf.predict(X_lately)
        return forecast_set[x-1]