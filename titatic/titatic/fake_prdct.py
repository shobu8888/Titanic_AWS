def fk_pred (Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title):
    import pickle
    x = [[Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title]]
    randomforest = pickle.load(open('titanic_rf.sav','rb'))
    pridiction = randomforest.predict(x)
    return pridiction
