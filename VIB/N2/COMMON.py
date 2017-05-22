# Indices of atoms to be moved (vibrate)
# index starts from 1 following PWSCF convention
IDXMOVE = [1,2]

atoms = ase.io.read('STRUCT.xyz')
Natoms = len(atoms)

#
INP_PREFIX = 'PWINPUT'
OUT_PREFIX = 'LOG'

# Parameter default
NFREE = 2
DELTA = 0.01
METHOD = 'default'
DIRECTION = 'central'

# Some setup stuffs
NMOVE = len(IDXMOVE)
indices = range(NMOVE)
indices = np.asarray(indices)
