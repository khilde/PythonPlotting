#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=outputAddMagnetNoFoilNode35_Parts_3_NoDipole_10
python plotAfterNodes2_OnlyFirstBunch.py --fileName "$filename.txt" --directory "$filename""_first_Bunch_Only" --markerSize 0.25
python plotAfterNodes2_OnlyFirstBunch.py --fileName "$filename.txt" --directory "$filename""_first_Bunch_Only" --yaxis 1 --ymin -.01 --ymax .01 --markerSize 0.25
python plotAfterNodes2_OnlyFirstBunch.py --fileName "$filename.txt" --directory "$filename""_first_Bunch_Only" --xaxis 2 --yaxis 3 --ymin -.01 --ymax .01 --markerSize 0.25

python plotAfterNodes2.py --fileName "$filename.txt" --directory "$filename" --markerSize 0.25
python plotAfterNodes2.py --fileName "$filename.txt" --directory "$filename" --yaxis 1 --ymin -.01 --ymax .01 --markerSize 0.25
python plotAfterNodes2.py --fileName "$filename.txt" --directory "$filename" --xaxis 2 --yaxis 3 --ymin -.01 --ymax .01 --markerSize 0.25
