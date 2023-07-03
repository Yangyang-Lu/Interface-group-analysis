
def deal_frame_information(every_frame_information):
    line = len(every_frame_information)
    title = []
    data = []
    top_data = []
    bottom_data = []
    for i in range(0, 8):
        title.append(every_frame_information[i])
    title.append(str(every_frame_information[8]).replace("['", "").replace("']", '') + " " + "Elj" + " " + "Edft" + " " + "Evderw" + " " + "Erv")
    #print(title)
    #print(len(title))
    for i in range(9, line):
        data.append(every_frame_information[i])
    #print(len(data))
    for i in range(0, len(data)):
        line_data = str(str(data[i]).replace("['", "").replace("']", "")).split( )
        if int(line_data[1]) == 1:
            top_data.append(line_data)
        if int(line_data[1]) == 2:
            bottom_data.append(line_data)
    top_title =[]
    bottom_title = []
    for t in title:
        top_title.append(t)
        bottom_title.append(t)

    top_title[3] = len(top_data)
    bottom_title[3] = len(bottom_data)
    for i in range(0,len(top_data)):
        top_data[i][len(top_data[i]) - 1] = 0
        top_data[i][len(top_data[i]) - 2] = 0
        top_data[i][len(top_data[i]) - 3] = 0
        top_data[i].append(0)
        top_data[i].append(0)
        top_data[i].append(0)
        top_data[i].append(0)
    for i in range(0,len(bottom_data)):
        bottom_data[i][len(bottom_data[i]) - 1] = 0
        bottom_data[i][len(bottom_data[i]) - 2] = 0
        bottom_data[i][len(bottom_data[i]) - 3] = 0
        bottom_data[i].append(0)
        bottom_data[i].append(0)
        bottom_data[i].append(0)
        bottom_data[i].append(0)

    #print("top_data")
    #print(len(top_data))
    #print(len(top_data[1]))
    #print(top_data[1])
    #print(top_title)
    #print("bottom_data")
    #print(len(bottom_data))
    #print(len(bottom_data[1]))
    #print(bottom_title)
    #print(bottom_data[1])
    return title, top_title, bottom_title,top_data, bottom_data


