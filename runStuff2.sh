#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=(output_IR_No_Dipoles output_IR_NoDipoles_Last2Scaled output_IR_Dipoles_NotOptimized output_IR_Dipoles_Optimized)

for i in ${filename[@]}
do
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 6 --xmin 0 --xmax 31 --yaxis 0 --ymin -.1 --ymax .1
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 6 --xmin 0 --xmax 31 --yaxis 1 --ymin -.05 --ymax .05
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 6 --xmin 0 --xmax 31 --yaxis 2 --ymin -.1 --ymax .1
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 6 --xmin 0 --xmax 31 --yaxis 3 --ymin -.05 --ymax .05
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 6 --xmin 0 --xmax 31 --yaxis 4 --ymin -.1 --ymax .1
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 0 --xmin -.1 --xmax .1 --yaxis 1 --ymin -.05 --ymax .05
    python plotAfterNodes2.py --fileName "$i.txt" --directory "$i" --xaxis 2 --xmin -.1 --xmax .1 --yaxis 3 --ymin -.05 --ymax .05
done
