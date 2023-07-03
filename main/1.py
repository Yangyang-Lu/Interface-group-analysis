##############################################
## for lammps data file


def read_file(fileName):
    splitChar ='\t'
    title = []
    data = []
    with open(fileName) as f:
        count = 0
        for line in f:
            count += 1
    f.close()
    with open(fileName) as f:
        i = 0
        for line in f.readlines()[0:count]:
            i += 1
            curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            if i < 12:
                title.append(str(curline).replace("['", "").replace("']", ""))
            else:
                data.append(curline)
    f.close()
    title[3] = str(title[3]).replace("3", "12")
    return title, data


def write_data_file(filename,title, data):
    with open(filename, "w", encoding='utf-8') as f:
        xyz_inf = ''
        for i in range(0, len(title)):
            xyz_inf = str(xyz_inf) + str(title[i]) + "\n"
        for i in range(0, len(data)):

            for j in range(0, len(data[0])):
                xyz_inf = str(xyz_inf)+ " " + str(data[i][j])
            xyz_inf = xyz_inf + "\n"
        inf = str(xyz_inf)
        f.write(str(inf))
        f.close()

fileName = "C:\\Users\dell001\Documents\Python Scripts\lammps\MoS2\mos2.data"
[title, data] = read_file(fileName)
for i in range(0, len(data)):
    data[i][2] = 0
    data[i][1] = 0
for i in range(0, len(data)):
    k = (float(data[i][4]) % (6.332000)) / (6.332000 / 4)
    if float(data[i][6]) == 0.000000:
        if ((-0.1 < k < 0.1) or (3.9 < k)):
            data[i][2] = 3
        elif 0.9 < k < 1.1:
            data[i][2] = 6
        elif 1.9 < k < 2.1:
            data[i][2] = 9
        elif 2.9 < k < 3.1:
            data[i][2] = 12
    elif float(data[i][6]) == 3.170000:
        if ((-0.1 < k < 0.1) or (3.9 < k)):
            data[i][2] = 1
        elif 0.9 < k < 1.1:
            data[i][2] = 4
        elif 1.9 < k < 2.1:
            data[i][2] = 7
        elif 2.9 < k < 3.1:
            data[i][2] = 10
    elif float(data[i][6]) == 1.576000:
        if ((-0.1 < k < 0.1) or (3.9 < k)):
            data[i][2] = 5
        elif 0.9 < k < 1.1:
            data[i][2] = 2
        elif 1.9 < k < 2.1:
            data[i][2] = 11
        elif 2.9 < k < 3.1:
            data[i][2] = 8
filename = "C:\\Users\dell001\Documents\Python Scripts\lammps\MoS2\mos2-2.data"
write_data_file(filename, title, data)
print("Successful completed")