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
parser.add_argument("--directoryClosed", dest='directoryClosed', default="output5", help="directory to put graphs into")
parser.add_argument("--imageType", dest='imageType', default="png", help="what file type to save image as (ie png)")
#parser.add_argument("--markerSize",type=float, dest='markerSize', default="1", help="size of markers in graph")
parser.add_argument("--markerSize",type=float, dest='markerSize', default=".25", help="size of markers in graph")
parser.add_argument("--markerStyle",type=int, dest='markerStyle', default="8", help="style of markers in graph")
parser.add_argument("--drawLine", type=int, dest='drawLine', default=0, help="which section of graphic we are in")
parser.add_argument("--stripper1Location", type=int, dest='stripper1Location', default=0, help="what slot stripper 1 magnet is in")
parser.add_argument("--doAfterStrip", type=bool, dest='doAfterStrip', default=False, help="whether this is right after stripping")
parser.add_argument("--rangeWindowX", type=float, dest='rangeWindowX', default=-1, help="What the range in xaxis is, negative means use custom")
parser.add_argument("--rangeWindowY", type=float, dest='rangeWindowY', default=-1, help="What the range in yaxis is, negative means use custom")
args = parser.parse_args()

#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3, end of chicane 3,begginning of chicane 4, end of chicane 4

#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042,5.35030,6.24055]
drawingArray=[]
prefixFileName="emmit"
stripper1CurrentLocation=args.stripper1Location
fileNameArray=["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_beg_b23_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
coordinateArray=[]
coordinateArrayClosed=[]
theDirectory=args.directory
theDirectoryClosed=args.directoryClosed

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
	#stops each canvas from being physically drawn
gROOT.SetBatch(True)    
#build drawing array for closed Orbit
for currentFileName in fileNameArray:
	print "%s/%s%s%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation)
	openedFile=open("%s/%s%s%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation),'r')



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
	firstLine=True
	sCoord="hi"
	xCoord="hi2"
	for line in lines:
	    #print line[0]
	    #print line

	    if firstLine:
	    	firstLine=False
	    	tokens=line.strip().split(" ")
	    	#print "%s"%tokens
	    	print "len(tokens)=%d"%len(tokens)
	    	sCoord="hi"
	    	sCoord=tokens[len(tokens)-1]
	    	print "%s"%sCoord

	    
	    if "x avg" in line:
	    	tokens=line.split("=")
	    	token=tokens[1]
	    	print "token=%s"%token
	    	token=token.split(",")[0].strip().strip("(")
	    	print "token=%s"%token
	    	xCoord="hi2"
	    	xCoord=token
	coordinateArrayClosed.append([float(xCoord),float(sCoord)])

#build drawing array
for currentFileName in fileNameArray:
	print "%s/%s%s%d.txt"%(theDirectory,prefixFileName,currentFileName,stripper1CurrentLocation)
	openedFile=open("%s/%s%s%d.txt"%(theDirectory,prefixFileName,currentFileName,stripper1CurrentLocation),'r')



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
	firstLine=True
	sCoord="hi"
	xCoord="hi2"
	for line in lines:
	    #print line[0]
	    #print line

	    if firstLine:
	    	firstLine=False
	    	tokens=line.strip().split(" ")
	    	#print "%s"%tokens
	    	print "len(tokens)=%d"%len(tokens)
	    	sCoord="hi"
	    	sCoord=tokens[len(tokens)-1]
	    	print "%s"%sCoord
	    	if "postS" not in currentFileName:
	    		drawingArray.append(float(sCoord))
	    
	    if "x avg" in line:
	    	tokens=line.split("=")
	    	token=tokens[1]
	    	print "token=%s"%token
	    	token=token.split(",")[0].strip().strip("(")
	    	print "token=%s"%token
	    	xCoord="hi2"
	    	xCoord=token
	coordinateArray.append([float(xCoord),float(sCoord)])
	
	    	
print coordinateArray	    	
theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
theCanvas.SetLeftMargin(0.15);
theCanvas.SetBottomMargin(0.25);	    
#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3,beginning of stripping2, end of chicane 3,begginning of chicane 4, end of chicane 4
#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042,5.35030,6.24055]
Length=drawingArray[9]
midLine=.1
stripLength=.06

drift1=TLine(0,midLine,drawingArray[1]/Length,midLine)
drift1.SetNDC()
drift1.Draw()
#print "%f"%drift1.GetX2()
chicane2=aBox(drawingArray[1]/Length,midLine/2.,drawingArray[3]/Length,midLine*3./2.)
#chicane2a=TLine(drawingArray[1]/Length,midLine/2.,drawingArray[3]/Length,midLine*3./2.)
#chicane2=TBox(drawingArray[1]/Length*500,midLine/2.*500,drawingArray[3]/Length*500,midLine*3./2.*500)
#stripping1=aBox(drawingArray[2]/Length,midLine/1.5,(drawingArray[2]+stripLength)/Length,midLine*2./1.5)
stripping1=aBox(float(coordinateArray[2][1])/Length,midLine/1.5,(float(coordinateArray[2][1])+stripLength)/Length,midLine*2./1.5)
drift2=TLine(drawingArray[3]/Length,midLine,drawingArray[4]/Length,midLine)
chicane3=aBox(drawingArray[4]/Length,midLine/2.,drawingArray[6]/Length,midLine*3./2.)
stripping2=aBox(drawingArray[5]/Length,midLine/1.5,(drawingArray[5]+stripLength)/Length,midLine*2./1.5)
drift3=TLine(drawingArray[6]/Length,midLine,drawingArray[7]/Length,midLine)
chicane4=aBox(drawingArray[7]/Length,midLine/2.,drawingArray[8]/Length,midLine*3./2.)
foil2=TLine(drawingArray[7]/Length,midLine*.4,drawingArray[7]/Length,midLine*1.6)
drift4=TLine(drawingArray[8]/Length,midLine,drawingArray[9]/Length,midLine)


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


#chicane2.SetNDC()
#stripping1.SetNDC()
drift2.SetNDC()
#chicane3.SetNDC()
#stripping2.SetNDC()
drift3.SetNDC()
drift4.SetNDC()
foil2.SetNDC()
markerLine.SetNDC()
markerLine.SetLineWidth(2)
markerLine.SetLineColor(kRed)
foil2.SetLineWidth(2)
foil2.SetLineColor(kBlue)



#chicane2.Draw("same")
#stripping1.Draw("same")
drift2.Draw("same")
#chicane3.Draw("same")
#stripping2.Draw("same")
drift3.Draw("same")
drift4.Draw("same")
foil2.Draw("same")

theMax=-1.
for index in range(len(coordinateArray)):
	if abs(coordinateArray[index][0])>theMax:
		theMax=abs(coordinateArray[index][0])
theMax=314
print "theMax=%d"%theMax
theOffsetForClosed=coordinateArrayClosed[0][1]-(2.24807-1.514801482455)
driftTrackArrayClosed=[]	
for index in range(len(coordinateArrayClosed)):
	print coordinateArrayClosed[index]
	
	if index!=len(coordinateArrayClosed)-1:
	#if index==5:
		driftTrack=None
		if coordinateArrayClosed[index][1]==coordinateArrayClosed[index+1][1]:
			print "1"
			firstX=1+0.5*coordinateArrayClosed[index][0]/theMax
			secondX=1+0.5*coordinateArrayClosed[index+1][0]/theMax
			driftTrack=TLine((coordinateArrayClosed[index][1]-theOffsetForClosed)/Length,midLine*firstX,((coordinateArrayClosed[index][1]-theOffsetForClosed)+stripLength)/Length,midLine*secondX)
		elif index!=0 and coordinateArrayClosed[index][1]==coordinateArrayClosed[index-1][1]:
			print "2"
			firstX=1+0.5*coordinateArrayClosed[index][0]/theMax
			secondX=1+0.5*coordinateArrayClosed[index+1][0]/theMax
			driftTrack=TLine(((coordinateArrayClosed[index][1]-theOffsetForClosed)+stripLength)/Length,midLine*firstX,(coordinateArrayClosed[index+1][1]-theOffsetForClosed)/Length,midLine*secondX)		
		else:
			print "3"
			firstX=1+0.5*coordinateArrayClosed[index][0]/theMax
			secondX=1+0.5*coordinateArrayClosed[index+1][0]/theMax
			driftTrack=TLine((coordinateArrayClosed[index][1]-theOffsetForClosed)/Length,midLine*firstX,(coordinateArrayClosed[index+1][1]-theOffsetForClosed)/Length,midLine*secondX)
		driftTrack.SetNDC()
		driftTrack.SetLineColor(kBlue)
		driftTrackArrayClosed.append(driftTrack)
		#driftTrack.Draw("same")

driftTrackArray=[]	
for index in range(len(coordinateArray)):
	print coordinateArray[index]
	
	if index!=len(coordinateArray)-1:
	#if index==5:
		driftTrack=None
		if coordinateArray[index][1]==coordinateArray[index+1][1]:
			print "1"
			firstX=1+0.5*coordinateArray[index][0]/theMax
			secondX=1+0.5*coordinateArray[index+1][0]/theMax
			driftTrack=TLine(coordinateArray[index][1]/Length,midLine*firstX,(coordinateArray[index][1]+stripLength)/Length,midLine*secondX)
		elif index!=0 and coordinateArray[index][1]==coordinateArray[index-1][1]:
			print "2"
			firstX=1+0.5*coordinateArray[index][0]/theMax
			secondX=1+0.5*coordinateArray[index+1][0]/theMax
			driftTrack=TLine((coordinateArray[index][1]+stripLength)/Length,midLine*firstX,coordinateArray[index+1][1]/Length,midLine*secondX)		
		else:
			print "3"
			firstX=1+0.5*coordinateArray[index][0]/theMax
			secondX=1+0.5*coordinateArray[index+1][0]/theMax
			driftTrack=TLine(coordinateArray[index][1]/Length,midLine*firstX,coordinateArray[index+1][1]/Length,midLine*secondX)
		driftTrack.SetNDC()
		driftTrack.SetLineColor(kRed)
		driftTrackArray.append(driftTrack)
		#driftTrack.Draw("same")
				
septumAngle=3*TMath.Pi()/180.
#m
septumStart=.113
septumWidth=.2762
#mm
#septumStart=113
#septumWidth=276.2
wasteSeptum=TLine(drawingArray[9]/Length,midLine*(1+0.5*septumStart*1000./theMax),(drawingArray[9]-TMath.Tan(septumAngle)*septumWidth)/Length,midLine*(1+0.5*(septumStart+septumWidth)*1000./theMax))
wasteSeptum.SetNDC()	
wasteSeptum.SetLineWidth(2)
wasteSeptum.SetLineColor(kGreen)
wasteSeptum.Draw("same")
for drift in driftTrackArray:
	drift.Draw("same")
for drift in driftTrackArrayClosed:
	drift.Draw("same")	
#markerLine.Draw("same")
#oneGraph.SetTitle("s= %f"%(drawingArray[theDrawLine]+afterStrip*Length))
theCanvas.Print("%s/tracking_%d.%s"%(theDirectoryClosed,stripper1CurrentLocation,args.imageType))
#theCanvas.Print("%s/%svs%s/temp%d.%s"%(args.directory,theXAxisVariable,theYAxisVariable,counter,args.imageType))
#theCanvas.SaveAs("temp%d.png"%counter)
theCanvas.Clear()
oneGraph= TGraph()
counter+=1

print coordinateArray	

print coordinateArrayClosed
