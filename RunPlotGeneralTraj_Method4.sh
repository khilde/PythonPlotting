#!/bin/bash
echo "Hello World"
configFileName=ConfigFiles/DefaultConfig_strippersNotClosed_ArrayConfig_ULRU.txt
directoryOutputSuffix=Plots
inputDirectoryPrefix=Method4_strippersNotClosed_ArrayConfig
#magneticFieldFiles=(UpUp DownDown UpDown DownUp LeftLeft LeftRight)
#magneticFieldFiles=(RUL LUR)
magneticFieldFiles=(ULRD)
#magneticFieldFiles=(LeftUp RightUp LeftDown RightDown)
suffixInjection=InjectBeam_Method4_ArrayConfig_FloatLength_p10
suffixWaste=WasteBeam_Method4_ArrayConfig_FloatLength_p10
suffixClosed=ClosedBeam_Method4_strippersNotClosed_ArrayConfig_p10

offsetStripper=1
offsetFoil=1

for j in ${magneticFieldFiles[@]}
do
	python plot_GeneralTrajectories_ArrayConfig.py --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
	python plot_GeneralTrajectories_ArrayConfig.py --doY 1 --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
done
