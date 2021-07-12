from ROOT import *
import sys
import os, argparse
import signal
from array import array

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

f = TFile("my_treePrintNode.root", "RECREATE")
tree = TTree("valid", "An Example Tree")

x = array('f', [0.])
px = array('f', [0.])
y = array('f', [0.])
py = array('f', [0.])
z = array('f', [0.])
pz = array('f', [0.])


tree.Branch("x", x, 'x/F')
tree.Branch("px", px, 'px/F')
tree.Branch("y", y, 'y/F')
tree.Branch("py", py, 'py/F')
tree.Branch("z", z, 'z/F')
tree.Branch("pz", pz, 'pz/F')

openedFile=open("print_beg_0.txt",'r')

lines=openedFile.readlines()
for line in lines:
    tokens1=line.split("=")
    tokens=tokens1[1].split(",")
    #print tokens[0].strip().strip("(")
    x[0]=float(tokens[0].strip().strip("("))
    px[0]=float(tokens[1])
    y[0]=float(tokens[2])
    py[0]=float(tokens[3])
    z[0]=float(tokens[4])
    pz[0]=float(tokens[5])    
    tree.Fill()
f.Write()
f.Close()
    
