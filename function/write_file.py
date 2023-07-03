from ovito.io import export_file
def write_to_file(frame, data):
    Write_method = "a"
    path = "C:\\Users\\dell001\\Documents\\Python Scripts\\lammps\\data\\Cu-Si-H2O-H2O2\\MD\\H2O\\reaxff_after.dump"
    if frame == 0:
        Write_method = "w"
    else:
        Write_method = "a"
    write_file(frame, data, Write_method, path)

def write_file(frame, data, Write_method, filename):
    export_file(data, "Temp.dump", "lammps/dump", columns=["Particle Identifier", "Particle Type", "Position.X", "Position.Y", "Position.Z"])
    filehandle = open("Temp.dump", "r")
    fames_information = filehandle.read()
    filehandle.close()
    with open(filename, Write_method) as file_object:
        file_object.write(fames_information)
    file_object.close()
