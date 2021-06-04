#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=(fixedoutputWithDisplacementWithScaleNegWithDipolesWithKickers100TurnsChicanes outputWithDisplacementWithScaleNegNoDipolesWithKickers100TurnsChicanes outputNoScaleNoDipolesWithKickers100Turns)
framerate=10

for i in ${filename[@]}
do
    ffmpeg -y -framerate "$framerate" -i "$i/XvsY/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$i/XvsY/"atemp.mp4
    ffmpeg -y -framerate "$framerate" -i "$i/XvsPX/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$i/XvsPX/"atemp.mp4
    ffmpeg -y -framerate "$framerate" -i "$i/YvsPY/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$i/YvsPY/"atemp.mp4
done
