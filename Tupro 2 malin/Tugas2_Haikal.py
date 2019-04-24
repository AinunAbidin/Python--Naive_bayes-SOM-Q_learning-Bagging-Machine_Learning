import csv
import math
import random
import matplotlib.pyplot as curv
f = open("Tugas 2 ML.csv","r")
data3 = list(csv.reader(f))
data = []
for d in data3:
    data.append((float(d[0]),float(d[1])))
n= []
n.append([random.uniform(-1, 25), random.uniform(-1, 25)])
n.append([random.uniform(-1, 25), random.uniform(-1, 25)])
n.append([random.uniform(-1, 25), random.uniform(-1, 25)])
n.append([random.uniform(-1, 25), random.uniform(-1, 25)])
#fungsi menghitung euclidian
def hitung_ecludian(x,y):
    hhe = math.sqrt(((x[0]-y[0])**2) + ((x[1]-y[1])**2))
    return hhe

#fungsi untuk menghitung sn
def hitung_SN(x,y):
    hasilsn = math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
    return hasilsn

#fungsi menghitung TN
def hitung_TN(x):
    hasilTN =[]
    for i in range(3):
        hasilTN.append(math.exp((-x[i])/(2*(sigma**2))))
    return hasilTN

def takeSecond1(elem):
    return elem[0]

#fungsi hitung wn
def hitung_wn(x,y):
    haswn = []
    for i in range(3):
        temp = []
        for j in range(2):
            temp.append(str(lr*y[j]*(x[j] - n[nbr[i]][j])))
        haswn.append((temp[0], temp[1]))
    return haswn

#fungsi ubah W 
def ubahnilai_W(x):
    
    for i in range(len(x)):
        y = []
        for j in range(2):
            n[nbr[i]][j] = n[nbr[i]][j] + float(x[i][j][:3])
    return y

sigma0 = 2
t0 = 2
lr0 = 0.1
tn = 2
sigma, lr = 0, 0
sn=[]
TN = []
hasil =[]
hasil_akhir =[]
jarak = []
# MAIN PROGRAM
for q in range(5):
    sigma = sigma0 * math.exp(-(q+1)/t0)
    lr = lr0 * math.exp(-(q+1)/tn)
    for j in range(len(data)):
        nbr=[]
        # Perulangan untuk setiap neuron dan mencari jarak terdekat untuk data tersebut
        for i in range(len(n)):
            jarak.append([hitung_ecludian(data[j], n[i]), i])
        jarak.sort(key=takeSecond1)

        for i in range(len(n)):
            nbr.append(jarak[i][1])

        for i in range(3):
            sn.append(hitung_SN(n[nbr[0]], n[nbr[i]]))
        
        TN = hitung_TN(sn)

        hasil=hitung_wn(data[j],TN)
        hasil_akhir = ubahnilai_W(hasil)

print(n)
for j in range(len(data)):
    for i in range (len(n)):
        jarak.append((hitung_ecludian(data[j],n[i]),i))
    jarak.sort(key=takeSecond1)
    
    if jarak[0][1] == 0:
        curv.scatter(data[j][0], data[j][1], c ='red', alpha=1)
    elif jarak[0][1] == 1:
        curv.scatter(data[j][0],data[j][1], c ='a', alpha=1) 
    elif jarak[0][1] == 2:
        curv.scatter(data[j][0],data[j][1], c ='b', alpha=1)
    elif jarak[0][1] == 3:
        curv.scatter(data[j][0],data[j][1], c ='c', alpha=1)


curv.scatter(n[0][0], n[0][1], marker = 'x', label = 0, c='red', alpha=1)
curv.scatter(n[1][0], n[1][1], marker = '^', c='a', alpha=1)
curv.scatter(n[2][0], n[2][1], marker = '*', c='b', alpha=1)
curv.scatter(n[3][0], n[3][1], marker = 's', c='c', alpha=1)
curv.title('Hasil SOM')
curv.show()