#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=(print_beg_DB12_Laser print_beg_Dipole_DH_A11 print_end_Dipole_DH_A11 print_beg_Dipole_DH_A12 print_end_Dipole_DH_A12 print_end_DB_Waste)
#directory=/home/5rz/PyOrbit/examples-khilde/InjectionRegion/NoMethod_SecondDoneRight_LR
directory=/home/5rz/PyOrbit/examples-khilde/InjectionRegion/NoMethod_SecondDoneRight
#folder=(101_1p0_LR 101_p5_011_p5_LR PPU_InjectBeam_NoMethod_ArrayConfig__Second101_p80_LR PPU_InjectBeam_NoMethod_ArrayConfig__Second011_p80_LR)
folder=(101_1p0 101_p5_011_p5 PPU_InjectBeam_NoMethod_ArrayConfig__Second101_p80_ULRD PPU_InjectBeam_NoMethod_ArrayConfig__Second011_p80_ULRD)
for j in ${folder[@]}
do
	for i in ${filename[@]}
	do
	    python plot_phaseSpace.py --fileName "$directory/$j/$i.txt" --directory "$directory/$j" --xaxis 0 --xmin -1 --xmax 1 --yaxis 1 --ymin -1 --ymax 1 --rangeWindowX .03 --rangeWindowY .01
	    python plot_phaseSpace.py --fileName "$directory/$j/$i.txt" --directory "$directory/$j" --xaxis 2 --xmin -1 --xmax 1 --yaxis 3 --ymin -1 --ymax 1 --rangeWindowX .03 --rangeWindowY .01
	
	done
done