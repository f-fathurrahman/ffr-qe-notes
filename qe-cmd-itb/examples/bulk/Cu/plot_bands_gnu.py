import numpy as np
import matplotlib.pyplot as plt
from ase.units import Ry

NBANDS   = 8
NKPOINTS = 60

databands = np.loadtxt('bands.out.gnu')

ebands = np.zeros( (NKPOINTS, NBANDS) )
kvec   = np.zeros( (NKPOINTS, NBANDS) )

for ib in range(NBANDS):
  idx1 = (ib)*NKPOINTS
  idx2 = (ib+1)*NKPOINTS
  ebands[:,ib] = databands[idx1:idx2,1]*Ry
  kvec[:,ib]   = databands[idx1:idx2,0]

Efermi = 16.4769 # in eV
ebands[:,:] = ebands[:,:] - Efermi

Emin = -10
Emax = 5

plt.figure(figsize=(5, 6))
plt.clf()
for ib in range(NBANDS):
  plt.plot( kvec[:,ib], ebands[:,ib], marker='o' )

Xkpt   = [0.0000, 0.7071, 1.5731, 2.5731, 3.0731, 3.4267]
labelX = ['W', 'L', r'$\Gamma$', 'X', 'W', 'K']

for p in Xkpt:
  plt.plot([p, p], [Emin, Emax], 'k-')
plt.xticks(Xkpt, labelX)

plt.plot([0, Xkpt[-1]], [0, 0], 'k--')

plt.ylim( Emin,Emax )
plt.xlim( 0, Xkpt[-1] )
plt.xlabel('k vector')
plt.ylabel('Energy (eV)')
plt.title('Band structure of Cu')
plt.savefig('Cu_bands_v1.pdf')


