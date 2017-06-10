import sys

class ControlNameList:

    """
    Values equal to `None` will not be written in the input file.
    """
    def __init__(self):

        self.calculation = 'scf'
        self.nstep = 1000
        self.tprnfor = True
        self.outdir = './tmp'
        self.prefix = 'pwscf'

        self.title = None
        self.verbosity = None
        self.restart_mode = None
        self.wf_collect = None
        self.iprint = None
        self.tstress = None
        self.dt = None
        self.wfcdir = None
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


    def write(self,f=None):
        if f == None:
            f = sys.stdout
        #
        f.write('&CONTROL\n')
        f.write('  prefix = \'%s\'\n' % self.prefix)
        f.write('  outdir = \'%s\'\'\n' % self.outdir)
        f.write('  pseudo_dir = \'%s\'\n' % self.outdir)
        f.write('  tprnfor = %s\n' % self.tprnfor)
        f.write('  nstep = %d\n' % self.nstep)
        f.write('/\n\n')
        #
        if( f != sys.stdout ):
            f.close()
