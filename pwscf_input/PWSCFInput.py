
# A simple Python class to write PWSCF input

class PWSCFInput:

    def __init__(self):

        self.CONTROL = ControlNamelist()

        self.SYSTEM = SystemNameList()

        self.ELECTRONS = ElectronsNameList('ELECTRONS')

        self.IONS = IonsNameList('IONS')

        self.ATOMIC_SPECIES = AtomicSpeciesCard( Atoms )

        self.ATOMIC_POSITIONS = AtomicPositionCard( Atoms )

        self.K_POINTS = KPointsCard( ksampling, ktype )

    def write(self):
        # write to file
        pass
