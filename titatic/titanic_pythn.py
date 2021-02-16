#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df_pd = pd.read_csv('train.csv')
df_pd["Age"].fillna(df_pd["Age"].median(), inplace = True)
df_pd["Embarked"].fillna("S", inplace=True)
del df_pd["Cabin"]


def title_name(name):
    if '.' in name :
        return name.split(",")[1].split(".")[0].strip()
    else:
        return "Tille missing" 

def shorter_title(x):
    title = x["Title"]
    if title in ('Major', 'Col', 'Capt'):
        title = 'Officer'
    elif title in ('Rev','Jonkheer', 'Sir', 'Lady', 'the Countess', 'Don','Master') :
        title = 'Royal'
    return title

df_pd["Title"] = df_pd.Name.map(lambda x:title_name(x))
df_pd["Title"] = df_pd.apply(shorter_title , axis = 1)



df_pd.drop("Name" , axis = 1 , inplace = True)
df_pd.drop("Ticket" , axis = 1 , inplace = True)

df_pd.Sex.replace(('male','female'), (0,1), inplace= True)
df_pd.Embarked.replace(('S','C', 'Q'), (0,1,2), inplace= True)

df_pd.Title.replace(('Mr','Miss', 'Mrs','Royal','Dr', 'Officer','Mlle','Ms', 'Mme'), (0,1,2,3,4,5,6,7,8), inplace= True)
df_pd.Title.replace(('Dona'), (9), inplace= True)



y = df_pd["Survived"]
x = df_pd.drop(["Survived" , "PassengerId" ],axis = 1)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.1)


randomforest = RandomForestClassifier()
randomforest.fit (x_train,y_train)
pickle.dump(randomforest , open('titanic_rf.sav' , 'wb'))


# In[ ]:




