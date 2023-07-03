from ovito.modifiers import ExpressionSelectionModifier,DeleteSelectedModifier
from ovito.io import *
import numpy as np
def delet_atoms(data,atoms_id):
    if len(atoms_id)> 0:
        atoms_delet = ""
        for i in range (len(atoms_id)):
            for j in range(len(atoms_id[0])):
                atoms_delet = atoms_delet + "ParticleIdentifier == " + str(int(atoms_id[i][j]))
                if (len(atoms_id)):
                    if (((j == len(atoms_id[0])-1) and (i == (len(atoms_id))-1))) < 0.5:
                         atoms_delet = atoms_delet + " || "
        #print(atoms_delet)
        data.apply(ExpressionSelectionModifier(expression=atoms_delet))
        data.apply(DeleteSelectedModifier())
    return data