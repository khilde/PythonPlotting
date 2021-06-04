#!/bin/bash
echo "Hello World"
#filename=outputAddMagnetNoFoilNode35_Parts_3_XDipole_10
#filename=outputAddMagnetNoFoilNode35_Parts_3_Dipole_10
filename=outputAddMagnetNoFoilNode35_Parts_3_NoDipole_10
framerate=10

ffmpeg -y -framerate "$framerate" -i "$filename/XvsY/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$filename/XvsY/"atemp.mp4
ffmpeg -y -framerate "$framerate" -i "$filename/XvsPX/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$filename/XvsPX/"atemp.mp4
ffmpeg -y -framerate "$framerate" -i "$filename/YvsPY/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$filename/YvsPY/"atemp.mp4

ffmpeg -y -framerate "$framerate" -i "$filename""_first_Bunch_Only/XvsY/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$filename""_first_Bunch_Only/XvsY/"atemp.mp4
ffmpeg -y -framerate "$framerate" -i "$filename""_first_Bunch_Only/XvsPX/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$filename""_first_Bunch_Only/XvsPX/"atemp.mp4
ffmpeg -y -framerate "$framerate" -i "$filename""_first_Bunch_Only/YvsPY/"temp%00d.png -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p "$filename""_first_Bunch_Only/YvsPY/"atemp.mp4
