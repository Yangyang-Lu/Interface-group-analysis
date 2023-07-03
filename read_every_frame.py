
def read_every_frame(fileName, frame, every_frame_line):
    splitChar ='\t'
    dataSet = []

    with open(fileName) as f:
        for line in f.readlines()[(frame*every_frame_line):((frame+1)*every_frame_line)]:
            curline = line.strip().split(splitChar)  # 字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            dataSet.append(curline)
    return dataSet


