##############################################
## for lammps dump file Data post processing
import numpy as np
import tkinter.filedialog
from fun.get_atoms_num_every_frame_line_and_total_frame import get_atoms_num_every_frame_line_and_total_frame
from fun.read_every_frame import read_every_frame
from fun.deal_frame_information import deal_frame_information
from fun.write_file import write_top_file
from fun.write_file import write_bottom_file
from fun.write_file import write_total_file
from fun.write_file import write_group_top_file
from fun.write_file import write_group_bottom_file
import re
from tkinter import *
fileName = tkinter.filedialog.askopenfilename()
print(fileName)

# get information of the file including total atoms, every frame line and total frames
[total_atoms, every_frame_line, total_frames] = get_atoms_num_every_frame_line_and_total_frame(fileName)
print(total_atoms)
print(every_frame_line)
print(total_frames)
total_top_force = np.zeros((int(total_frames), 8))
total_bottom_force = np.zeros((int(total_frames), 8))
for i in range(0, (int(total_frames))):
    total_top_force[i][0] = i
    total_bottom_force[i][0] = i


#################################################
# get every frame information
for frame in range(0,(total_frames)):
    print(frame)
#for frame in range(0, 3):
    every_frame_information = read_every_frame(fileName, frame, every_frame_line)
    #print(every_frame_information)
    #######################################################
    # get file basement information title and position
    [title, top_title, bottom_title, top_data, bottom_data] = deal_frame_information(every_frame_information)

    #####################################################################
    # compute the force in atoms and group
    [top_data, bottom_data] = compute_force(top_data, bottom_data)
    #####################################################################
    # compute the force of group on group
    [total_top_force, total_bottom_force] = compute_total_force(top_data, bottom_data, total_top_force, total_bottom_force, frame)
    # write file
    #print(title)

    write_top_file(top_title, top_data)
    write_bottom_file(bottom_title, bottom_data)
    write_total_file(title, top_data, bottom_data)
write_group_top_file(total_top_force)
write_group_bottom_file(total_bottom_force)
print("Successful completed")
#print(total_top_force)
#print(top_data)