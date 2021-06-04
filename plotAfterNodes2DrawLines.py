from ROOT import *
import sys
import os, argparse
import signal
#python plotAfterNodes2DrawLines.py --fileName "print_beg.txt" --xmin -.015 --xmax .015 --ymin -.015 --ymax .015 --directory "test_print_beg" 

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def aBox(x1,y1,x2,y2):
    theLines=[TLine(x1,y1,x2,y1),TLine(x1,y2,x2,y2),TLine(x1,y1,x1,y2),TLine(x2,y1,x2,y2)]
    for theLine in theLines:
        theLine.SetNDC()
        theLine.Draw("same")
    return theLines
    
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#parser.add_argument("--directory", dest='directory', default="/share/t3data3/khildebr/RandomConeV204MC/", help="Path to the input directory")
parser.add_argument("--fileName", dest='fileName', default="output5.txt", help="Input File to read")
#parser.add_argument("--totalTGraph", type=int, dest='totalTGraph', default=-1, help="the number of tgraphs to include in total tgraph")
parser.add_argument("--totalTGraph", type=int, dest='totalTGraph', default=0, help="the number of tgraphs to include in total tgraph")
parser.add_argument("--xmin", type=float, dest='xmin', default=-.065, help="xmin for tgraph")
parser.add_argument("--xmax", type=float, dest='xmax', default=.065, help="xmax for tgraph")
parser.add_argument("--ymin", type=float, dest='ymin', default=-.065, help="ymin for tgraph")
parser.add_argument("--ymax", type=float, dest='ymax', default=.065, help="ymax for tgraph")
parser.add_argument("--xaxis", type=int, dest='xaxis', default=0, help="what to plot on xaxis for tgraph. Options are [0-6]=(x,px,y,py,z,pz,s)")
parser.add_argument("--yaxis", type=int, dest='yaxis', default=2, help="what to plot on yaxis for tgraph. Options are [0-6]=(x,px,y,py,z,pz,s)")
parser.add_argument("--directory", dest='directory', default="output5", help="directory to put graphs into")
parser.add_argument("--imageType", dest='imageType', default="png", help="what file type to save image as (ie png)")
#parser.add_argument("--markerSize",type=float, dest='markerSize', default="1", help="size of markers in graph")
parser.add_argument("--markerSize",type=float, dest='markerSize', default=".25", help="size of markers in graph")
parser.add_argument("--markerStyle",type=int, dest='markerStyle', default="8", help="style of markers in graph")
parser.add_argument("--drawLine", type=int, dest='drawLine', default=0, help="which section of graphic we are in")
parser.add_argument("--doAfterStrip", type=bool, dest='doAfterStrip', default=False, help="whether this is right after stripping")
parser.add_argument("--rangeWindowX", type=float, dest='rangeWindowX', default=-1, help="What the range in xaxis is, negative means use custom")
parser.add_argument("--rangeWindowY", type=float, dest='rangeWindowY', default=-1, help="What the range in yaxis is, negative means use custom")
args = parser.parse_args()

#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3, end of chicane 3,
drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042]


doAll=True
numberToDo=-1
if (args.totalTGraph>0):
    doAll=False
    numberToDo=args.totalTGraph
    
#fileName=sys.argv[1]
if not os.path.isdir(args.directory):
    os.mkdir(args.directory)
    #print("%s directory does not exist"%(args.directory))
    #sys.exit(0)
theNaming=["X","PX","Y","PY","Z","PZ","S"]
theNamingWithUnits=["X (m)","PX (rad)","Y (m)","PY (rad)","Z (m)","PZ (GeV)","S (m)"]
theXAxisVariable=theNaming[args.xaxis]
theYAxisVariable=theNaming[args.yaxis]
if not os.path.isdir("%s/%svs%s"%(args.directory,theXAxisVariable,theYAxisVariable)):
    os.mkdir(("%s/%svs%s"%(args.directory,theXAxisVariable,theYAxisVariable)))
openedFile=open(args.fileName,'r')

#stops each canvas from being physically drawn
gROOT.SetBatch(True)

lines=openedFile.readlines()
graphs=[]
oneGraph= TGraph()
totalGraph=TGraph()
#count number of tgraphs
counter=0
#count number of lines read
counterLinesRead=0
bigNumber=10000000
xMin=bigNumber
xMax=-bigNumber
yMin=bigNumber
yMax=-bigNumber
for line in lines:
    #print line[0]
    #print line
    tokens=line.split("(")
    #print tokens[0]
    #print tokens[1]
    #print tokens[2]
    if (int(tokens[0].strip())==0 and counterLinesRead!=0):
        theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
        theCanvas.SetLeftMargin(0.15);
        theCanvas.SetBottomMargin(0.25);
        oneGraph.GetYaxis().SetRangeUser(args.ymin,args.ymax);
        oneGraph.GetXaxis().SetLimits(args.xmin,args.xmax);
        oneGraph.SetMarkerStyle(args.markerStyle)
        oneGraph.SetMarkerSize(args.markerSize)
        oneGraph.SetTitle("turn %s"%counter)
        oneGraph.GetXaxis().SetTitle(theNamingWithUnits[args.xaxis])
        oneGraph.GetYaxis().SetTitle(theNamingWithUnits[args.yaxis])
        oneGraph.Draw("AP")   
        theCanvas.Print("%s/%svs%s/temp%d.%s"%(args.directory,theXAxisVariable,theYAxisVariable,counter,args.imageType))
        #theCanvas.SaveAs("temp%d.png"%counter)
        theCanvas.Clear()
        oneGraph= TGraph()
        counter+=1
        xMin=bigNumber
        xMax=-bigNumber
        yMin=bigNumber
        yMax=-bigNumber        
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
    oneGraph.SetPoint(oneGraph.GetN(),float(parameters[args.xaxis]),float(parameters[args.yaxis]))
    if float(parameters[args.xaxis]) <xMin:
        xMin=float(parameters[args.xaxis])
    if float(parameters[args.xaxis]) >xMax:
        xMax=float(parameters[args.xaxis])
    if float(parameters[args.yaxis]) <yMin:
        yMin=float(parameters[args.yaxis])
    if float(parameters[args.yaxis]) >yMax:
        yMax=float(parameters[args.yaxis]) 
        
    if (doAll==True or numberToDo>counter):
        totalGraph.SetPoint(totalGraph.GetN(),float(parameters[args.xaxis]),float(parameters[args.yaxis]))

#still need to print last graph
theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
theCanvas.SetLeftMargin(0.15);
theCanvas.SetBottomMargin(0.25);
if args.rangeWindowX >0:
    if args.rangeWindowX <xMax-xMin:
        print "warning rangeWindowX=%f but xMax-xMin=%f\n"%(args.rangeWindowX,xMax-xMin)
        oneGraph.GetXaxis().SetLimits(xMin,xMax)
    else:
        theNumber=(args.rangeWindowX-(xMax-xMin))/2.
        oneGraph.GetXaxis().SetLimits(xMin-theNumber,xMax+theNumber)
else:
    oneGraph.GetXaxis().SetLimits(args.xmin,args.xmax);
    
if args.rangeWindowY >0:
    if args.rangeWindowY <yMax-yMin:
        print "warning rangeWindowY=%f but yMax-yMin=%f\n"%(args.rangeWindowY,yMax-yMin)
        oneGraph.GetYaxis().SetRangeUser(yMin,yMax)
    else:
        theNumber=(args.rangeWindowY-(yMax-yMin))/2.
        oneGraph.GetYaxis().SetRangeUser(yMin-theNumber,yMax+theNumber)
else:
    oneGraph.GetYaxis().SetRangeUser(args.ymin,args.ymax)  

oneGraph.SetMarkerStyle(args.markerStyle)
oneGraph.SetMarkerSize(args.markerSize)
oneGraph.SetTitle("turn %s"%counter)
oneGraph.GetXaxis().SetTitle(theNamingWithUnits[args.xaxis])
oneGraph.GetYaxis().SetTitle(theNamingWithUnits[args.yaxis])
oneGraph.Draw("AP")   
#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3,beginning of stripping 2, end of chicane 3,
#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042]
Length=drawingArray[6]
midLine=.1
stripLength=.06

drift1=TLine(0,midLine,drawingArray[1]/Length,midLine)
#print "%f"%drift1.GetX2()
chicane2=aBox(drawingArray[1]/Length,midLine/2.,drawingArray[3]/Length,midLine*3./2.)
#chicane2a=TLine(drawingArray[1]/Length,midLine/2.,drawingArray[3]/Length,midLine*3./2.)
#chicane2=TBox(drawingArray[1]/Length*500,midLine/2.*500,drawingArray[3]/Length*500,midLine*3./2.*500)
stripping1=aBox(drawingArray[2]/Length,midLine/1.5,(drawingArray[2]+stripLength)/Length,midLine*2./1.5)
drift2=TLine(drawingArray[3]/Length,midLine,drawingArray[4]/Length,midLine)
chicane3=aBox(drawingArray[4]/Length,midLine/2.,drawingArray[6]/Length,midLine*3./2.)
stripping2=aBox(drawingArray[5]/Length,midLine/1.5,(drawingArray[5]+stripLength)/Length,midLine*2./1.5)

#where to draw red line
afterStrip=0;
theDrawLine=args.drawLine
if args.doAfterStrip:
    afterStrip=stripLength/Length
    
if "print_beg.txt" in args.fileName:
    theDrawLine=0
elif "print_beg_DH11.txt" in args.fileName:
    theDrawLine=1
elif "print_DH11_3pre.txt" in args.fileName:
    theDrawLine=2
elif "print_DH11_3.txt" in args.fileName:
    theDrawLine=2   
    afterStrip=stripLength/Length    
elif "print_beg_b23.txt" in args.fileName:
    theDrawLine=3   
elif "print_beg_DH12.txt" in args.fileName:
    theDrawLine=4   
elif "print_DH12_3pre.txt" in args.fileName:
    theDrawLine=5
elif "print_DH12_3.txt" in args.fileName:
    theDrawLine=5
    afterStrip=stripLength/Length 
elif "print_end_DH12.txt" in args.fileName:
    theDrawLine=6
markerLine=TLine(drawingArray[theDrawLine]/Length+afterStrip,0,drawingArray[theDrawLine]/Length+afterStrip,.17)

drift1.SetNDC()
#chicane2.SetNDC()
#stripping1.SetNDC()
drift2.SetNDC()
#chicane3.SetNDC()
#stripping2.SetNDC()
markerLine.SetNDC()
markerLine.SetLineWidth(2)
markerLine.SetLineColor(kRed)

drift1.Draw("same")
#chicane2.Draw("same")
#stripping1.Draw("same")
drift2.Draw("same")
#chicane3.Draw("same")
#stripping2.Draw("same")

markerLine.Draw("same")
oneGraph.SetTitle("s= %f"%(drawingArray[theDrawLine]+afterStrip*Length))
theCanvas.Print("%s/%svs%s_%s.%s"%(args.directory.split("/")[0],theXAxisVariable,theYAxisVariable,args.directory.split("/")[1],args.imageType))
#theCanvas.Print("%s/%svs%s/temp%d.%s"%(args.directory,theXAxisVariable,theYAxisVariable,counter,args.imageType))
#theCanvas.SaveAs("temp%d.png"%counter)
theCanvas.Clear()
oneGraph= TGraph()
counter+=1

#save totalgraph
theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
totalGraph.GetYaxis().SetRangeUser(args.ymin,args.ymax);
totalGraph.GetXaxis().SetLimits(args.xmin,args.xmax);
totalGraph.SetMarkerStyle(args.markerStyle)
totalGraph.SetMarkerSize(args.markerSize)
totalGraph.SetTitle("theTitle")
totalGraph.Draw("AP")   
theCanvas.Print("%s/%svs%s/aTotal%d.%s"%(args.directory,theXAxisVariable,theYAxisVariable,counter,args.imageType))
#theCanvas.SaveAs("temp%d.png"%counter)
theCanvas.Clear()
totalGraph= TGraph()
