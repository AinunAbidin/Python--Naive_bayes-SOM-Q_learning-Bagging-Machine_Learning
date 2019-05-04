import csv
import numpy as np
import random

data = []
with open('DataTugas3ML2019.txt','r') as f:
    for row in csv.reader(f,delimiter='\t'):
        data.append(row)

atas = list()
bawah = list()
kiri = list()
kanan = list()

#deklarasi tabel R
for i in range(15):
    for j in range(15):
        if (i==0):
            atas.append(0)
        else:
            atas.append(data[i-1][j])

for i in range(15):
    for j in range(15):
        if (i==14):
            bawah.append(0)
        else:
            bawah.append(data[i+1][j])

for i in range(15):
    for j in range(15):
        if (j==0):
            kiri.append(0)
        else:
            kiri.append(data[i][j-1])

for i in range(15):
    for j in range(15):
        if (j==14):
            kanan.append(0)
        else:
            kanan.append(data[i][j+1])

R= np.array([atas,kanan,kiri,bawah])
#membuat tabel Q
Q = np.matrix(np.zeros([15,15]))
#deklarasi varibel gamma untuk menghitung nilang di tabel Q
gamma = 0.8

#fungsi hitung Q
def hitungQ(n,Q_tab):
    P=[]
    for i in range (len(Q_tab)):
        if (Q_tab[i][2] == "atas"):
            P.append(int(Q[0, (((Q_tab[i][0] * 10)-10) + Q_tab[i][1] + 1)]))
        elif (Q_tab[i][2] == "bawah"):
            P.append(int(Q[1, (((Q_tab[i][0] * 10)-10) + Q_tab[i][1] + 1)]))
        elif (Q_tab[i][2] == "kiri"):
            P.append(int(Q[2, (((Q_tab[i][0] * 10)-10) + Q_tab[i][1] + 1)]))
        elif (Q_tab[i][2] == "kanan"):
            P.append(int(Q[3, (((Q_tab[i][0] * 10)-10) + Q_tab[i][1] + 1)]))
    H = float(n) + ( gamma * max(P) )
    return H
 #fungsi ambil aksi
def getR(action):
    position = []
    if (action[2] == "atas"):
        position = [0, ((action[0]*10)-10)+(action[1]+1)]
    elif (action[2] == "bawah"):
        position = [1, ((action[0]*10)-10)+(action[1]+1)]
    elif (action[2] == "kiri"):
        position = [2, ((action[0]*10)-10)+(action[1]+1)]
    elif (action[2] == "kanan"):
        position = [3, ((action[0]*10)-10)+(action[1]+1)]

    return position
#fungsi ubah R 
def gantiR(q):
    if (action[2] == "atas"):
        R[0, ((action[0]*10)-10)+(action[1]+1)] = q
    elif (action[2] == "bawah"):
        R[1, ((action[0]*10)-10)+(action[1]+1)] = q
    elif (action[2] == "kiri"):
        R[2, ((action[0]*10)-10)+(action[1]+1)] = q
    elif (action[2] == "kanan"):
        R[3, ((action[0]*10)-10)+(action[1]+1)] = q
#fungsi Ubah Q
def gantiQ(q):
    if (action[2] == "atas"):
        Q[0, ((action[0]*10)-10)+(action[1]+1)] = q
    elif (action[2] == "bawah"):
        Q[1, ((action[0]*10)-10)+(action[1]+1)] = q
    elif (action[2] == "kiri"):
        Q[2, ((action[0]*10)-10)+(action[1]+1)] = q
    elif (action[2] == "kanan"):
        Q[3, ((action[0]*10)-10)+(action[1]+1)] = q

#fungsi cari jalan 
def carijalan(x,y):
    choice = []
    if (x == 0):
        if (y == 0):
            choice.append([x+1, y, "bawah"])
            choice.append([x, y+1, "kanan"])
        elif (y == 14):
            choice.append([x, y-1, "kiri"])
            choice.append([x+1, y, "bawah"])
        else:
            choice.append([x + 1, y, "bawah"])
            choice.append([x, y - 1, "kiri"])
            choice.append([x, y + 1, "kanan"])
    elif (x == 14):
        if (y == 0):
            choice.append([x-1, y, "atas"])
            choice.append([x, y+1, "kanan"])
        elif (y == 14):
            choice.append([x-1, y, "atas"])
            choice.append([x, y-1, "kiri"])
        else:
            choice.append([x - 1, y, "atas"])
            choice.append([x, y - 1, "kiri"])
            choice.append([x, y+1, "kanan"])
    elif(y == 0):
        if (x != 0 and x != 14):
            choice.append([x - 1, y, "atas"])
            choice.append([x, y + 1, "kanan"])
            choice.append([x + 1, y, "bawah"])
    elif(y == 14):
        if (x != 0 and x != 14):
            choice.append([x - 1, y, "atas"])
            choice.append([x, y - 1, "kiri"])
            choice.append([x + 1, y, "bawah"])
    else:
        choice.append([x - 1, y, "atas"])
        choice.append([x, y + 1, "kanan"])
        choice.append([x, y - 1, "kiri"])
        choice.append([x + 1, y, "bawah"])

    return choice

#fungsi cek jalan 
def cekjalan(x,y):
    nextPath = []
    if (x == 0):
        if (y == 0):
            if (Q[x+1, y] >= Q[x, y+1]):
                nextPath = Q[x+1, y]
            else:
                nextPath = Q[x, y + 1]
        elif (y == 14):
            if (Q[x, y-1] >= Q[x+1, y]):
                nextPath = Q[x, y-1]
            else:
                nextPath = Q[x+1, y]
        else:
            if (Q[x + 1, y] >= Q[x, y - 1] and Q[x + 1, y] >= Q[x, y + 1]):
                nextPath = Q[x + 1, y]
            elif (Q[x, y - 1] >= Q[x + 1, y] and Q[x, y - 1] >= Q[x, y + 1]):
                nextPath = Q[x+1, y]
            elif (Q[x, y + 1] >= Q[x + 1, y] and Q[x, y + 1] >= Q[x, y - 1]):
                nextPath = Q[x+1, y]

    elif (x == 14):
        if (y == 0):
            if (Q[x-1, y] >= Q[x, y+1]):
                nextPath = Q[x-1, y]
            else:
                nextPath = Q[x, y + 1]
        elif (y == 14):
            if (Q[x-1, y] >= Q[x, y+1]):
                nextPath = Q[x-1, y]
            else:
                nextPath = Q[x, y-1]
        else:
            if (Q[x - 1, y] >= Q[x, y - 1] and Q[x - 1, y] >= Q[x, y+1]):
                nextPath = Q[x - 1, y]
            elif (Q[x, y - 1] >= Q[x - 1, y] and Q[x, y - 1] >= Q[x, y+1]):
                nextPath = Q[x, y - 1]
            elif (Q[x, y+1] >= Q[x - 1, y] and Q[x, y+1] >= Q[x, y - 1]):
                nextPath = Q[x, y+1]
    elif(y == 0):
        if (x != 0 and x != 14):
            if (Q[x - 1, y] >= Q[x, y + 1] and Q[x - 1, y] >= Q[x + 1, y]):
                nextPath = Q[x - 1, y]
            elif (Q[x, y + 1] >= Q[x - 1, y] and Q[x, y + 1] >= Q[x + 1, y]):
                nextPath = Q[x, y + 1]
            elif (Q[x + 1, y] >= Q[x - 1, y] and Q[x + 1, y] >= Q[x, y + 1]):
                nextPath = Q[x + 1, y]

    elif(y == 14):
        if (x != 0 and x != 14):
            if (Q[x - 1, y] >= Q[x, y - 1] and Q[x - 1, y] >= Q[x + 1, y]):
                nextPath = Q[x - 1, y]
            elif (Q[x, y - 1] >= Q[x - 1, y] and Q[x, y - 1] >= Q[x + 1, y]):
                nextPath = Q[x, y - 1]
            elif (Q[x + 1, y] >= Q[x - 1, y] and Q[x + 1, y] >= Q[x, y - 1]):
                nextPath = Q[x + 1, y]
    else:
        if (Q[x - 1, y] >= Q[x, y - 1] and Q[x - 1, y] >= Q[x, y + 1] and Q[x - 1, y] >= Q[x + 1, y]):
            nextPath = Q[x - 1, y]
        elif (Q[x, y - 1] >= Q[x - 1, y] and Q[x, y - 1] >= Q[x, y + 1] and Q[x, y - 1] >= Q[x + 1, y]):
            nextPath = Q[x, y - 1]
        elif (Q[x, y + 1] >= Q[x - 1, y] and Q[x, y + 1] >= Q[x, y - 1] and Q[x, y + 1] >= Q[x + 1, y]):
            nextPath = Q[x, y + 1]
        elif (Q[x + 1, y] >= Q[x - 1, y] and Q[x + 1, y] >= Q[x, y + 1] and Q[x + 1, y] >= Q[x, y - 1]):
            nextPath = Q[x, y + 1]

    return nextPath

def learn(x, y):
    Learn = []
    if (x == 0):
        if (y == 0):
            if (Q[1, (((x+1)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)]):
                Learn = (Q[1, (((x+1)*10)-10)+(y+1)])
            else:
                Learn = (Q[3, ((x*10)-10)+(y+2)])

        elif (y == 14):
            if (Q[2, (((x)*10)-10)+(y)] >= Q[1, (((x+1)*10)-10)+(y+1)]):
                Learn = (Q[2, (((x)*10)-10)+(y)])
            else:
                Learn = (Q[1, ((x*10)-10)+(y+1)])

        else:
            if (Q[1, (((x+1)*10)-10)+(y+1)] >= Q[2, ((x*10)-10)+(y)] and Q[1, (((x+1)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)]):
                Learn = (Q[1, (((x+1)*10)-10)+(y+1)])
            elif(Q[2, ((x*10)-10)+(y)] >= Q[1, (((x+1)*10)-10)+(y+1)] and Q[2, ((x*10)-10)+(y)] >= Q[3, ((x*10)-10)+(y+2)]):
                Learn = (Q[2, ((x*10)-10)+(y)])
            elif (Q[3, ((x*10)-10)+(y+2)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[3, ((x*10)-10)+(y+2)] >= Q[2, ((x*10)-10)+(y)]):
                Learn = (Q[3, ((x * 10) - 10) + (y + 1)])

    elif (x == 14):
        if (y == 0):
            if (Q[0, (((x)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)]):
                Learn = (Q[0, (((x)*10)-10)+(y+1)])
            else:
                Learn = (Q[3, ((x * 10) - 10) + (y + 2)])

        elif (y == 14):
            if (Q[0, (((x)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)]):
                Learn = (Q[0, (((x)*10)-10)+(y+1)])
            elif (Q[2, ((x * 10) - 10) + (y)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[2, ((x * 10) - 10) + (y)] >= Q[3, ((x * 10) - 10) + (y + 2)]):
                Learn = (Q[2, ((x * 10) - 10) + (y)])

        else:
            if (Q[0, (((x)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)] and Q[0, (((x)*10)-10)+(y+1)] >= Q[2, ((x * 10) - 10) + (y)]):
                Learn = (Q[0, (((x)*10)-10)+(y+1)])
            elif (Q[2, ((x * 10) - 10) + (y)] >= Q[0, (((x)*10)-10)+(y+1)] and Q[2, ((x * 10) - 10) + (y)] >= Q[3, ((x * 10) - 10) + (y + 2)]):
                Learn = (Q[2, ((x * 10) - 10) + (y)])
            elif (Q[3, ((x * 10) - 10) + (y + 2)] >= Q[0, (((x)*10)-10)+(y+1)] and Q[3, ((x * 10) - 10) + (y + 2)] >= Q[2, ((x * 10) - 10) + (y)]):
                Learn = (Q[3, ((x * 10) - 10) + (y + 1)])

    elif(y == 0):
        if (x != 0 and x != 14):
            if (Q[0, (((x)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)] and Q[0, (((x)*10)-10)+(y+1)] >= Q[1, (((x+1)*10)-10)+(y+1)]):
                Learn = (Q[0, (((x)*10)-10)+(y+1)])
            elif (Q[3, ((x * 10) - 10) + (y + 2)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[3, ((x * 10) - 10) + (y + 2)] >= Q[0, (((x)*10)-10)+(y+1)]):
                Learn = (Q[3, ((x * 10) - 10) + (y + 1)])
            elif (Q[1, (((x+1)*10)-10)+(y+1)] >= Q[3, ((x*10)-10)+(y+2)] and Q[1, (((x+1)*10)-10)+(y+1)] >= Q[0, (((x)*10)-10)+(y+1)]):
                Learn = (Q[1, (((x+1)*10)-10)+(y+1)])

    elif(y == 14):
        if (x != 0 and x != 14):
            if (Q[0, (((x)*10)-10)+(y+1)] >= Q[2, ((x * 10) - 10) + (y)] and Q[0, (((x)*10)-10)+(y+1)] >= Q[1, (((x+1)*10)-10)+(y+1)]):
                Learn = (Q[0, (((x)*10)-10)+(y+1)])
            elif (Q[2, ((x * 10) - 10) + (y)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[2, ((x * 10) - 10) + (y)] >= Q[0, (((x)*10)-10)+(y+1)]):
                Learn = (Q[2, ((x * 10) - 10) + (y)])
            elif (Q[1, (((x+1)*10)-10)+(y+1)] >= Q[0, (((x)*10)-10)+(y+1)] and Q[1, (((x+1)*10)-10)+(y+1)] >= Q[2, ((x * 10) - 10) + (y)]):
                Learn = (Q[1, (((x+1)*10)-10)+(y+1)])

    else:
        if (Q[0, (((x) * 10) - 10) + (y + 1)] >= Q[2, ((x * 10) - 10) + (y)] and Q[0, (((x) * 10) - 10) + (y + 1)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[0, (((x) * 10) - 10) + (y + 1)] >= Q[3, ((x * 10) - 10) + (y + 1)]):
            Learn = (Q[0, (((x) * 10) - 10) + (y + 1)])
        elif (Q[2, ((x * 10) - 10) + (y)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[2, ((x * 10) - 10) + (y)] >= Q[0, (((x) * 10) - 10) + (y + 1)] and Q[2, ((x * 10) - 10) + (y)] >= Q[3, ((x * 10) - 10) + (y + 1)]):
            Learn = (Q[2, ((x * 10) - 10) + (y)])
        elif (Q[1, (((x + 1) * 10) - 10) + (y + 1)] >= Q[0, (((x) * 10) - 10) + (y + 1)] and Q[1, (((x + 1) * 10) - 10) + (y + 1)] >= Q[2, ((x * 10) - 10) + (y)] and Q[1, (((x + 1) * 10) - 10) + (y + 1)] >= Q[3, ((x * 10) - 10) + (y + 1)]):
            Learn = (Q[1, (((x + 1) * 10) - 10) + (y + 1)])
        elif (Q[3, ((x * 10) - 10) + (y + 2)] >= Q[1, (((x + 1) * 10) - 10) + (y + 1)] and Q[3, ((x * 10) - 10) + (y + 2)] >= Q[0, (((x) * 10) - 10) + (y + 1)] and Q[3, ((x * 10) - 10) + (y + 2)] >= Q[2, ((x * 10) - 10) + (y)]):
            Learn = (Q[3, ((x * 10) - 10) + (y + 1)])

    return Learn
arrayReward = []
for i in range(500):
    CurrentState = -2
    x = 14
    y = 0
    reward = []
    print("Espisode")
    while(CurrentState != 500):
        choices = carijalan(x,y)
        print(choices)
        action = random.choice(choices)
        print(action)
        r = getR(action)
        rx = r[0]
        ry = r[1]
        # print(rx, ry)
        q = hitungQ(R[rx][ry], choices)
        # updateR(q)
        gantiQ(q)
        x = action[0]
        y = action[1]
        # print(x, y)

        CurrentState = data[x][y]
        reward.append(CurrentState)
        print(CurrentState)
        if (CurrentState == 500):
            print("Goal State")
            print("Reward\t: ", np.sum(reward))
            arrayReward.append(np.sum(reward))