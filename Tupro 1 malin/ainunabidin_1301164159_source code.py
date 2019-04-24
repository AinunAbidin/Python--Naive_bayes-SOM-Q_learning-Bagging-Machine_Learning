import csv
import math
import random
f = open('TrainsetTugas1ML.csv','r')
g = open('TestsetTugas1ML.csv','r')
train = list(csv.reader(f))
test = list(csv.reader(g))

# fungsi perhitungan probabilitas dari masing-masing label atau kelas
def probkelas():
    terima,tidak = 0,0
    for i in train:
        if (i[8] == ">50K"):
            terima += 1
        else:
            tidak +=1
    proby = terima/(terima+tidak)
    probt = tidak/(terima+tidak)
    return terima,tidak,proby,probt

#fungsi untuk mencari probilitas dari nilai proby
def hitungprobterima(x1,x2,x3,x4,x5,x6,x7,terima,proby):
    age,workclass,education,marital,occupation,relationship,hoursperweek=0,0,0,0,0,0,0
    for i in train:
        if (x1==i[1]) and (i[8]==">50K"):
            age +=1
    for i in train:
        if (x2==i[2]) and (i[8]==">50K"):
            workclass +=1
    for i in train:
        if (x3==i[3]) and (i[8]==">50K"):
            education +=1
    for i in train:
        if (x4==i[4]) and (i[8]==">50K"):
            marital +=1
    for i in train:
        if (x5==i[5]) and (i[8]==">50K"):
            occupation +=1
    for i in train:
        if (x6==i[6]) and (i[8]==">50K"):
            relationship +=1
    for i in train:
        if (x7==i[7]) and (i[8]==">50K"):
            hoursperweek +=1 
    return ((age/terima) * (workclass/terima) * (education/terima) * (marital/terima) * (occupation/terima) * (relationship/terima) * (hoursperweek/terima) * proby)

#fungsi untuk mencari probilitas dari nilai probt
def hitungprobtolak(x1,x2,x3,x4,x5,x6,x7,tidak,probt):
    age,workclass,education,marital,occupation,relationship,hoursperweek=0,0,0,0,0,0,0 
    for i in train:
        if (x1==i[1]) and (i[8]=="<=50K"):
            age +=1
    for i in train:
        if (x2==i[2]) and (i[8]=="<=50K"):
            workclass +=1
    for i in train:
        if (x3==i[3]) and (i[8]=="<=50K"):
            education +=1
    for i in train:
        if (x4==i[4]) and (i[8]=="<=50K"):
            marital +=1
    for i in train:
        if (x5==i[5]) and (i[8]=="<=50K"):
            occupation +=1
    for i in train:
        if (x6==i[6]) and (i[8]=="<=50K"):
            relationship +=1
    for i in train:
        if (x7==i[7]) and (i[8]=="<=50K"):
            hoursperweek +=1
    return ((age/tidak) * (workclass/tidak) * (education/tidak) * (marital/tidak) * (occupation/tidak) * (relationship/tidak) * (hoursperweek/tidak) * probt)



arrhasil = []
terima,tidak,proby,probt = probkelas()
print(terima,tidak,proby,probt)
tb =0
for i in test:
    probterima = hitungprobterima(i[1],i[2],i[3],i[4],i[5],i[6],i[7],terima,proby)
    probtolak = hitungprobtolak(i[1],i[2],i[3],i[4],i[5],i[6],i[7],tidak,probt)
    if ( probterima > probtolak):
        arrhasil.append(">50K")
        tb += 1
    elif (probterima < probtolak) :
        arrhasil.append("<=50K")
        tb += 1
akurasi = tb/float(len(test))*100.0
arrhasil.append('Accuracy: {0}%'.format(akurasi))
with open("TebakanTugas1ML.csv",'w') as f:
    writer = csv.writer(f)
    for i in arrhasil:
        f.write(i+"\n")



    
    
    

