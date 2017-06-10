import numpy as np

class SystemNameList:

    """
    Atomic structures will be specified using in CELL_PARAMETERS.
    """
    def __init__(self, atoms):

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

        nbnd = None
        tot_charge = None
        tot_magnetization = None
        starting_magnetization = None
        ecutwfc = 30.0
        ecutrho = 4.*ecutwfc
        ecutfock = None
        nr1 = None
        nr2 = None
        nr3 = None
        nr1s = None
        nr2s = None
        nr3s = None
        nosym = None
        nosym_evc = None
        """
        noinv | no_t_rev | force_symmorphic | use_all_frac | occupations | one_atom_occupations |
        starting_spin_angle | degauss | smearing | nspin | noncolin | ecfixed | qcutz | q2sigma |
        input_dft | exx_fraction | screening_parameter | exxdiv_treatment | x_gamma_extrapolation |
        ecutvcut | nqx1 | nqx2 | nqx3 | lda_plus_u | lda_plus_u_kind | Hubbard_U | Hubbard_J0 |
        Hubbard_alpha | Hubbard_beta | Hubbard_J(i,ityp) | starting_ns_eigenvalue(m,ispin,I) |
        U_projection_type | edir | emaxpos | eopreg | eamp | angle1 | angle2 | constrained_magnetization
        | fixed_magnetization | lambda | report | lspinorb | assume_isolated | esm_bc | esm_w |
        esm_efield | esm_nfit | fcp_mu | vdw_corr | london | london_s6 | london_c6 | london_rvdw |
        london_rcut | ts_vdw_econv_thr | ts_vdw_isolated | xdm | xdm_a1 | xdm_a2 | space_group | uniqueb
        | origin_choice | rhombohedral | zmon | realxz | block | block_1 | block_2 | block_height
        """

    def write(self, f=None):
        import sys
        if f == None:
            f = sys.stdout
        f.write('Hello\n')
        f.write('nat = %d\n' % self.nat)
        #
        if( f != sys.stdout ):
            f.close()
