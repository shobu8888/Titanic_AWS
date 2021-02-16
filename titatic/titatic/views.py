from django.shortcuts import render
from . import fake_prdct

def home(request):
    return render(request , 'index.html')

def result(request):
    Pclass = int(request.GET['Pclass'])
    Sex = int(request.GET['Sex'])
    Age = int(request.GET['Age'])
    SibSp = int(request.GET['SibSp'])
    Parch = int(request.GET['Parch'])
    Fare = int(request.GET['Fare'])
    Embarked = int(request.GET['Embarked'])
    Title = int(request.GET['Title'])
    prd = fake_prdct.fk_pred(Pclass,Sex,Age,SibSp,Parch,Fare,Embarked,Title)
    print (prd)
    return render(request , 'result.html', {"User_input" : prd})
