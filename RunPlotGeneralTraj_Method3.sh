#!/bin/bash
echo "Hello World"
configFileName=ConfigFiles/DefaultConfig.txt
directoryOutputSuffix=Plots
inputDirectoryPrefix=Method3
magneticFieldFiles=(UpUp DownDown UpDown DownUp LeftLeft LeftRight)
suffixInjection=InjectBeam_Method3
suffixWaste=WasteBeam_Method3
suffixClosed=ClosedBeam_Method3

for j in ${magneticFieldFiles[@]}
do
	python plot_GeneralTrajectories.py --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j"
	python plot_GeneralTrajectories.py --doY 1 --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j"
done
