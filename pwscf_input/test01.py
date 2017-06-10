from __future__ import print_function
from ase import Atoms
from ControlNameList import *
from SystemNameList import *

atoms = Atoms('NH3')

ctrl_NL = ControlNameList()
ctrl_NL.write_all()

sys_NL = SystemNameList(atoms)
sys_NL.write_all()
