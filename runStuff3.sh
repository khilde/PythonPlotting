#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=(fixedoutputWithDisplacementWithScaleNegWithDipolesWithKickers100TurnsChicanes outputWithDisplacementWithScaleNegNoDipolesWithKickers100TurnsChicanes outputNoScaleNoDipolesWithKickers100Turns)

for i in ${filename[@]}
do
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" 
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --yaxis 1 --ymin -.02 --ymax .02
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 2 --yaxis 3 --ymin -.02 --ymax .02

done
