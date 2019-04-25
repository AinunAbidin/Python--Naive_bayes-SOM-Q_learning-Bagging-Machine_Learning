import csv

data = []
with open('DataTugas3ML2019.txt','r') as f:
    for row in csv.reader(f,delimiter='\t'):
        data.append(row)

print(data[1][2])