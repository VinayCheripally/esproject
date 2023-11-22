import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


class ml:
    def runQuery(self,x,y):
        if(y==1):
            df = pd.read_csv