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

def theDeriv(x,par):
    theFit2= TF1("theFit2","-[3]*exp(-x*([0]/.0254*x*(x<.0254)+[0]*(x>=.0254))/(2.47*10^-6)*exp(-4.49*10^9/([1]*[2]*299792458*([0]/.0254*x*(x<.0254)+[0]*(x>=.0254)))))",0,.0254)
    theFit2.FixParameter(0,1.2)
    theFit2.FixParameter(1,2.065789)
    theFit2.FixParameter(2,0.875026)
    #theFit.SetParameter(3,10000*dipoleLength)
    theFit2.FixParameter(3,1)    
    #print theFit2.Derivative(x[0])
    return par[0]*theFit2.Derivative(x[0])
def theDeriv2(x,par):
    theFit2= TF1("theFit2","-[3]*exp(-x*((([0]-[4])/.03*x+[4])*(x<.03)+[0]*(x>=.03))/(2.47*10^-6)*exp(-4.49*10^9/([1]*[2]*299792458*((([0]-[4])/.03*x+[4])*(x<.03)+[0]*(x>=.03)))))",0,.03)
    theFit2.FixParameter(0,1.3)
    theFit2.FixParameter(4,.1)
    theFit2.FixParameter(1,2.065789)
    theFit2.FixParameter(2,0.875026)
    #theFit.SetParameter(3,10000*dipoleLength)
    theFit2.FixParameter(3,1)    
    #print theFit2.Derivative(x)
    return par[0]*theFit2.Derivative(x[0])
dipoleLength=0.03*2
cutLength=.03
#dipoleLength=1
nBins=100



openedFile=open("firstChicaneLength.txt",'r')
#openedFile=open("randomFirst.txt",'r')
openedFile2=open("firstChicaneLengthInfo.txt",'w')
#stops each canvas from being physically drawn
gROOT.SetBatch(True)

lines=openedFile.readlines()
oneHisto= TH1F("firstChicane","first chicane",nBins,0,dipoleLength)
counter=0
for line in lines:
    oneHisto.Fill(float(line))
    counter=counter+1
openedFile2.write("{")  
for i in range(oneHisto.GetNbinsX()):
    openedFile2.write("{%f,%f},"%(oneHisto.GetBinLowEdge(i+1),oneHisto.GetBinContent(i+1)))
openedFile2.write("}")
openedFile2.close()
print "number Of particles= %d" %counter 
#[0] is mangetic field
#[1] is gamma
#[2] is beta
#[3] is normalization, ie number of particles
#theFit= TF1("thefit","[3]*exp(-x*[0]/(2.47*10^-6)*exp(-4.49*10^9/([1]*[2]*299792458*[0])))",0,.0254)
theFit= TF1("theFit","[3]*exp(-x*([0]/.0254*x*(x<.0254)+[0]*(x>=.0254))/(2.47*10^-6)*exp(-4.49*10^9/([1]*[2]*299792458*([0]/.0254*x*(x<.0254)+[0]*(x>=.0254)))))",0,.03)
#theDer= TF1("theDer",theFit.Derivative(x),0,.0254)
theDer= TF1("theDer",theDeriv2,0,.03,1)
theDer.SetParameter(0, counter*cutLength/nBins);
print counter*cutLength/nBins
theFit.FixParameter(0,1.2)
theFit.FixParameter(1,2.065789)
theFit.FixParameter(2,0.875026)
#theFit.SetParameter(3,10000*dipoleLength)
theFit.SetParameter(3,1)
#theFit.SetParameter(3,10000*dipoleLength)
#still need to print last graph
theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
#oneGraph.GetYaxis().SetRangeUser(args.ymin,args.ymax);
#oneGraph.GetXaxis().SetLimits(args.xmin,args.xmax);
#oneGraph.SetMarkerStyle(args.markerStyle)
#oneGraph.SetMarkerSize(args.markerSize)
#oneGraph.SetTitle("theTitle")
oneHisto.Draw("Histo")  
#oneHisto.Fit(theDer)
#theFit.Draw("same")
#theDer.Draw("same")
theCanvas.Print("firstChicaneLength.png")
#theCanvas.Print("randomFirst.png")
theCanvas.Clear()

theFile=TFile("firstChangeLength.root","RECREATE")
#theFile=TFile("randomFirst.root","RECREATE")
oneHisto.Write()
theFile.Close()


f = TFile("my_tree.root", "RECREATE")
tree = TTree("valid", "An Example Tree")

angle = array('f', [0.])
offset = array('f', [0.])
length = array('f', [0.])

tree.Branch("angle", angle, 'angle/F')
tree.Branch("offset", offset,'offset/F')
tree.Branch("length", length, 'length/F')

openedFile.close()
openedFile=open("InjectBeam/firstChicaneL_A_D_1626463039.txt",'r')

lines=openedFile.readlines()
for line in lines:
    tokens=line.split(",")
    length[0]=float(tokens[0])
    angle[0]=float(tokens[1])
    offset[0]=float(tokens[2])
    tree.Fill()
f.Write()
f.Close()
    
