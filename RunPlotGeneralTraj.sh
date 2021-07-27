#!/bin/bash
echo "Hello World"
configFileName=ConfigFiles/DefaultConfig.txt
directoryOutputSuffix=Plots
inputDirectoryPrefix=Method1_UpUp
suffixInjection=InjectBeam
suffixWaste=WasteBeam
suffixClosed=ClosedBeam

python plot_GeneralTrajectories.py --directoryOutput "$inputDirectoryPrefix"_"$directoryOutputSuffix" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix"_"$suffixWaste" --directoryInjection "$inputDirectoryPrefix"_"$suffixInjection" --directoryClosed "$inputDirectoryPrefix"_"$suffixClosed"
python plot_GeneralTrajectories.py --doY 1 --directoryOutput "$inputDirectoryPrefix"_"$directoryOutputSuffix" --configFileName "$configFileName" --directoryWaste "$inputDirectoryPrefix"_"$suffixWaste" --directoryInjection "$inputDirectoryPrefix"_"$suffixInjection" --directoryClosed "$inputDirectoryPrefix"_"$suffixClosed"
