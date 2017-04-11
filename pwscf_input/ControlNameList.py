class ControlNameList:

    """
    Values equal to `None` will not be written in the input file.
    """
    def __init__(self):

        self.calculation = 'scf'
        self.nstep = 1000
        self.tprnfor = True
        self.outdir = './tmp'

        self.title = None
        self.verbosity = None
        self.restart_mode = None
        self.wf_collect = None
        self.iprint = None
        self.tstress = None
        self.dt = None
        self.wfcdir = None
        self.prefix = None
        self.lkpoint_dir = None
        self.max_seconds = None
        self.etot_conv_thr = None
        self.forc_conv_thr = None
        self.disk_io = None
        self.pseudo_dir = None
        self.tefield = None
        self.dipfield = None
        self.lelfield = None
        self.nberrycyc = None
        self.lorbm = None
        self.lberry = None
        self.gdir = None
        self.nppstr = None
        self.lfcpopt = None
        self.monopole = None


    def write_line(file):
        #file.write()
        pass

if __main__:
