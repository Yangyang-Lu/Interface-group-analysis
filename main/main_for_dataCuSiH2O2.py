#######################################
#use for get lammps.data file by yangyang Lu at 2020/10/11

########################################
import numpy as np

def read_every_data(fileName):
    splitChar ='\t'
    dataSet = []

    with open(fileName) as f:
        for line in f.readlines():
            curline = line.strip().split( )  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            dataSet.append(curline)
    return dataSet

def write_data_file(data):
    with open("C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Si-H2O2\modal.data", "a", encoding='utf-8') as f:
        xyz_inf = ''
        for i in range(0, len(data)):
            xyz_inf = xyz_inf + " " + str(int(data[i][0])) + " " + str(int(data[i][1])) + " " + str(
                int(data[i][2])) + " " + str(float(data[i][3])) + " " + str(float(data[i][4])) + " " + str(
                float(data[i][5])) + "\n"

            #xyz_inf = xyz_inf + " " + str(int(data[i][0])) + " " + str(int(data[i][1])) + " " + str(int(data[i][2])) + " " + str(float(data[i][3])) + " " + str(float(data[i][4])) + " " + str(float(data[i][5])) + " " + str(float(data[i][6])) + "\n"
            #for j in range(0, len(data[0])):
            #    xyz_inf = str(xyz_inf) + " " + str(data[i][j])
            #xyz_inf = xyz_inf + "\n"

        inf = str(xyz_inf)
        f.write(str(inf))
        f.close()


Cu_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Si-H2O2\Cu\Cu (1 1 1).txt"
Si_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Si-H2O2\Si\Si (1 1 1).txt"
H2O2_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Si-H2O2\H2O2\H2O (2).txt"
SiO2_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Si-H2O2\SiO2ball\SiO2_21A_3d.txt"
Cu_file_data = read_every_data(Cu_file_path)
Si_file_data = read_every_data(Si_file_path)
H2O2_file_data = read_every_data(H2O2_file_path)
SiO2_file_data = read_every_data(SiO2_file_path)
print(len(Cu_file_data))
print(len(Si_file_data))
print(len(H2O2_file_data))
print(len(SiO2_file_data))
Cu_x = 23.00381
Cu_y = 26.562512
Cu_z = 0
Si_x = 19.200424
Si_y = 26.604888
Si_z = 0
H2O2_x = 42.204234
H2O2_y = 26.5837
H2O2_z = 20

SiO2_x = 42.78972
SiO2_y = 42.78972
SiO2_z = 42.78972
x = (Cu_x + Si_x)
y = (Cu_y + Si_y)/2
for i in range(0, len(Si_file_data)):
    Si_file_data[i][2] = float(Si_file_data[i][2]) + float(Cu_x) +0.5
    Si_file_data[i][3] = float(Si_file_data[i][3]) * float( y / Si_y)

for i in range(0,len(Cu_file_data)-1):
    Cu_file_data[i][2] = float(Cu_file_data[i][2]) * float( y / Cu_y )

for i in range(0, len(H2O2_file_data)):
    if float(H2O2_file_data[i][2]) < 0:
        H2O2_file_data[i][2] = float(H2O2_file_data[i][2]) + 42.204234
    if float(H2O2_file_data[i][2]) > 42.204234:
        H2O2_file_data[i][2] = float(H2O2_file_data[i][2]) - 42.204234
    if float(H2O2_file_data[i][3]) < 0:
        H2O2_file_data[i][3] = float(H2O2_file_data[i][3]) + 26.5837
    if float(H2O2_file_data[i][3]) > 26.5837:
        H2O2_file_data[i][3] = float(H2O2_file_data[i][3]) - 26.5837
    H2O2_file_data[i][2] = float(H2O2_file_data[i][2]) * float(x / H2O2_x )
    H2O2_file_data[i][3] = float(H2O2_file_data[i][3]) * float(y / H2O2_y )
for i in range(0, len(SiO2_file_data)):
    SiO2_file_data[i][4] = - float(SiO2_file_data[i][4])
#total_atoms = len(Cu_file_data) + len(Si_file_data) + len(H2O2_file_data) + len(SiO2_file_data)
total_atoms = len(Cu_file_data) + len(Si_file_data) + len(H2O2_file_data)
print(total_atoms)
print(total_atoms)
#data = np.zeros((21*23*7, 4))
#for i in range(1, 21):
#    for j in range(1, 23):
#        for k in range(1, 7):
#            data[((i-1)*(j*7)+(j-1)*7 + j ][0]
#print(data[0])
#print(len(data))
data = np.zeros((int(total_atoms), 7))
atom_number = 0
#####Cu  atom index 1
for i in range(0, len(Cu_file_data)):
    data[atom_number][0] = int(atom_number + 1)
    #data[atom_number][1] = int(0)
    data[atom_number][1] = int(1)
    data[atom_number][2] = float(0.0000000000)
    data[atom_number][3] = float(Cu_file_data[i][2])
    data[atom_number][4] = float(Cu_file_data[i][3])
    data[atom_number][5] = float(Cu_file_data[i][4])
    atom_number = atom_number + 1

#####Si  atom index 2
for i in range(0, len(Si_file_data)):
    data[atom_number][0] = int(atom_number + 1)
    #data[atom_number][1] = int(0)
    data[atom_number][1] = int(2)
    data[atom_number][2] = float(0.0000000000)
    data[atom_number][3] = float(Si_file_data[i][2])
    data[atom_number][4] = float(Si_file_data[i][3])
    data[atom_number][5] = float(Si_file_data[i][4]) + 1
    atom_number = atom_number + 1
#####H2O2  H atom index 3
#          0 atom index 4
for i in range(0, len(H2O2_file_data)):
    data[atom_number][0] = int(atom_number + 1)
   # data[atom_number][1] = int(0)
    if str(H2O2_file_data[i][1]) == 'H':
        data[atom_number][1] = int(3)
    elif str(H2O2_file_data[i][1]) == "O":
        data[atom_number][1] = int(4)
    data[atom_number][2] = float(0.0000000000)
    data[atom_number][3] = float(H2O2_file_data[i][2])
    data[atom_number][4] = float(H2O2_file_data[i][3])
    data[atom_number][5] = float(H2O2_file_data[i][4]) + 25.3
    atom_number = atom_number + 1

#####SiO2  Si atom index 5
#          0 atom index 6
#for i in range(0, len(SiO2_file_data)):
#    data[atom_number][0] = int(atom_number + 1)
#    data[atom_number][1] = int(0)
#    if str(SiO2_file_data[i][1]) == 'Si':
#        data[atom_number][2] = int(5)
#    elif str(SiO2_file_data[i][1]) == "O":
#        data[atom_number][2] = int(6)
#    data[atom_number][3] = float(0.0000000000)
#    data[atom_number][4] = float(SiO2_file_data[i][2]) + 40
#    data[atom_number][5] = float(SiO2_file_data[i][3]) + 30
#    data[atom_number][6] = float(SiO2_file_data[i][4]) + 40
#    atom_number = atom_number + 1

print(atom_number)
print(data)
print(data[len(data)-1])
write_data_file(data)
