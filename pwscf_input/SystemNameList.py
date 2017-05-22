import numpy as np

class SystemNameList:

    """
    Atomic structures will be specified using in CELL_PARAMETERS.
    """
    def __init__(self, atoms, ntyp):

        self.ibrav = 0
        self.celldm = None
        self.A = None
        self.B = None
        self.C = None
        self.cosAB = None
        self.cosAC = None
        self.cosBC = None
        self.nat = len(atoms)

        ntyp = len( np.unique( atoms.get_atomic_numbers() ) )

        nbnd =
        tot_charge
        tot_magnetization
        starting_magnetization
        ecutwfc
        ecutrho
        ecutfock
        nr1
        nr2
        nr3
        nr1s
        nr2s
        nr3s
        nosym
        nosym_evc
        noinv | no_t_rev | force_symmorphic | use_all_frac | occupations | one_atom_occupations | starting_spin_angle | degauss | smearing | nspin | noncolin | ecfixed | qcutz | q2sigma | input_dft | exx_fraction | screening_parameter | exxdiv_treatment | x_gamma_extrapolation | ecutvcut | nqx1 | nqx2 | nqx3 | lda_plus_u | lda_plus_u_kind | Hubbard_U | Hubbard_J0 | Hubbard_alpha | Hubbard_beta | Hubbard_J(i,ityp) | starting_ns_eigenvalue(m,ispin,I) | U_projection_type | edir | emaxpos | eopreg | eamp | angle1 | angle2 | constrained_magnetization | fixed_magnetization | lambda | report | lspinorb | assume_isolated | esm_bc | esm_w | esm_efield | esm_nfit | fcp_mu | vdw_corr | london | london_s6 | london_c6 | london_rvdw | london_rcut | ts_vdw_econv_thr | ts_vdw_isolated | xdm | xdm_a1 | xdm_a2 | space_group | uniqueb | origin_choice | rhombohedral | zmon | realxz | block | block_1 | block_2 | block_height

    def write(self, f):
        f.write()
        pass
