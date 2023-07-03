
def file_information_get(fileName):
    splitChar ='\t'
    dataSet = []
    with open(fileName, encoding='utf-8') as f:
        count =  0
        for line in f:
            count += 1
    f.close()
    with open(fileName, encoding='utf-8') as f:
        for line in f.readlines()[3:4]:
            curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            dataSet.append(curline)
    return dataSet, count

def get_atoms_num_every_frame_line_and_total_frame(fileName):
    [atoms, total_line] = file_information_get(fileName)
    total_atoms = (int(str(atoms[0]).replace("['", "").replace("']", "").replace("[", "").replace("]", "")))
    every_frame_line = total_atoms + 9
    print(total_line)
    total_frames = int(total_line / every_frame_line)
    # for i in K:
    #    KK.append(str(i).replace("['", "").replace("']", ""))

    return total_atoms ,every_frame_line, total_frames
