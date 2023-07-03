import numpy as np

def Judge_bond_list(bonds_elements_array, bonds_array):
    # Judging  atoms in the bonds
    bonds_O_O  = list()
    bonds_O_H  = list()
    bonds_O_Si = list()
    bonds_O_Cu = list()
    bonds_H_H = list()
    bonds_H_Si = list()
    bonds_H_Cu = list()
    bonds_Si_Si = list()
    for i in range(len(bonds_elements_array)):
        ######################################
        #O-X

        #O-O
        if (bonds_elements_array[i,0] == 4) and (bonds_elements_array[i,1] ==4):
            bonds_O_O.append([bonds_array[i][0],bonds_array[i][1]])
        #O-H
        if (bonds_elements_array[i,0] == 4) and (bonds_elements_array[i,1] == 3):
            bonds_O_H.append([bonds_array[i][0],bonds_array[i][1]])
        if (bonds_elements_array[i,0] == 3) and (bonds_elements_array[i,1] == 4):
            bonds_O_H.append([bonds_array[i][1],bonds_array[i][0]])
        #O-Si
        if (bonds_elements_array[i,0] == 4) and (bonds_elements_array[i,1] == 2):
            bonds_O_Si.append([bonds_array[i][0],bonds_array[i][1]])
        if (bonds_elements_array[i,0] == 2) and (bonds_elements_array[i,1] == 4):
            bonds_O_Si.append([bonds_array[i][1],bonds_array[i][0]])
        # O-C
        if (bonds_elements_array[i, 0] == 4) and (bonds_elements_array[i, 1] == 1):
            bonds_O_Cu.append([bonds_array[i][0], bonds_array[i][1]])
        if (bonds_elements_array[i, 0] == 1) and (bonds_elements_array[i, 1] == 4):
            bonds_O_Cu.append([bonds_array[i][1], bonds_array[i][0]])
        ##########
        #H-X
        #H-H
        if (bonds_elements_array[i,0] == 3) and (bonds_elements_array[i,1] ==3):
            bonds_H_H.append([bonds_array[i][0],bonds_array[i][1]])
        #H-Si
        if (bonds_elements_array[i,0] == 3) and (bonds_elements_array[i,1] ==2):
            bonds_H_Si.append([bonds_array[i][0],bonds_array[i][1]])
        if (bonds_elements_array[i, 0] == 2) and (bonds_elements_array[i, 1] == 3):
            bonds_H_Si.append([bonds_array[i][1], bonds_array[i][0]])
        # H-Cu
        if (bonds_elements_array[i, 0] == 3) and (bonds_elements_array[i, 1] == 2):
            bonds_H_Si.append([bonds_array[i][0], bonds_array[i][1]])
        if (bonds_elements_array[i, 0] == 2) and (bonds_elements_array[i, 1] == 3):
            bonds_H_Si.append([bonds_array[i][1], bonds_array[i][0]])
        #Si-X
        # Si-Si
        if (bonds_elements_array[i, 0] == 2) and (bonds_elements_array[i, 1] == 2):
            bonds_Si_Si.append([bonds_array[i][0], bonds_array[i][1]])

    #bonds_O_O = np.matrix(bonds_O_O)
    #bonds_O_H = np.matrix(bonds_O_H)
    #bonds_O_Si = np.matrix(bonds_O_Si)
    #bonds_O_Cu = np.matrix(bonds_O_Cu)
    #bonds_H_H = np.matrix(bonds_H_H)
    #bonds_H_Si = np.matrix(bonds_H_Si)
    #bonds_H_Cu = np.matrix(bonds_H_Cu)
    #bonds_Si_Si = np.matrix(bonds_Si_Si)
    return(bonds_O_O, bonds_O_H, bonds_O_Si, bonds_O_Cu, bonds_H_H, bonds_H_Si, bonds_H_Cu, bonds_Si_Si)


