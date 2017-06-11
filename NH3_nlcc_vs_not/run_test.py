from __future__ import print_function

from ase import Atoms
from ase.units import Bohr
import ase.io

import sys
sys.path.append('../')

from qeManager import *

import os

atoms = ase.io.read('../structures/NH3.xyz')

# set periodic  bounding box
atoms.set_pbc([True,True,True])
cell = np.array([16.0,16.0,16.0])*Bohr
atoms.set_cell(cell)
atoms.center()

pspFiles = ['H.q1.gth', 'N.q5.gth']

ecutwfcs = np.arange(20.,50.,2.)

for ec in ecutwfcs:
    inpName = 'PWINPUT_' + str(int(ec))
    pwinput = PWSCFInput(atoms, pspFiles, filename=inpName)
    #
    pwinput.SYSTEM.set_ecutwfc(ec)
    #
    pwinput.CONTROL.pseudo_dir = '../GTH_PBE'
    pwinput.CONTROL.disk_io = 'none'
    pwinput.write()
    #
    logName = 'LOG_' + str(int(ec))
    os.system('pw.x < ' + inpName + ' > ' + logName)


