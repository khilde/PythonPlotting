#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
#directory is for injectbeam
#directory2 is for closed beam
directory=WasteBeamSplitGeneralNewStripperChicaneFieldAddedCleanNew
directory2=WasteBeamSplitGeneralClosedBeam
stripperLocation=(0 1 2 3 4 5 6)

for i in ${stripperLocation[@]}
do
    python plotAfterNodes2DrawLinesFromFile_WithClosed_SplitChicane.py --directory "$directory" --directoryClosed "$directory2" --stripper1Location "$i" --imageType "pdf"
    #python plotAfterNodes2DrawLines.py --fileName "$directory$i.txt" --directory "$directory$i" --xaxis 0 --xmin -.06 --xmax .06 --yaxis 1 --ymin -.06 --ymax .06 --markerStyle 1 --rangeWindowX .03 --rangeWindowY .01
    #python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --ymin -.0005 --ymax .0005
    #python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --yaxis 1 --ymin -.06 --ymax .06    
    #python plotAfterNodes2DrawLines.py --fileName "$i.txt" --directory "$i" --xaxis 2 --yaxis 3 --ymin -.02 --ymax .02

done
