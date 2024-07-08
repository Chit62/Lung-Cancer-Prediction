import pandas as pd
import joblib

df=pd.read_csv('cancer.csv')


df=df.drop('Patient Id',axis =1)
df=df.drop('Passive Smoker',axis=1)
df=df.drop('Obesity',axis=1)
df=df.drop('Balanced Diet',axis=1)


df['Gender'].replace(1, 'female',inplace=True)
df['Gender'].replace(2,'male',inplace=True)


level_mapping = {'Low':1, 'Medium':2, 'High':3}
df.Level = df['Level'].map(level_mapping)


X=df.drop('Level',axis=1)
y=df.Level

from sklearn.preprocessing import LabelEncoder

lo=LabelEncoder()
X['Gender']=lo.fit_transform(X['Gender'])
joblib.dump(lo,('Gender.joblib'))


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
joblib.dump(sc,'scaler.joblib')


from sklearn.model_selection import train_test_split as tts

X_train,X_test,y_train,y_test=tts(X,y,test_size=0.33,random_state=1)


from sklearn.linear_model import LogisticRegression

Model1 = LogisticRegression()
Model1.fit(X_train, y_train)
predictions1 = Model1.predict(X_test)


from sklearn.metrics import classification_report
print(classification_report(y_test,predictions1))

joblib.dump(Model1,'model1.joblib ')


