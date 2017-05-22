import numpy as np
from ase.units import Ry, Bohr

def read_pwscf_forces(logfile):
    f = open(logfile,'r')

    line = f.readline()
    while not ('number of atoms' in line):
        line = f.readline()

    #print line
    Natoms = int( line.split()[4] )

    while not ('Forces acting' in line):
        line = f.readline()
    line = f.readline()
    #
    forces = np.zeros( (Natoms,3) )
    for ia in range(Natoms):
        line = f.readline()
        #print line
        forces[ia,0] = float( line.split()[6] )
        forces[ia,1] = float( line.split()[7] )
        forces[ia,2] = float( line.split()[8] )
    f.close()
    return forces*(Ry/Bohr)
