#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
#directory is for injectbeam wastebeam
#directory2 is for closed beam
#directory3 is injectbeam ring
directory=WasteBeamSplitGeneralNewStripperChicaneFieldAddedCleanNewTestY_Inject3c_ReverseBoth
directory2=WasteBeamSplitGeneralClosedBeamNewY_Inject3c_ReverseBoth
directory3=InjectBeam3c_ReverseBoth
#stripperLocation=(0 1 2 3 4 5 6)
stripperLocation=(1)
stripperLocation2=(-1)
stripperMax1=1
stripperMax2=0

for i in ${stripperLocation[@]}
do
	for j in ${stripperLocation2[@]}
	do
		python plotAfterNodes2DrawLinesFromFile_WithClosedWithInject_SplitChicaneNewMethodWithY.py --directory "$directory" --directoryClosed "$directory2" --directoryRing "$directory3" --stripper1Location "$i" --stripper2Location "$j" --stripper1LocationMax "$stripperMax1" --stripper2LocationMax "$stripperMax2" --imageType "pdf"
		python plotAfterNodes2DrawLinesFromFile_WithClosedWithInject_SplitChicaneNewMethodWithY.py --doY 1 --directory "$directory" --directoryClosed "$directory2" --directoryRing "$directory3" --stripper1Location "$i" --stripper2Location "$j" --stripper1LocationMax "$stripperMax1" --stripper2LocationMax "$stripperMax2" --imageType "pdf"
		#python plotAfterNodes2DrawLines.py --fileName "$directory$i.txt" --directory "$directory$i" --xaxis 0 --xmin -.06 --xmax .06 --yaxis 1 --ymin -.06 --ymax .06 --markerStyle 1 --rangeWindowX .03 --rangeWindowY .01
		#python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --ymin -.0005 --ymax .0005
		#python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --yaxis 1 --ymin -.06 --ymax .06    
		#python plotAfterNodes2DrawLines.py --fileName "$i.txt" --directory "$i" --xaxis 2 --yaxis 3 --ymin -.02 --ymax .02
	done
done
