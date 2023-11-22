import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler


class ml:
    def runQuery(self,x,y):
        if(y==1):
            df = pd.read_csv("dis1.csv")
        elif y==2:
            df = pd.read_csv("dis2.csv")
        elif y==3:
            df = pd.read_csv("dis3.csv")
        else:
            df = pd.read_csv("dis4.csv")
        forecast_col = 'pH'
        forecast_out = 12


        df['label'] = df[forecast_col].shift(-forecast_out)
        df.dropna(inplace=True)
        X = df[['pH']].values
        y = df['label'].values
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)

        clf = LinearRegression()
        clf.fit(X_train, y_train)

        X_lately = X_scaled[-forecast_out:]
        forecast_set = clf.predict(X_lately)
        print(f"Forecasted pH value at index 3: {forecast_set[3]}")