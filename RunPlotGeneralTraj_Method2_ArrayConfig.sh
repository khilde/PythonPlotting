#!/bin/bash
echo "Hello World"
configFileName=ConfigFiles/DefaultConfig_strippersNotClosed_ArrayConfig_ULRU.txt
directoryOutputSuffix=Plots
inputDirectoryPrefix=Method2_strippersNotClosed_ArrayConfig_p20_Early_Separate_Horiz
#magneticFieldFiles=(UpUp DownDown UpDown DownUp LeftLeft LeftRight)
#magneticFieldFiles=(RUL LUR)
magneticFieldFiles=(ULLL URRR)
#magneticFieldFiles=(LeftUp RightUp LeftDown RightDown)
suffixInjection=InjectBeam_Method2_ArrayConfig_FloatLength_p20_1st_2nd_Early
suffixWaste=WasteBeam_Method2_ArrayConfig_FloatLength_p20_1st_2nd_Early
suffixClosed=ClosedBeam_Method2_strippersNotClosed_ArrayConfig

offsetStripper=1
offsetFoil=1

for j in ${magneticFieldFiles[@]}
do
	python plot_GeneralTrajectories_ArrayConfig.py --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
	python plot_GeneralTrajectories_ArrayConfig.py --doY 1 --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
done