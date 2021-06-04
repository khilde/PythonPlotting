#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
directory=RampingField4/
filename=(print_beg print_beg_DH11 print_DH11_3pre print_DH11_3 print_beg_b23 print_beg_DH12 print_DH12_3pre print_DH12_3 print_end_DH12)

for i in ${filename[@]}
do
    python plotAfterNodes2DrawLines.py --fileName "$directory$i.txt" --directory "$directory$i" --xmin -.06 --xmax .06 --ymin -.06 --ymax .06 --markerStyle 1 --rangeWindowX .03 --rangeWindowY .03
    python plotAfterNodes2DrawLines.py --fileName "$directory$i.txt" --directory "$directory$i" --xaxis 0 --xmin -.06 --xmax .06 --yaxis 1 --ymin -.06 --ymax .06 --markerStyle 1 --rangeWindowX .03 --rangeWindowY .01
    #python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --ymin -.0005 --ymax .0005
    #python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --yaxis 1 --ymin -.06 --ymax .06    
    #python plotAfterNodes2DrawLines.py --fileName "$i.txt" --directory "$i" --xaxis 2 --yaxis 3 --ymin -.02 --ymax .02

done
