from ase.structure import molecule

atoms = molecule('CH4')

atoms.set_cell( [15, 15, 15] )
atoms.set_pbc( [True,True,True] )
atoms.center()
atoms.write('CH4.xyz')


