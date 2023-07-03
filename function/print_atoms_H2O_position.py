from ovito.data import DataCollection
from ovito.io import *
import numpy as np
def print_atoms_H2O_position_Cu(data,Cu_H2O_atoms, point_O):
    positions = data.particles.positions
    tprop1 = data.particles['Particle Type']
    tprop = data.particles.identifiers.array
    #print(tprop1[...])
    #print(len(positions))
    #print(len(tprop))
    #point_O = []
    if len(Cu_H2O_atoms)> 0:
        for i in range(len(Cu_H2O_atoms)):
            #for j in range(len(Cu_H2O_atoms[i])):
            for j in range(0, 1):
                for s in range(len(tprop)):
                    if ((tprop[s]) == (Cu_H2O_atoms[i][j])):
                        #print(int(Cu_H2O_atoms[i][j]))
                        #print(tprop[s])
                        #print(tprop1[s])
                        #print(positions[s])
                        a = []
                        for l in range (0,3):
                            a.append(float(positions[s][l]))
                        #print(a)
                        point_O.append(a)
    len(Cu_H2O_atoms)
    #print(len(np.array(point_O)))
    #print(point_O)
    return point_O

    ######################################
def print_atoms_H2O_position_Si(data,Si_H2O_atoms, point_O):
    positions = data.particles.positions
    tprop1 = data.particles['Particle Type']
    tprop = data.particles.identifiers.array
    #print(tprop1[...])
    #print(len(positions))
    #print(len(tprop))
    #point_O = []
    if len(Si_H2O_atoms)> 0:
        for i in range(len(Si_H2O_atoms)):
            #for j in range(len(Cu_H2O_atoms[i])):
            for j in range(0, 1):
                for s in range(len(tprop)):
                    if ((tprop[s]) == (Si_H2O_atoms[i][j])):
                        #print(int(Cu_H2O_atoms[i][j]))
                        #print(tprop[s])
                        #print(tprop1[s])
                        #print(positions[s])
                        a = []
                        for l in range (0,3):
                            a.append(float(positions[s][l]))
                        #print(a)
                        point_O.append(a)
    len(Si_H2O_atoms)
    #print(len(np.array(point_O)))
    #print(point_O)
    return point_O

    ######################################
def deal_H2O_position(length, point_O):
    k = int(length/0.5)
    H2O_distribution = np.zeros((k,2))
    aaa = np.zeros((k,2))
    for i in range(0,k):
        H2O_distribution[i][0] = i
        H2O_distribution[i][1] = 0
    for i in range(len(point_O)):
        if point_O[i][0] < 0:
            point_O[i][0] = point_O[i][0] + 84.5
        if point_O[i][0] > 84.5:
            point_O[i][0] = point_O[i][0] - 84.5
    for i in range(len(point_O)):
        #print(point_O[i][0]//0.5)
        H2O_distribution[int(point_O[i][0]//0.5)][1] += 1
    for i in range(40, len(H2O_distribution)):
        aaa[i - 40][0] = i - 40
        aaa[i - 40][1] = H2O_distribution[i][1]
    for i in range(0, 40):
        aaa[i + 129][0] = i +129
        aaa[i + 129][1] = H2O_distribution[i][1]
    bbb = np.zeros((int(k/2), 2))
    for i in range(len(bbb)):
        bbb[i][0] = i
        bbb[i][1] = aaa[2*i][1] + aaa[2*i+1][1]


    #for i in range(len(H2O_distribution)):
        #print("%f %f"  %(H2O_distribution[i][0]/2, H2O_distribution[i][1]))
     #   print("%f %f" % (aaa[i][0]/2, aaa[i][1]))
    for i in range(len(bbb)):
        print("%f %f" % (bbb[i][0], bbb[i][1]))