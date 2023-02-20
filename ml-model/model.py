from sklearn import linear_model
import pandas as pd
import pickle

df = pd.read_csv('prices.csv')

y = df['Value'] #Dependent variable
X = df[['Rooms', 'Distance']] #Independent variable

lm = linear_model.LinearRegression()
lm.fit(X, y)

pickle.dump(lm, open('model.pkl', 'wb'))

print(lm.predict([[15,61]]))
print(f'score: {lm.score(X, y)}')