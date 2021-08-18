#!/bin/bash
echo "Hello World"
configFileName=ConfigFiles/DefaultConfig_strippersNotClosed_ArrayConfig_LetsGo.txt
directoryOutputSuffix=Plots
inputDirectoryPrefix=LetsGo
#magneticFieldFiles=(UpUp DownDown UpDown DownUp LeftLeft LeftRight)
#magneticFieldFiles=(RUL LUR)
magneticFieldFiles=(FoilTest)
#magneticFieldFiles=(LeftUp RightUp LeftDown RightDown)
suffixInjection=InjectBeam79_Method2_ArrayConfig_FloatLength
suffixWaste=OG_Injection_Kicker
suffixWaste2=OG_Injection_SBEND
suffixClosed=InjectBeam8049_Method2_ArrayConfig_FloatLength

#suffixInjection=InjectBeam_Method2_ArrayConfig_FloatLength
#suffixWaste=WasteBeam_Method2_ArrayConfig_FloatLength
#suffixWaste2=WasteBeam2_Method2_ArrayConfig_FloatLength
#suffixClosed=ClosedBeam_Method2_strippersNotClosed_ArrayConfig

offsetStripper=1
offsetFoil=1

for j in ${magneticFieldFiles[@]}
do
	python plot_GeneralTrajectories_ArrayConfig_FoilTest_2Waste.py --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryWaste2 "$inputDirectoryPrefix/$suffixWaste2"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
	python plot_GeneralTrajectories_ArrayConfig_FoilTest_2Waste.py --doY 1 --directoryOutput "$inputDirectoryPrefix/$directoryOutputSuffix"_"$j" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix/$suffixWaste"_"$j" --directoryWaste2 "$inputDirectoryPrefix/$suffixWaste2"_"$j" --directoryInjection "$inputDirectoryPrefix/$suffixInjection"_"$j" --directoryClosed "$inputDirectoryPrefix/$suffixClosed"_"$j" --offsetStripper "$offsetStripper" --offsetFoil "$offsetFoil"
done
