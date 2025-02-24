import random
import csv
import pandas as pd
import numpy as np
import sklearn
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.metrics import accuracy_score
#f = open('TrainsetTugas4ML.csv','r')
#g = open('TestsetTugas4ML.csv','r')
#train = list(csv.reader(f))
#test = list(csv.reader(g))
##Data_train =[]

##Data_test = pd.read_csv("TestsetTugas4ML.csv")

#def ambil_random(x):
#    Data = x[0]
#    for i in range(100) :
#       Data.append(x[random.randrange(1, 299, 2)])
#    return Data
Data_test = pd.read_csv("TestsetTugas4ML.csv")
Data_train = pd.read_csv("TrainsetTugas4ML.csv")
x_train1 = Data_train.drop(["Class"], axis = 1)
y_train1 = Data_train["Class"]
x_test = Data_test.drop(["Class"], axis = 1)

# fungsi mengambil random data train sejumlah 100
def pd_read():
    filename = "TrainsetTugas4ML.csv"
    n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
    s = 100 #desired sample size
    skip = sorted(random.sample(range(1,n+1),n-s)) #the 0-indexed header will not be included in the skip list
    df = pd.read_csv(filename, skiprows=skip)
    return df
model= []

#melakukan prediksi model selama 5x di simpan di 5 model
for i in range(5):
    x_train = pd_read().drop(["Class"], axis = 1)
    y_train = pd_read()["Class"]
    ModelG = GaussianNB()
    Gtrain = ModelG.fit(x_train,y_train)
    y_pred = Gtrain.predict(x_test)
    model.append(y_pred)
hasil=[]

#melakukan voting untuk hasil 
for i in range(len(Data_test)):
    temp=[]
    for j in range(len(model)):
        temp.append(model[j][i])
    hasil.append(1) if temp.count(1)>=temp.count(2) else hasil.append(2)
# perbandingan hasil akurasi naive bayes seebelum dan sesudah di bagging
Modelnv = GaussianNB()
nvtrain = Modelnv.fit(x_train1,y_train1)
y_pred1 = nvtrain.predict(x_test)
print("data prediksi naive bayes: ",y_pred1)
print("score naive bayes: ",nvtrain.score(x_train,y_train))
print("data prediksi naive bayes dengan bagging: ",hasil)
print("score naive bayes dengan bagging: ",nvtrain.score(x_test,hasil))
with open("TebakanTugas4ML.csv",'w') as f:
    writer = csv.writer(f)
    for i in hasil:
        f.write(str(i)+"\n")