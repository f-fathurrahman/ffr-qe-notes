import ase.io
import numpy as np
from math import sin, pi, sqrt, log
import ase.units as units
from sys import stdout

execfile('COMMON.py')
execfile('read_pwscf_forces.py')

n = 3 * len(indices)
H = np.empty((n, n))
r = 0

#if direction != 'central':
#    feq = load(self.name + '.eq.pckl')

for a in indices:
    for i in 'xyz':
        name = '%s.%d%s' % (OUT_PREFIX, a+1, i)
        #print name
        fminus = read_pwscf_forces(name + 'm')
        fplus  = read_pwscf_forces(name + 'p')
        if METHOD == 'frederiksen':
            fminus[a] -= fminus.sum(0)
            fplus[a]  -= fplus.sum(0)
        if NFREE == 4:
            fminusminus = read_pwscf_forces(name + 'mm')
            fplusplus   = read_pwscf_forces(name + 'mm')
            if METHOD == 'frederiksen':
                fminusminus[a] -= fminusminus.sum(0)
                fplusplus[a] -= fplusplus.sum(0)
        if DIRECTION == 'central':
            if NFREE == 2:
                H[r] = .5 * (fminus - fplus)[indices].ravel()
            else:
                H[r] = H[r] = (-fminusminus +
                               8 * fminus -
                               8 * fplus +
                               fplusplus)[indices].ravel() / 12.0
        elif DIRECTION == 'forward':
            H[r] = (feq - fplus)[indices].ravel()
        else:
            assert DIRECTION == 'backward'
            H[r] = (fminus - feq)[indices].ravel()
        H[r] /= 2 * DELTA
        r += 1
H += H.copy().T

m = atoms.get_masses()
if 0 in [m[index] for index in indices]:
    raise RuntimeError('Zero mass encountered in one or more of '
                       'the vibrated atoms. Use Atoms.set_masses()'
                       ' to set all masses to non-zero values.')

print m
im = np.repeat(m[indices]**-0.5, 3)
omega2, modes = np.linalg.eigh(im[:, None] * H * im)
modes = modes.T.copy()

# Conversion factor:
s = units._hbar * 1e10 / sqrt(units._e * units._amu) # original
hnu = s * omega2.astype(complex)**0.5

print hnu

# conversion factor
s = 0.01 * units._e / units._c / units._hplanck  # to cm^{-1}

stdout.write('---------------------\n')
stdout.write('  #    meV     cm^-1\n')
stdout.write('---------------------\n')
for n, e in enumerate(hnu):
    if e.imag != 0:
        c = 'i'
        e = e.imag
    else:
        c = ' '
        e = e.real
    stdout.write('%3d %6.1f%s  %7.1f%s\n' % (n, 1000 * e, c, s * e, c))
stdout.write('---------------------\n')

# write to jmol

fd = open('VIBMODES.xyz', 'w')
symbols = atoms.get_chemical_symbols()
f = hnu/units.invcm

mode = np.zeros((len(atoms), 3))
for n in range(3 * len(indices)):
    fd.write('%6d\n' % len(atoms))
    if f[n].imag != 0:
        c = 'i'
        f[n] = f[n].imag
    else:
        c = ' '
    fd.write('Mode #%d, f = %.1f%s cm^-1' % (n, f[n], c))
    fd.write('.\n')
    #mode = self.get_mode(n)
    mode[indices] = (modes[n] * im).reshape((-1, 3))
    for i, pos in enumerate(atoms.positions):
        fd.write('%2s %12.5f %12.5f %12.5f %12.5f %12.5f %12.5f \n' %
                 (symbols[i], pos[0], pos[1], pos[2],
                  mode[i, 0], mode[i, 1], mode[i, 2]))
fd.close()
