#!/bin/bash
echo "Hello World"
configFileName=ConfigFiles/DefaultConfig_strippersNotClosed.txt
directoryOutputSuffix=Plots
inputDirectoryPrefix=Method1_strippersNotClosed
#magneticFieldFiles=(UpUp DownDown UpDown DownUp LeftLeft LeftRight RightLeft RightRight)
#magneticFieldFiles=(LeftLeft LeftRight RightLeft RightRight)
magneticFieldFiles=(LeftUp RightUp)
suffixInjection=InjectBeam_Method1
suffixWaste=WasteBeam_Method1
suffixClosed=ClosedBeam_Method1_strippersNotClosed
offsetStripper=1
offsetFoil=1

for j in ${magneticFieldFiles[@]}
do
	python plot_GeneralTrajectories.py --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
	python plot_GeneralTrajectories.py --doY 1 --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
done
