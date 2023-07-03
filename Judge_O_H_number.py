import numpy as np
def Judge_SiH_Cu_H(bonds_H_Si, bonds_H_Cu):
    if (len(bonds_H_Si) > 0):
        atomsH_Si = np.unique((np.array(bonds_H_Si)[:, 0]).tolist())
    else:
        atomsH_Si = list()
    if (len(bonds_H_Cu) > 0):
        atomsH_Cu = np.unique((np.array(bonds_H_Cu)[:, 0]).tolist())
    else:
        atomsH_Cu = list()
    return atomsH_Si, atomsH_Cu

def Judge_othe_OH_atoms_abs(other_OH_atoms, bonds_O_Si, bonds_O_Cu):
    OH_Si = list()
    OH_Cu = list()
    OH_Si_Cu = list()
    OH_without_abs = list()
    if len(other_OH_atoms) > 0:
        for i in range(len(other_OH_atoms)):
            if (np.sum(bonds_O_Si == other_OH_atoms[i][0])) > 0 and (np.sum(bonds_O_Cu == other_OH_atoms[i][0])) == 0:
                OH_Si.append(other_OH_atoms[i])
            if (np.sum(bonds_O_Si == other_OH_atoms[i][0])) == 0 and (np.sum(bonds_O_Cu == other_OH_atoms[i][0])) > 0:
                OH_Cu.append(other_OH_atoms[i])
            if (np.sum(bonds_O_Si == other_OH_atoms[i][0])) > 0 and (np.sum(bonds_O_Cu == other_OH_atoms[i][0])) > 0:
                OH_Si_Cu.append(other_OH_atoms[i])
            if (np.sum(bonds_O_Si == other_OH_atoms[i][0])) == 0 and (np.sum(bonds_O_Cu == other_OH_atoms[i][0])) == 0:
                OH_without_abs.append(other_OH_atoms[i])
    return OH_Si, OH_Cu, OH_Si_Cu, OH_without_abs

def get_O_H_id(number, bonds_O_H, a):
    aa = np.zeros(number+1)
    aa[0] = bonds_O_H[(a[0,0]), 0]
    for i in range(0, number):
       # print(bonds_O_H[(a[0][i]), 0])
        aa[i + 1] = bonds_O_H[(a[0][i]),1]
    return aa


def Judge_O_H_number(bonds_O_H):
 #Judging  atoms in the bonds
    #a = np.reshape(np.array(np.where(atoms_type == 4)),(np.sum(atoms_type == 4),1))
    bondsOH = np.matrix(bonds_O_H)
    atoms = np.array(np.unique(np.transpose((bondsOH[:,0])).tolist()))
    #print(len(atoms))
    O_H1 = 0
    O_H2 = 0
    O_H3 = 0
    O_H4 = 0
    bond_O_H1 = list()
    bond_O_H2 = list()
    bond_O_H3 = list()
    bond_O_H4 = list()
    for i in range(len(atoms)):
         number = np.sum(bondsOH == atoms[i])
         a = np.reshape(np.array(np.where(bondsOH == atoms[i])), (2, np.sum(bondsOH == atoms[i])))
         #print(type(a))
         if number == 1:
             bond_O_H1.append(get_O_H_id(number, bondsOH, a))
             O_H1 = O_H1 + 1
         if number == 2:
             bond_O_H2.append(get_O_H_id(number, bondsOH, a))
             O_H2 = O_H2 + 1
         if number == 3:
             bond_O_H3.append(get_O_H_id(number, bondsOH, a))
             O_H3 = O_H3 + 1
         if number == 4:
             bond_O_H4.append(get_O_H_id(number, bondsOH, a))
             O_H4 = O_H4 + 1
    return bond_O_H1, bond_O_H2, bond_O_H3, bond_O_H4

def Judge_H2O_adsorb(bond_O_H2,bonds_O_Si, bonds_O_Cu):
    Cu_H2O_atoms = list()
    Si_H2O_atoms = list()
    Both_H20_atoms = list()
    Just_H2O_atoms = list()
    for i in range (len(bond_O_H2)):
        if (np.sum(bonds_O_Si == bond_O_H2[i][0])) > 0 and (np.sum(bonds_O_Cu == bond_O_H2[i][0])) == 0:
            Si_H2O_atoms.append(bond_O_H2[i])
        if (np.sum(bonds_O_Si == bond_O_H2[i][0])) == 0 and (np.sum(bonds_O_Cu == bond_O_H2[i][0])) > 0:
            Cu_H2O_atoms.append(bond_O_H2[i])
        if (np.sum(bonds_O_Si == bond_O_H2[i][0])) > 0 and (np.sum(bonds_O_Cu == bond_O_H2[i][0])) > 0:
            Both_H20_atoms.append(bond_O_H2[i])
        if (np.sum(bonds_O_Cu == bond_O_H2[i][0])) == 0 and (np.sum(bonds_O_Si == bond_O_H2[i][0])) == 0:
            Just_H2O_atoms.append(bond_O_H2[i])

    return Cu_H2O_atoms, Si_H2O_atoms, Both_H20_atoms, Just_H2O_atoms

def Judge_H2O2(bonds_O_O, bond_O_H1):
    if len(bonds_O_O) > 0:
        bondsOH1 = np.matrix(bond_O_H1)
        H2O2_number = 0
        for i in range(len(bonds_O_O)):
            if ((np.sum(bondsOH1 == bonds_O_O[i][0]))> 0) and ((np.sum(bondsOH1 == bonds_O_O[i][1]))> 0):
                #H2O2_atoms.append(bondsOH1[(np.where(bondsOH1 ==  bonds_O_O[i][0])[0][0])] + bondsOH1[(np.where(bondsOH1 ==  bonds_O_O[i][0])[0][0])])
                H2O2_number = H2O2_number + 1
        H2O2_atoms =  np.zeros((H2O2_number, 4), dtype=np.int64)
        other_OH_atoms = np.zeros(((len(bondsOH1)- 2 * H2O2_number), 4), dtype=np.int64)
        H2O2_number = 0
        #hhh = list()
        for i in range(len(bonds_O_O)):
            if ((np.sum(bondsOH1 == bonds_O_O[i][0])) > 0) and ((np.sum(bondsOH1 == bonds_O_O[i][1])) > 0):
                H2O2_atoms[H2O2_number,0] = int(bondsOH1[(np.where(bondsOH1 == bonds_O_O[i][0])[0]), 0])
                H2O2_atoms[H2O2_number,1] = bondsOH1[(np.where(bondsOH1 == bonds_O_O[i][0])[0]), 1]
                H2O2_atoms[H2O2_number,2] = bondsOH1[(np.where(bondsOH1 == bonds_O_O[i][1])[0]), 0]
                H2O2_atoms[H2O2_number,3] = bondsOH1[(np.where(bondsOH1 == bonds_O_O[i][1])[0]), 1]
                #hhh.append(bondsOH1[(np.where(bondsOH1 == bonds_O_O[i][0])[0])])
                #hhh.append(bondsOH1[(np.where(bondsOH1 == bonds_O_O[i][1])[0])])
                H2O2_number = H2O2_number + 1
        lone_HO_number = 0
        for i in range(len(bondsOH1)):
            if ((np.sum(H2O2_atoms == bondsOH1[i, 0])) == 0):
                other_OH_atoms[lone_HO_number, 0] = bondsOH1[i, 0]
                other_OH_atoms[lone_HO_number, 1] = bondsOH1[i, 1]
                lone_HO_number = lone_HO_number + 1
    else:
        H2O2_atoms = list()
        other_OH_atoms = list()
    return H2O2_atoms, other_OH_atoms
