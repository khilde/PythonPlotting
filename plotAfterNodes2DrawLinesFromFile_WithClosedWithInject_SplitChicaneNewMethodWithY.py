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
parser.add_argument("--directoryRing", dest='directoryRing', default="output5", help="directory to put graphs into")
parser.add_argument("--imageType", dest='imageType', default="png", help="what file type to save image as (ie png)")
#parser.add_argument("--markerSize",type=float, dest='markerSize', default="1", help="size of markers in graph")
parser.add_argument("--markerSize",type=float, dest='markerSize', default=".25", help="size of markers in graph")
parser.add_argument("--markerStyle",type=int, dest='markerStyle', default="8", help="style of markers in graph")
parser.add_argument("--drawLine", type=int, dest='drawLine', default=0, help="which section of graphic we are in")
parser.add_argument("--stripper1Location", type=int, dest='stripper1Location', default=0, help="what slot stripper 1 magnet is in")
parser.add_argument("--stripper2Location", type=int, dest='stripper2Location', default=0, help="what slot stripper 2 magnet is in")
parser.add_argument("--stripper1LocationMax", type=int, dest='stripper1LocationMax', default=0, help="Max NParts for stripper 1")
parser.add_argument("--stripper2LocationMax", type=int, dest='stripper2LocationMax', default=0, help="Max NParts for stripper 2")
parser.add_argument("--doAfterStrip", type=bool, dest='doAfterStrip', default=False, help="whether this is right after stripping")
parser.add_argument("--rangeWindowX", type=float, dest='rangeWindowX', default=-1, help="What the range in xaxis is, negative means use custom")
parser.add_argument("--rangeWindowY", type=float, dest='rangeWindowY', default=-1, help="What the range in yaxis is, negative means use custom")
parser.add_argument("--doY", type=int, dest='doY', default=0, help="Draw Y if positive")
args = parser.parse_args()
#stripper2CurrentLocation=5
#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3, end of chicane 3,begginning of chicane 4, end of chicane 4

#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042,5.35030,6.24055]
drawingArray=["_beg_","_beg_DH11_","_end_DH11_","_DH11_3pre_","_postS_DH11_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
prefixFileName="emmit"
stripper1CurrentLocation=args.stripper1Location
stripper2CurrentLocation=args.stripper2Location
stripper1Max=args.stripper1LocationMax
stripper2Max=args.stripper2LocationMax
#fileNameArray=["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_beg_b23_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
fileNameArray=["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_end_DH11_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
#coordinateArray sorts them based on file name array
#trackingArray just contains all of em
coordinateArray={}
coordinateArrayClosed={}
coordinateArrayRing={}
trackingArray=[]
trackingArrayClosed=[]
trackingArrayRing=[]
theDirectory=args.directory
theDirectoryClosed=args.directoryClosed
theDirectoryRing=args.directoryRing

doAll=True
doY=False
if args.doY >0 :
	doY=True
tokenToFind="x avg"
positionTokenToFind=0
if doY:
	tokenToFind="y avg"
	positionTokenToFind=1
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
#build drawing array for injected orbit into ring
for currentFileName in fileNameArray:
	#print "%s/%s%s%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation)
	openedFile=open("%s/%s%s%d_%d_%d_%d.txt"%(theDirectoryRing,prefixFileName,currentFileName,stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max),'r')



	lines=openedFile.readlines()
	coords=[]
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

	    #if line.find("myEmitNode")>0:
	    if 'myEmitNode' in line or 'MyEmitNode' in line:
	    	#print "here we go"
	    	firstLine=False
	    	tokens=line.strip().split(" ")
	    	#print "%s"%tokens
	    	#print "len(tokens)=%d"%len(tokens)
	    	sCoord="hi"
	    	sCoord=tokens[len(tokens)-1]
	    	#print "%s"%sCoord

	    #print tokenToFind
	    if tokenToFind in line and "twiss" not in line:
	    	tokens=line.split("=")
	    	token=tokens[1]
	    	#print "token=%s"%token
	    	token=token.split(",")[positionTokenToFind].strip().strip("()")
	    	#print "token=%s"%token
	    	xCoord="hi2"
	    	xCoord=token
	    	trackingArrayRing.append([float(xCoord),float(sCoord)])
		coords.append([float(xCoord),float(sCoord)])
	coordinateArrayRing[currentFileName] =coords

#sort the array
trackingArrayRing=sorted(trackingArrayRing,key=lambda x: (x[1]))
#build drawing array for closed Orbit
for currentFileName in fileNameArray:
	#print "%s/%s%s%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation)
	openedFile=open("%s/%s%s%d_%d_%d_%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max),'r')



	lines=openedFile.readlines()
	coords=[]
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

	    #if line.find("myEmitNode")>0:
	    if 'myEmitNode' in line or 'MyEmitNode' in line:
	    	#print "here we go"
	    	firstLine=False
	    	tokens=line.strip().split(" ")
	    	#print "%s"%tokens
	    	#print "len(tokens)=%d"%len(tokens)
	    	sCoord="hi"
	    	sCoord=tokens[len(tokens)-1]
	    	#print "%s"%sCoord

	    #print tokenToFind
	    if tokenToFind in line and "twiss" not in line:
	    	tokens=line.split("=")
	    	token=tokens[1]
	    	#print "token=%s"%token
	    	token=token.split(",")[positionTokenToFind].strip().strip("()")
	    	#print "token=%s"%token
	    	xCoord="hi2"
	    	xCoord=token
	    	trackingArrayClosed.append([float(xCoord),float(sCoord)])
		coords.append([float(xCoord),float(sCoord)])
	coordinateArrayClosed[currentFileName] =coords

#sort the array
trackingArrayClosed=sorted(trackingArrayClosed,key=lambda x: (x[1]))
#coordinateArrayClosed=sorted(coordinateArrayClosed,key=lambda x: (x[1]))
#print(sorted(coordinateArrayClosed,key=lambda x: (x[1])))
countChicane2=0
countChicane3=0
#build drawing array
for currentFileName in fileNameArray:
	#print "%s/%s%s%d.txt"%(theDirectory,prefixFileName,currentFileName,stripper1CurrentLocation)
	openedFile=open("%s/%s%s%d_%d_%d_%d.txt"%(theDirectory,prefixFileName,currentFileName,stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max),'r')



	lines=openedFile.readlines()
	coords=[]
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

	    if 'myEmitNode' in line or 'MyEmitNode' in line:
	    	if "beg_DH11" in line:
	    		countChicane2+=1
	    	if "beg_DH12" in line:
	    		countChicane3+=1	    		
	    	firstLine=False
	    	tokens=line.strip().split(" ")
	    	#print "%s"%tokens
	    	#print "len(tokens)=%d"%len(tokens)
	    	sCoord="hi"
	    	sCoord=tokens[len(tokens)-1]
	    	#print "%s"%sCoord
	    	#if "postS" not in currentFileName:
	    	#drawingArray.append(float(sCoord))
	    
	    if tokenToFind in line and "twiss" not in line:
	    	tokens=line.split("=")
	    	token=tokens[1]
	    	#print "token=%s"%token
	    	token=token.split(",")[positionTokenToFind].strip().strip("()")
	    	#print "token=%s"%token
	    	xCoord="hi2"
	    	xCoord=token
	    	trackingArray.append([float(xCoord),float(sCoord)])
		coords.append([float(xCoord),float(sCoord)])
	coordinateArray[currentFileName] =coords
#print "testPrint"
trackingArray=sorted(trackingArray,key=lambda x: (x[1]))
#for currentFileName in fileNameArray:
	#print "coordinateArray[",currentFileName,"]= ",coordinateArray[currentFileName] 
splitChicane2=False
splitChicane3=False	
if countChicane2 >1:
	splitChicane2=True
if countChicane3 >1:
	splitChicane3=True	
#coordinateArray=sorted(coordinateArray,key=lambda x: (x[1]))	
#drawingArray=sorted(drawingArray)	
print coordinateArray	
theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
theCanvas.SetLeftMargin(0.15);
theCanvas.SetBottomMargin(0.25);	    
#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3,beginning of stripping2, end of chicane 3,begginning of chicane 4, end of chicane 4
#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042,5.35030,6.24055]
Length=coordinateArray["_end_DB_WASTE_"][0][1]
midLine=.5
stripLength=.06
#["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_end_DH11_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]

#print "%f"%drift1.GetX2()

if stripper1CurrentLocation==0:
	drift1=TLine(0,midLine,coordinateArray["_DH11_3pre_"][0][1]/Length,midLine)
	chicane2=aBox(coordinateArray["_DH11_3pre_"][0][1]/Length,midLine/2.,coordinateArray["_end_DH11_"][0][1]/Length,midLine*3./2.)
else:
	drift1=TLine(0,midLine,coordinateArray["_beg_DH11_"][0][1]/Length,midLine)
	chicane2=aBox(coordinateArray["_beg_DH11_"][0][1]/Length,midLine/2.,coordinateArray["_end_DH11_"][len(coordinateArray["_end_DH11_"])-1][1]/Length,midLine*3./2.)

stripping1=aBox(coordinateArray["_DH11_3pre_"][0][1]/Length,midLine/1.5,coordinateArray["_postS_DH11_"][0][1]/Length,midLine*2./1.5)
begginingOfChicane3=coordinateArray["_beg_DH12_"][0][1]
if stripper2CurrentLocation==0:
	begginingOfChicane3=coordinateArray["_DH12_3pre_"][0][1]
if stripper1CurrentLocation==0 or splitChicane2:	
	drift2=TLine(coordinateArray["_end_DH11_"][len(coordinateArray["_end_DH11_"])-1][1]/Length,midLine,begginingOfChicane3/Length,midLine)
else:
	drift2=TLine(coordinateArray["_postS_DH11_"][len(coordinateArray["_end_DH11_"])-1][1]/Length,midLine,begginingOfChicane3/Length,midLine)

chicane3=aBox(begginingOfChicane3/Length,midLine/2.,coordinateArray["_end_DH12_"][len(coordinateArray["_end_DH12_"])-1][1]/Length,midLine*3./2.)
stripping2=aBox(coordinateArray["_DH12_3pre_"][0][1]/Length,midLine/1.5,coordinateArray["_postS_DH12_"][0][1]/Length,midLine*2./1.5)
if stripper2CurrentLocation==0 or splitChicane3:	
	drift3=TLine(coordinateArray["_end_DH12_"][len(coordinateArray["_end_DH12_"])-1][1]/Length,midLine,coordinateArray["_beg_DH13_"][0][1]/Length,midLine)
else:
	drift3=TLine(coordinateArray["_postS_DH12_"][len(coordinateArray["_end_DH12_"])-1][1]/Length,midLine,coordinateArray["_beg_DH13_"][0][1]/Length,midLine)

chicane4=aBox(coordinateArray["_beg_DH13_"][0][1]/Length,midLine/2.,coordinateArray["_end_DH13_"][0][1]/Length,midLine*3./2.)
foil2=TLine(coordinateArray["_beg_DH13_"][0][1]/Length,midLine*.4,coordinateArray["_beg_DH13_"][0][1]/Length,midLine*1.6)
drift4=TLine(coordinateArray["_end_DH13_"][0][1]/Length,midLine,coordinateArray["_end_DB_WASTE_"][0][1]/Length,midLine)





drift1.SetNDC()
drift1.Draw()
drift2.SetNDC()
drift3.SetNDC()
drift4.SetNDC()
foil2.SetNDC()
foil2.SetLineWidth(2)
foil2.SetLineColor(kBlue)

drift2.Draw("same")
drift3.Draw("same")
drift4.Draw("same")
foil2.Draw("same")

theMax=-1.
for element in coordinateArray:
	#print element
	for index in range(len(coordinateArray[element])):
		if abs(coordinateArray[element][index][0])>theMax:
			theMax=abs(coordinateArray[element][index][0])
print "theMax= ", theMax
theMax=314
print "theMax=%d"%theMax
theOffsetForClosed=coordinateArrayClosed["_beg_"][0][1]-(2.24807-1.514801482455)
driftTrackArrayClosed=[]	
for index in range(len(trackingArrayClosed)):
	#print trackingArrayClosed[index]
	
	if index!=len(trackingArrayClosed)-1:
	#if index==5:
		driftTrack=None
		firstX=1+0.5*trackingArrayClosed[index][0]/theMax
		secondX=1+0.5*trackingArrayClosed[index+1][0]/theMax
		driftTrack=TLine((trackingArrayClosed[index][1]-theOffsetForClosed)/Length,midLine*firstX,(trackingArrayClosed[index+1][1]-theOffsetForClosed)/Length,midLine*secondX)
		driftTrack.SetNDC()
		driftTrack.SetLineColor(kBlue)
		driftTrackArrayClosed.append(driftTrack)
		#driftTrack.Draw("same")

driftTrackArrayRing=[]	
for index in range(len(trackingArrayRing)):
	#print trackingArrayRing[index]
	
	if index!=len(trackingArrayRing)-1:
	#if index==5:
		driftTrack=None
		firstX=1+0.5*trackingArrayRing[index][0]/theMax
		secondX=1+0.5*trackingArrayRing[index+1][0]/theMax
		driftTrack=TLine(trackingArrayRing[index][1]/Length,midLine*firstX,trackingArrayRing[index+1][1]/Length,midLine*secondX)
		driftTrack.SetNDC()
		driftTrack.SetLineColor(kGreen)
		driftTrackArrayRing.append(driftTrack)
		#driftTrack.Draw("same")
			
			
driftTrackArray=[]	
for index in range(len(trackingArray)):
	#print trackingArray[index]
	
	if index!=len(trackingArray)-1:
	#if index==5:
		driftTrack=None
		firstX=1+0.5*trackingArray[index][0]/theMax
		secondX=1+0.5*trackingArray[index+1][0]/theMax
		driftTrack=TLine(trackingArray[index][1]/Length,midLine*firstX,trackingArray[index+1][1]/Length,midLine*secondX)
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
wasteSeptum=TLine(Length/Length,midLine*(1+0.5*septumStart*1000./theMax),(Length-TMath.Tan(septumAngle)*septumWidth)/Length,midLine*(1+0.5*(septumStart+septumWidth)*1000./theMax))
wasteSeptum.SetNDC()	
wasteSeptum.SetLineWidth(2)
wasteSeptum.SetLineColor(kGreen)
wasteSeptum.Draw("same")
for drift in driftTrackArrayRing:
	drift.Draw("same")
for drift in driftTrackArray:
	drift.Draw("same")
for drift in driftTrackArrayClosed:
	drift.Draw("same")	

theCanvas.Print("%s/tracking_%s_%d_%d_%d_%d.%s"%(theDirectoryClosed,tokenToFind[0],stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max,args.imageType))
#theCanvas.Print("%s/%svs%s/temp%d.%s"%(args.directory,theXAxisVariable,theYAxisVariable,counter,args.imageType))
#theCanvas.SaveAs("temp%d.png"%counter)
theCanvas.Clear()
oneGraph= TGraph()
counter+=1

#print coordinateArray	

#print coordinateArrayClosed
