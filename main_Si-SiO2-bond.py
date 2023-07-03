# Import OVITO modules.
from ovito.io import *
from ovito.modifiers import *
from ovito.data import *
from ovito import dataset

from ovito.io import import_file
from functionSi_SiO2_Bond.Judge_O_H_number import Judge_H2O_number
from functionSi_SiO2_Bond.Judge_O_H_number import Judge_SiOSi_bond_number
from functionSi_SiO2_Bond.deal_inf import deal_inf


from PySide2.QtCore import Qt
#Import standard Python and NumPy modules.
import sys
import numpy as np
import subprocess
start = 0
file_name = ['f1.dump','f2.dump','f3.dump','f4.dump','f5.dump']
for file in range(len(file_name)):
    #node = import_file('C:\\Users\\dell001\\Documents\\Python Scripts\\lammps\\data\\Si-H20-H2O2\\MD\\H2O\\reaxff.dump', multiple_frames = True)
    file_path = str("C:\\Users\\dell001\\Documents\\Materials Studio Projects\\Si-SiO2\\Si-H2O\\Si-SiO2 lammps\\small model\\wang\\10Gpa\\")+str(file_name[file])
    print(file_path)
    start = deal_inf(start, file_path)
