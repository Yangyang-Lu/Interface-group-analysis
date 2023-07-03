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
    with open("C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Ta-H2O2-SiO2\modal.data", "a", encoding='utf-8') as f:
        xyz_inf = ''
        for i in range(0, len(data)):
            xyz_inf = xyz_inf + " " + str(int(data[i][0])) + " " + str(int(data[i][1])) + " " + str(int(data[i][2])) + " " + str(float(data[i][3])) + " " + str(float(data[i][4])) + " " + str(float(data[i][5])) + " " + str(float(data[i][6])) + "\n"
            #for j in range(0, len(data[0])):
            #    xyz_inf = str(xyz_inf) + " " + str(data[i][j])
            #xyz_inf = xyz_inf + "\n"

        inf = str(xyz_inf)
        f.write(str(inf))
        f.close()


Cu_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Ta-H2O2-SiO2\Cu\Cu (1 1 1).txt"
Ta_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Ta-H2O2-SiO2\Ta\Ta (1 1 1).txt"
H2O2_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Ta-H2O2-SiO2\H2O2\H2O2-H2O-1.txt"
SiO2_file_path = "C:\\Users\dell001\Documents\Python Scripts\lammps\data\Cu-Ta-H2O2-SiO2\SiO2ball\SiO2_21A_3d.txt"
Cu_file_data = read_every_data(Cu_file_path)
Ta_file_data = read_every_data(Ta_file_path)
H2O2_file_data = read_every_data(H2O2_file_path)
SiO2_file_data = read_every_data(SiO2_file_path)
print(len(Cu_file_data))
print(len(Ta_file_data))
print(len(H2O2_file_data))
print(len(SiO2_file_data))
Cu_x = 88.541706
Cu_y = 51.119578
Cu_z = 0
Ta_x = 88.986533
Ta_y = 46.705817
Ta_z = 0
H2O2_x = 89.130154
H2O2_y = 97.61874
H2O2_z = 4.244293
SiO2_x = 42.78972
SiO2_y = 42.78972
SiO2_z = 42.78972
x = (Cu_x + Ta_x)/2
y = (Cu_y + Ta_y)
for i in range(0, len(Ta_file_data)):
    Ta_file_data[i][2] = float(Ta_file_data[i][2]) * float( x / Ta_x)
    Ta_file_data[i][3] = float(Ta_file_data[i][3]) + float(Cu_y)

for i in range(0,len(Cu_file_data)-1):
    Cu_file_data[i][2] = float(Cu_file_data[i][2]) * float( x / Cu_x )

for i in range(0, len(H2O2_file_data)):
    H2O2_file_data[i][2] = float(H2O2_file_data[i][2]) * float(x / H2O2_x )
    H2O2_file_data[i][3] = float(H2O2_file_data[i][3]) * float(y / H2O2_y )
for i in range(0, len(SiO2_file_data)):
    SiO2_file_data[i][4] = - float(SiO2_file_data[i][4])

total_atoms = len(Cu_file_data) + len(Ta_file_data) + len(H2O2_file_data) + len(SiO2_file_data)
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
    data[atom_number][1] = int(0)
    data[atom_number][2] = int(1)
    data[atom_number][3] = float(0.0000000000)
    data[atom_number][4] = float(Cu_file_data[i][2])
    data[atom_number][5] = float(Cu_file_data[i][3])
    data[atom_number][6] = float(Cu_file_data[i][4])
    atom_number = atom_number + 1

#####Ta  atom index 2
for i in range(0, len(Ta_file_data)):
    data[atom_number][0] = int(atom_number + 1)
    data[atom_number][1] = int(0)
    data[atom_number][2] = int(2)
    data[atom_number][3] = float(0.0000000000)
    data[atom_number][4] = float(Ta_file_data[i][2])
    data[atom_number][5] = float(Ta_file_data[i][3])
    data[atom_number][6] = float(Ta_file_data[i][4])
    atom_number = atom_number + 1
#####H2O2  H atom index 3
#          0 atom index 4
for i in range(0, len(H2O2_file_data)):
    data[atom_number][0] = int(atom_number + 1)
    data[atom_number][1] = int(0)
    if str(H2O2_file_data[i][1]) == 'H':
        data[atom_number][2] = int(3)
    elif str(H2O2_file_data[i][1]) == "O":
        data[atom_number][2] = int(4)
    data[atom_number][3] = float(0.0000000000)
    data[atom_number][4] = float(H2O2_file_data[i][2])
    data[atom_number][5] = float(H2O2_file_data[i][3])
    data[atom_number][6] = float(H2O2_file_data[i][4]) + 5
    atom_number = atom_number + 1

#####SiO2  Si atom index 5
#          0 atom index 6
for i in range(0, len(SiO2_file_data)):
    data[atom_number][0] = int(atom_number + 1)
    data[atom_number][1] = int(0)
    if str(SiO2_file_data[i][1]) == 'Si':
        data[atom_number][2] = int(5)
    elif str(SiO2_file_data[i][1]) == "O":
        data[atom_number][2] = int(6)
    data[atom_number][3] = float(0.0000000000)
    data[atom_number][4] = float(SiO2_file_data[i][2]) + 40
    data[atom_number][5] = float(SiO2_file_data[i][3]) + 30
    data[atom_number][6] = float(SiO2_file_data[i][4]) + 40
    atom_number = atom_number + 1

print(atom_number)
print(data[0])
print(data[len(data)-1])
write_data_file(data)
print(Cu_file_data[0])