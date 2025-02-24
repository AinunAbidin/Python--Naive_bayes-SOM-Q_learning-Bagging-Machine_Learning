import numpy as np
import random

gamma =0.8
data = np.loadtxt('DataTugas3ML2019.txt', usecols=range(15)).astype(int)
#deklarasi Tabel R
atas = list()
bawah = list()
kiri = list()
kanan = list()
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

R = np.array([atas, kanan, kiri, bawah])
Q = np.zeros_like(R)
for i in range(len(R)):
    for j in range(len(R[0])):
        Q[i][j] = 0
def FungsiR(action):
    if (action[2] == "up"):
        position = [0, ((action[0]*15)-15)+(action[1]+1)]
    elif (action[2] == "down"):
        position = [1, ((action[0]*15)-15)+(action[1]+1)]
    elif (action[2] == "left"):
        position = [2, ((action[0]*15)-15)+(action[1]+1)]
    elif (action[2] == "right"):
        position = [3, ((action[0]*15)-15)+(action[1]+1)]

    return position

def GantiR(q):
    if (action[2] == "up"):
        R[0, ((action[0]*15)-15)+(action[1]+1)] = q
    elif (action[2] == "down"):
        R[1, ((action[0]*15)-15)+(action[1]+1)] = q
    elif (action[2] == "left"):
        R[2, ((action[0]*15)-15)+(action[1]+1)] = q
    elif (action[2] == "right"):
        R[3, ((action[0]*15)-15)+(action[1]+1)] = q

def GantiQ(q):
    if (action[2] == "up"):
        Q[0, ((action[0]*15)-15)+(action[1]+1)] = q
    elif (action[2] == "down"):
        Q[1, ((action[0]*15)-15)+(action[1]+1)] = q
    elif (action[2] == "left"):
        Q[2, ((action[0]*15)-15)+(action[1]+1)] = q
    elif (action[2] == "right"):
        Q[3, ((action[0]*15)-15)+(action[1]+1)] = q


def HitungQ(r, Q_table):
    poin = []
    for i in range(len(Q_table)):
        if (Q_table[i][2] == "up"):
            poin.append(int(Q[0, (((Q_table[i][0] * 15)-15) + Q_table[i][1] + 1)]))
        elif (Q_table[i][2] == "down"):
            poin.append(int(Q[1, (((Q_table[i][0] * 15)-15) + Q_table[i][1] + 1)]))
        elif (Q_table[i][2] == "left"):
            poin.append(int(Q[2, (((Q_table[i][0] * 15)-15) + Q_table[i][1] + 1)]))
        elif (Q_table[i][2] == "right"):
            poin.append(int(Q[3, (((Q_table[i][0] * 15)-15) + Q_table[i][1] + 1)]))
    result = float(r) + (gamma * max(poin))
    return result

def carijalan(x, y):
    choice = []
    if (x == 0):
        if (y == 0):
            choice.append([x+1, y, "down"])
            choice.append([x, y+1, "right"])
        elif (y == 14):
            choice.append([x, y-1, "left"])
            choice.append([x+1, y, "down"])
        else:
            choice.append([x + 1, y, "down"])
            choice.append([x, y - 1, "left"])
            choice.append([x, y + 1, "right"])
    elif (x == 14):
        if (y == 0):
            choice.append([x-1, y, "up"])
            choice.append([x, y+1, "right"])
        elif (y == 14):
            choice.append([x-1, y, "up"])
            choice.append([x, y-1, "left"])
        else:
            choice.append([x - 1, y, "up"])
            choice.append([x, y - 1, "left"])
            choice.append([x, y+1, "right"])
    elif(y == 0):
        if (x != 0 and x != 14):
            choice.append([x - 1, y, "up"])
            choice.append([x, y + 1, "right"])
            choice.append([x + 1, y, "down"])
    elif(y == 14):
        if (x != 0 and x != 14):
            choice.append([x - 1, y, "up"])
            choice.append([x, y - 1, "left"])
            choice.append([x + 1, y, "down"])
    else:
        choice.append([x - 1, y, "up"])
        choice.append([x, y + 1, "right"])
        choice.append([x, y - 1, "left"])
        choice.append([x + 1, y, "down"])

    return choice



arrayReward = []
for i in range(500):
    point_keberhasilan = []
    CurrentState = -2
    x = 14
    y = 0
    print("Espisode")
    while(CurrentState != 500):
        choices = carijalan(x,y)
        print(choices)
        action = random.choice(choices)
        print(action)
        r = FungsiR(action)
        rx = r[0]
        ry = r[1]
        # print(rx, ry)
        q = HitungQ(R[rx][ry], choices)
        # GantiR(q)
        GantiQ(q)
        x = action[0]
        y = action[1]


        CurrentState = data[x][y]
        point_keberhasilan.append(CurrentState)
        print(CurrentState)
        if (CurrentState == 500):
            print("Goal State")
            print("Reward\t: ", np.sum(point_keberhasilan))
            arrayReward.append(np.sum(reward))


print("UP\t: ", R[0])
print("DOWN\t: ", R[1])
print("LEFT\t: ", R[2])
print("RIGHT\t: ", R[3])
print("UP\t: ", Q[0])
print("DOWN\t: ", Q[1])
print("LEFT\t: ", Q[2])
print("RIGHT\t: ", Q[3])

print("Max Reward\t: ",np.max(arrayReward))

