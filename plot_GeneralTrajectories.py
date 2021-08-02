from ROOT import *
import sys
import os, argparse
import signal
from ConfigureFileClass import ConfigureFileReader
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
    
def aLine(x1,y1,x2,y2):
    theLine=TLine(x1,y1,x2,y2)
    theLine.SetNDC()
    theLine.Draw("same")
    return theLine
parser = argparse.ArgumentParser(description="%prog [options]", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
#parser.add_argument("--directory", dest='directory', default="/share/t3data3/khildebr/RandomConeV204MC/", help="Path to the input directory")
parser.add_argument("--directoryOutput", dest='directoryOutput', default="output5", help="directory to put graphs into")
parser.add_argument("--directoryWaste", dest='directoryWaste', default="output5", help="directory to put graphs into")
parser.add_argument("--directoryClosed", dest='directoryClosed', default="output5", help="directory to put graphs into")
parser.add_argument("--directoryInjection", dest='directoryInjection', default="output5", help="directory to put graphs into")
parser.add_argument("--imageType", dest='imageType', default="pdf", help="what file type to save image as (ie png)")
parser.add_argument("--doY", type=int, dest='doY', default=0, help="Draw Y if positive")

parser.add_argument("--configFileName", dest='configFileName', default="ConfigFiles/DefaultConfig.txt", help="info on python plotting configing")

args = parser.parse_args()
#stripper2CurrentLocation=5
#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3, end of chicane 3,begginning of chicane 4, end of chicane 4

plottingSettingsDictionary=ConfigureFileReader(args.configFileName)
plottingSettingsDictionary.printDictionary()
nPartsChicane=1
nPartsChicane2=0
stripperPositionArray=["0"]
stripperPositionArray2=["0"]
doDipoleStrippersInjection=False
doDipoleStrippersClosed=False

stripper1Max=int(plottingSettingsDictionary.getValue("firstStripperPositionMax"))
stripper2Max=int(plottingSettingsDictionary.getValue("secondStripperPositionMax"))	
stripperPositionArray=plottingSettingsDictionary.getArray("firstStripperPositionArray")
stripperPositionArray2=plottingSettingsDictionary.getArray("secondStripperPositionArray")

foil2Location=plottingSettingsDictionary.getValue("foil2Location")
#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042,5.35030,6.24055]
#prefixFileName="emmit"

#fileNameArray=["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_beg_b23_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
#fileNameArray=["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_end_DH11_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
#coordinateArray sorts them based on file name array
#trackingArray just contains all of em
fileNameArrayInjection=plottingSettingsDictionary.getArray("fileNameArrayInjection")
fileNameArrayWaste=plottingSettingsDictionary.getArray("fileNameArrayWaste")
fileNameArrayClosed=plottingSettingsDictionary.getArray("fileNameArrayClosed")
fileNamePrefix=["emmit_beg","emmit_end"]
for currentPart in stripperPositionArray:
	stripper1CurrentLocation=int(currentPart)
	for currentPart2 in stripperPositionArray2:
		stripper2CurrentLocation=int(currentPart2)
		coordinateArrayWaste={}
		coordinateArrayClosed={}
		coordinateArrayInjection={}
		trackingArrayWaste=[]
		trackingArrayClosed=[]
		trackingArrayInjection=[]
		theDirectoryWaste=args.directoryWaste
		theDirectoryClosed=args.directoryClosed
		theDirectoryInjection=args.directoryInjection
		
		
		doY=False
		if args.doY >0 :
			doY=True
		tokenToFind="x avg"
		positionTokenToFind=0
		if doY:
			tokenToFind="y avg"
			positionTokenToFind=1
    
		#fileName=sys.argv[1]
		if not os.path.isdir(args.directoryOutput):
		    os.mkdir(args.directoryOutput)
		    #print("%s directory does not exist"%(args.directory))
		    #sys.exit(0)
		theNaming=["X","PX","Y","PY","Z","PZ","S"]
		theNamingWithUnits=["X (m)","PX (rad)","Y (m)","PY (rad)","Z (m)","PZ (GeV)","S (m)"]

		#stops each canvas from being physically drawn
		gROOT.SetBatch(True)    
		#build drawing array for injected orbit into ring
		for prefixFileName in fileNamePrefix:
			for currentFileName in fileNameArrayInjection:
				#print "%s/%s%s%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation)
				openedFile=open("%s/%s%s%d_%d_%d_%d.txt"%(theDirectoryInjection,prefixFileName,currentFileName,stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max),'r')
			
				lines=openedFile.readlines()
				coords=[]
	
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
					trackingArrayInjection.append([float(xCoord),float(sCoord)])
					coords.append([float(xCoord),float(sCoord)])
				coordinateArrayInjection[prefixFileName+currentFileName] =coords
		
		#sort the array
		trackingArrayInjection=sorted(trackingArrayInjection,key=lambda x: (x[1]))
		#build drawing array for closed Orbit
		for prefixFileName in fileNamePrefix:
			for currentFileName in fileNameArrayClosed:
				#print "%s/%s%s%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation)
				openedFile=open("%s/%s%s%d_%d_%d_%d.txt"%(theDirectoryClosed,prefixFileName,currentFileName,stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max),'r')
			
				lines=openedFile.readlines()
				coords=[]
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
				coordinateArrayClosed[prefixFileName+currentFileName] =coords
		
		#sort the array
		trackingArrayClosed=sorted(trackingArrayClosed,key=lambda x: (x[1]))
		#coordinateArrayClosed=sorted(coordinateArrayClosed,key=lambda x: (x[1]))
		#print(sorted(coordinateArrayClosed,key=lambda x: (x[1])))
		countChicane2=0
		countChicane3=0
		#build drawing array
		for prefixFileName in fileNamePrefix:
			for currentFileName in fileNameArrayWaste:
				#print "%s/%s%s%d.txt"%(theDirectory,prefixFileName,currentFileName,stripper1CurrentLocation)
				openedFile=open("%s/%s%s%d_%d_%d_%d.txt"%(theDirectoryWaste,prefixFileName,currentFileName,stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max),'r')
				
				lines=openedFile.readlines()
				coords=[]
	
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
					trackingArrayWaste.append([float(xCoord),float(sCoord)])
					coords.append([float(xCoord),float(sCoord)])
				coordinateArrayWaste[prefixFileName+currentFileName] =coords
		#print "testPrint"
		trackingArrayWaste=sorted(trackingArrayWaste,key=lambda x: (x[1]))
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
		print coordinateArrayWaste	
		theCanvas=TCanvas("TGraph","TGraph",0,0,500,500)
		theCanvas.SetLeftMargin(0.15);
		theCanvas.SetBottomMargin(0.25);	    
		#beg of drift, beginning of chicane 2,beginning of stripping,end of chicane 2,begginning of chicane 3,beginning of stripping2, end of chicane 3,begginning of chicane 4, end of chicane 4
		#drawingArray=[0.,1.51480,2.24164,2.38700,3.27006,4.09536,4.26042,5.35030,6.24055]
		#Length=coordinateArrayWaste[fileNameArrayWaste[len(fileNameArrayWaste)-1]][0][1]
		Length=trackingArrayWaste[len(trackingArrayWaste)-1][1]
		referenceLengthWaste=trackingArrayWaste[0][1]
		referenceLengthInjection=trackingArrayInjection[0][1]
		referenceLengthClosed=trackingArrayClosed[0][1] - ((trackingArrayWaste[1][1]-trackingArrayWaste[0][1])-(trackingArrayClosed[1][1]-trackingArrayClosed[0][1]))
		#print "CHECK"
		#print trackingArrayClosed[1][1]-trackingArrayClosed[0][1]
		#print trackingArrayWaste[1][1]-trackingArrayWaste[0][1]
		midLine=.5
		#["_beg_","_beg_DH11_","_DH11_3pre_","_postS_DH11_","_end_DH11_","_beg_DH12_","_DH12_3pre_","_postS_DH12_","_end_DH12_","_beg_DH13_","_end_DH13_","_end_DB_WASTE_"]
		
		#print "%f"%drift1.GetX2()
		haventDrawnYet=True
		theLines=[]
		theBoxes=[]
		for currentFileName in fileNameArrayWaste:
			#draw the drift
			if "DB" in currentFileName:
				print "what it is"
				#if haventDrawnYet:
				#	theLine=TLine((coordinateArrayWaste[fileNamePrefix[0]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine,(coordinateArrayWaste[fileNamePrefix[1]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine)
				#	theLine.SetNDC()
				#	theLine.Draw()
				#	haventDrawnYet=False
				#else:
				#	aLine((coordinateArrayWaste[fileNamePrefix[0]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine,(coordinateArrayWaste[fileNamePrefix[1]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine)
				theLines.append(aLine((coordinateArrayWaste[fileNamePrefix[0]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine,(coordinateArrayWaste[fileNamePrefix[1]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine))
			#draw chicane
			elif "DH" in currentFileName and "Dipole" not in currentFileName:
				theBoxes.append(aBox((coordinateArrayWaste[fileNamePrefix[0]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine/2.,(coordinateArrayWaste[fileNamePrefix[1]+currentFileName][len(coordinateArrayWaste[fileNamePrefix[1]+currentFileName])-1][1]-referenceLengthWaste)/Length,midLine*3./2.))
			#draw stripper
			elif "Dipole" in currentFileName:
				theBoxes.append(aBox((coordinateArrayWaste[fileNamePrefix[0]+currentFileName][0][1]-referenceLengthWaste)/Length,midLine/1.5,(coordinateArrayWaste[fileNamePrefix[1]+currentFileName][len(coordinateArrayWaste[fileNamePrefix[1]+currentFileName])-1][1]-referenceLengthWaste)/Length,midLine*2./1.5))
			
		#draw foil2
		foil2=TLine((coordinateArrayWaste[fileNamePrefix[0]+foil2Location][0][1]-referenceLengthWaste)/Length,midLine*.4,(coordinateArrayWaste[fileNamePrefix[0]+foil2Location][0][1]-referenceLengthWaste)/Length,midLine*1.6)
		#foil2=TLine(coordinateArray["_beg_DH13_"][0][1]/Length,midLine*.4,coordinateArray["_beg_DH13_"][0][1]/Length,midLine*1.6)
			
		foil2.SetNDC()
		foil2.SetLineWidth(2)
		foil2.SetLineColor(kBlue)

		foil2.Draw("same")
		
		theMax=-1.
		for element in coordinateArrayWaste:
			#print element
			for index in range(len(coordinateArrayWaste[element])):
				if abs(coordinateArrayWaste[element][index][0])>theMax:
					theMax=abs(coordinateArrayWaste[element][index][0])
		print "theMax= ", theMax
		theMax=314
		print "theMax=%d"%theMax
		#theOffsetForClosed=coordinateArrayClosed["_beg_"][0][1]-(2.24807-1.514801482455)
		#theOffsetForClosed=referenceLengthClosed
		driftTrackArrayClosed=[]	
		for index in range(len(trackingArrayClosed)):
			#print trackingArrayClosed[index]
			
			if index!=len(trackingArrayClosed)-1:
			#if index==5:
				driftTrack=None
				firstX=1+0.5*trackingArrayClosed[index][0]/theMax
				secondX=1+0.5*trackingArrayClosed[index+1][0]/theMax
				driftTrack=TLine((trackingArrayClosed[index][1]-referenceLengthClosed)/Length,midLine*firstX,(trackingArrayClosed[index+1][1]-referenceLengthClosed)/Length,midLine*secondX)
				driftTrack.SetNDC()
				driftTrack.SetLineColor(kBlue)
				driftTrackArrayClosed.append(driftTrack)
				#driftTrack.Draw("same")
		
		driftTrackArrayInjection=[]	
		for index in range(len(trackingArrayInjection)):
			#print trackingArrayRing[index]
			
			if index!=len(trackingArrayInjection)-1:
			#if index==5:
				driftTrack=None
				firstX=1+0.5*trackingArrayInjection[index][0]/theMax
				secondX=1+0.5*trackingArrayInjection[index+1][0]/theMax
				driftTrack=TLine((trackingArrayInjection[index][1]-referenceLengthInjection)/Length,midLine*firstX,(trackingArrayInjection[index+1][1]-referenceLengthInjection)/Length,midLine*secondX)
				driftTrack.SetNDC()
				driftTrack.SetLineColor(kGreen)
				driftTrackArrayInjection.append(driftTrack)
				#driftTrack.Draw("same")
					
					
		driftTrackArrayWaste=[]	
		for index in range(len(trackingArrayWaste)):
			#print trackingArray[index]
			
			if index!=len(trackingArrayWaste)-1:
			#if index==5:
				driftTrack=None
				firstX=1+0.5*trackingArrayWaste[index][0]/theMax
				secondX=1+0.5*trackingArrayWaste[index+1][0]/theMax
				driftTrack=TLine((trackingArrayWaste[index][1]-referenceLengthWaste)/Length,midLine*firstX,(trackingArrayWaste[index+1][1]-referenceLengthWaste)/Length,midLine*secondX)
				driftTrack.SetNDC()
				driftTrack.SetLineColor(kRed)
				driftTrackArrayWaste.append(driftTrack)
				#driftTrack.Draw("same")
						
		septumAngle=3*TMath.Pi()/180.
		#m
		septumStart=.113
		septumWidth=.2762
		
		septumWidthY=.07
		septumStartY=.046-septumWidthY/2.
		#mm
		#septumStart=113
		#septumWidth=276.2
		if doY:
			wasteSeptum=TLine(Length/Length,midLine*(1+0.5*septumStartY*1000./theMax),Length/Length,midLine*(1+0.5*(septumStartY+septumWidthY)*1000./theMax))
		else:
			wasteSeptum=TLine(Length/Length,midLine*(1+0.5*septumStart*1000./theMax),(Length-TMath.Tan(septumAngle)*septumWidth)/Length,midLine*(1+0.5*(septumStart+septumWidth)*1000./theMax))
		wasteSeptum.SetNDC()	
		wasteSeptum.SetLineWidth(2)
		wasteSeptum.SetLineColor(kGreen)
		wasteSeptum.Draw("same")
		for drift in driftTrackArrayInjection:
			drift.Draw("same")
		for drift in driftTrackArrayWaste:
			drift.Draw("same")
		for drift in driftTrackArrayClosed:
			drift.Draw("same")	
		
		theCanvas.Print("%s/tracking_%s_%d_%d_%d_%d.%s"%(args.directoryOutput,tokenToFind[0],stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max,args.imageType))
		#theCanvas.Print("%s/tracking_%s_%d_%d_%d_%d.%s"%(args.directoryOutput,tokenToFind[0],stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max,"png"))
		#theCanvas.Print("%s/tracking_%s_%d_%d_%d_%d.%s"%(args.directoryOutput,tokenToFind[0],stripper1CurrentLocation,stripper2CurrentLocation,stripper1Max,stripper2Max,"pdf"))
		
		
		#theCanvas.Print("%s/%svs%s/temp%d.%s"%(args.directory,theXAxisVariable,theYAxisVariable,counter,args.imageType))

		#print coordinateArray	
		
		#print coordinateArrayClosed
