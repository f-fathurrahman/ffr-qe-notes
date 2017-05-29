import numpy as np
import matplotlib.pyplot as plt
from ase.units import Ry

data1 = np.loadtxt('ecut_vs_ene')
ecut = data1[:,0]
ene  = data1[:,1]*Ry
ene  = ene - np.min(ene)

plt.clf()
plt.plot( ecut, ene, marker='o' )
plt.xlabel('Ecut (Ry)')
plt.ylabel('Etot relative (eV)')
plt.grid()
plt.savefig( 'conv1.png', dpi=300 )


