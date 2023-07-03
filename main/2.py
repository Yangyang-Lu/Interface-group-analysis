import numpy as np

def read_every_frame(fileName):
    splitChar ='\t'
    dataSet = []

    with open(fileName) as f:
        for line in f.readlines()[(11):(3635)]:
            curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            dataSet.append(curline)
    return dataSet

def write_data_file(data):
    with open("C:\\Users\dell001\Documents\Python Scripts\lammps\PES\PES.txt", "a", encoding='utf-8') as f:
        xyz_inf = ''
        for i in range(0, len(data)):
            xyz_inf = xyz_inf + "  " + str(float(data[i][0])) + "  " + str(float(data[i][1])) + "  " + str(float(data[i][2])) + "\n"
            #for j in range(0, len(data[0])):
            #    xyz_inf = str(xyz_inf) + " " + str(data[i][j])
            #xyz_inf = xyz_inf + "\n"

        inf = str(xyz_inf)
        f.write(str(inf))
        f.close()




fileName = "C:\\Users\dell001\Documents\Python Scripts\lammps\PES\MoS2Graphen2.data"

dataset = read_every_frame(fileName)

for i in range(0,len(dataset)):
    if int(dataset[i][2]) == 1:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 2:
        dataset[i][2] = "Mo"
    elif int(dataset[i][2]) == 3:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 4:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 5:
        dataset[i][2] = "Mo"
    elif int(dataset[i][2]) == 6:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 7:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 8:
        dataset[i][2] = "Mo"
    elif int(dataset[i][2]) == 9:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 10:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 11:
        dataset[i][2] = "Mo"
    elif int(dataset[i][2]) == 12:
        dataset[i][2] = "S"
    elif int(dataset[i][2]) == 13:
        dataset[i][2] = "C"
C = 0
S = 0
Mo = 0

for i in range(0,len(dataset)):
    if dataset[i][2] == "Mo":
        Mo = Mo + 1
    if dataset[i][2] == "S":
        S = S + 1
    if dataset[i][2] == "C":
        C = C + 1
C_atoms = np.zeros((int(C ), 3))
S_atoms = np.zeros((int(S), 3))
Mo_atoms = np.zeros((int(Mo), 3))
cc = 0
ss = 0
mm = 0

for i in range(0,len(dataset)):
    if dataset[i][2] == "C":
        C_atoms[cc][0] = float(dataset[i][4])
        C_atoms[cc][1] = float(dataset[i][5])
        C_atoms[cc][2] = float(dataset[i][6])
        cc = cc + 1
    if dataset[i][2] == "S":
        S_atoms[ss][0] = float(dataset[i][4])
        S_atoms[ss][1] = float(dataset[i][5])
        S_atoms[ss][2] = float(dataset[i][6])
        ss = ss + 1
    if dataset[i][2] == "Mo":
        Mo_atoms[mm][0] = float(dataset[i][4])
        Mo_atoms[mm][1] = float(dataset[i][5])
        Mo_atoms[mm][2] = float(dataset[i][6])
        mm = mm + 1
pes = np.zeros((100*100, 3))
print(cc)
print(ss)
print(mm)

for i in range(0, 100):
    for j in range(0, 100):
        print(i * 100 + j)
        pes[i * 100 + j][0] = i * 0.1
        pes[i * 100 + j][1] = j * 0.1
        C = C_atoms
        for k in range(0, len(C)):
            C[k][0] = C[k][0] + (i / 10)
            C[k][1] = C[k][1] + (j / 10)
        for k in range(0, len(C)):
            for k1 in range(0, len(S_atoms)):
                dtx = float(C[k][0]) - float(S_atoms[k1][0])
                dty = float(C[k][1]) - float(S_atoms[k1][1])
                dtz = float(C[k][2]) - float(S_atoms[k1][2])
                dt = pow((pow(dtx, 2) + pow(dty, 2) + pow(dtz, 2)), 0.5)

                if dt <= 10:
                    f = 4 * 0.012035 * ((pow(3.39, 12)) / pow(dt, 12)) - 4 * 0.012035 * ((pow(3.39, 6)) / pow(dt, 6))
                    pes[i * 100 + j][2] = pes[i * 100 + j][2] + f
            for k2 in range(0, len(Mo_atoms)):
                dtx = float(C[k][0]) - float(Mo_atoms[k2][0])
                dty = float(C[k][1]) - float(Mo_atoms[k2][1])
                dtz = float(C[k][2]) - float(Mo_atoms[k2][2])
                dt = pow((pow(dtx, 2) + pow(dty, 2) + pow(dtz, 2)), 0.5)

                if dt <= 10:
                    f = 4 * 0.044758 * ((pow(2.949, 12)) / pow(dt, 12)) - 4 * 0.044758 * ((pow(2.949, 6)) / pow(dt, 6))
                    pes[i * 100 + j][2] = pes[i * 100 + j][2] + f

#print(pes)
write_data_file(pes)
print(pes)