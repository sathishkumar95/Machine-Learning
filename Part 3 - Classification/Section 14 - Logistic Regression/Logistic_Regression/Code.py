#importing libraries

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importing dataset

dataset = pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:,2:4].values
y = dataset.iloc[:,4].values

#splitting training and test set

from sklearn.cross_validation import train_test_split as tts

X_train, X_test, y_train, y_test = tts(X,y,test_size=0.25,random_state=0)

#feature scaling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#Training the classifier

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
