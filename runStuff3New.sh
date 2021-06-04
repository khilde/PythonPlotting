#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=(ConstantField_1p2/print_beg ConstantField_1p2/print_beg_b23)

for i in ${filename[@]}
do
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.0005 --xmax .0005 --ymin -.0005 --ymax .0005
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.0005 --xmax .0005 --yaxis 1 --ymin -.006 --ymax .006
    #python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --ymin -.0005 --ymax .0005
    #python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xmin -.05 --xmax .05 --yaxis 1 --ymin -.06 --ymax .06    
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 2 --yaxis 3 --ymin -.02 --ymax .02

done
