import ase.io
import numpy as np

execfile('COMMON.py')

f = open('TEMPL_1')
STR1 = f.readlines()
f.close()

f = open('TEMPL_2')
STR2 = f.readlines()
f.close()

shscript = open('RUNPWSCF.sh', 'w')

for a in indices:
    for i in range(3):  # x y z
        for sign in ['m', 'p']:  # plus minus
            for ndis in range(1, NFREE // 2 + 1):
                infile = ('%s.%d%s%s' %
                            (INP_PREFIX, a+1, 'xyz'[i],
                             ndis * sign))
                print infile
                # Compute displacement
                if sign == 'm':
                    disp = -ndis * DELTA
                else:
                    disp =  ndis * DELTA
                #
                pos = atoms.get_positions()
                print a, i
                pos[a,i] = pos[a,i] + disp  # move the atom
                print pos - atoms.get_positions()
                #
                f = open(infile,'w')
                f.writelines(STR1)
                #
                f.write('\nATOMIC_POSITIONS angstrom\n')
                for ia in range(Natoms):
                    f.write('%s %18.10f %18.10f %18.10f\n' %
                      (atoms[ia].symbol, pos[ia,0], pos[ia,1], pos[ia,2]) )
                f.write('\n')
                f.writelines(STR2)
                f.close()
                #
                # Run pwscf here or generate appropriate script to run it
                outfile = ('%s.%d%s%s' %
                          (OUT_PREFIX, a+1, 'xyz'[i],
                           ndis * sign))
                shscript.write('pw.x < ' + infile + ' > ' + outfile + '\n')

shscript.close()
