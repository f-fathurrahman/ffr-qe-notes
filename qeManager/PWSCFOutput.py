from __future__ import print_function

class PWSCFOutput:

    def __init__(self, fname):
        self.filename = fname
        self.file = open(fname, 'r')

    def parse(self):
        f = self.file
        line = f.readline()
        while line:
            if 'Program PWSCF' in line:
                version = 
            line = f.readline()

    def close(self):
        self.file.close()
