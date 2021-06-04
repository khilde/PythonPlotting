from ROOT import *
import sys

if (len(sys.argv) < 2) :
    print "need to provide a file name"
    exit(1)
    
fileName=sys.argv[1]

openedFile=open(fileName,'r')

lines=openedFile.readlines()
graphs=[]
oneGraph= TGraph()
#count number of tgraphs
counter=0
#count number of lines read
counterLinesRead=0
for line in lines:
    #print line[0]
    #print line
    tokens=line.split("(")
    #print tokens[0]
    #print tokens[1]
    #print tokens[2]
    if (int(tokens[0].strip())==0 and counterLinesRead!=0):
        theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
        oneGraph.GetYaxis().SetRangeUser(-.05,.05);
        oneGraph.GetXaxis().SetLimits(-.05,.05);
        oneGraph.SetMarkerStyle(8)
        oneGraph.SetTitle("theTitle")
        oneGraph.Draw("AP")   
        #theCanvas.Print("temp%d.pdf"%counter)
        theCanvas.SaveAs("temp%d.png"%counter)
        print "hi"
        theCanvas.Clear()
        oneGraph= TGraph()
        counter+=1
    counterLinesRead+=1
    #tokens[2]=tokens[2].strip(')')
    tokens[2]=tokens[2].strip().strip(')')
    #parameters[0-5]=(x,px,y,py,z,pz)
    #parameters[0]=x
    #parameters[1]=px
    #parameters[2]=y
    #parameters[3]=py
    #parameters[4]=z
    #parameters[5]=pz
    parameters=tokens[2].split(',')
    #print tokens[2]
    oneGraph.SetPoint(oneGraph.GetN(),float(parameters[0]),float(parameters[2]))
        
if (False):        
    theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
    oneGraph.SetTitle("theTitle")
    oneGraph.Draw("AP")   
    theCanvas.Print("temp%d.png"%counter)
    print "hi"
    theCanvas.Clear()
    oneGraph= TGraph()
