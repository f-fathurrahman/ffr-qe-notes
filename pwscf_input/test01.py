from ase import Atoms
from SystemNameList import *

atoms = Atoms('NH3')

sys_NL = SystemNameList(atoms)
sys_NL.write()
