# Exact-exchange calculation (PBE0) for Si crystal

This calculation is taken from the official QE `Example`.

The following input variables in `SYSTEM` namelist are used

```
input_dft = 'pbe0'
nqx1 = 1
nqx2 = 1
nqx3 = 1
exxdiv_treatment='gygi-baldereschi'
ecutvcut = 0.7
x_gamma_extrapolation = .TRUE.
```

## Varying value of `nqx1`, `nqx2`, and `nqx3`

Using value of 1, 2, and 4.

Using value of 3 will give error. Need to read the original paper
of Gygi-Baldereschi to figure out why this is so.
