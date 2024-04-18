#
cd MoS2_BULK/scf-bands/PBE+vdW

Copy the input files and Scripts files to run and to plot the Bandstructures with and without 
the Spin-orbit Interaction (SOC) included.

cp ./Inputs/*in .
cp ./Scripts/* . 

Open the input and look at the new variables introduced in the input to run the case wSOC.
Please note that vdW interaction has been commented since it is not compatible with SOC

If your shell is not zsh substitute zsh with bash at the beginning of the script file
run_bands.sh,  close it  and run doing:

./run_bands.sh

At the end you should have  MoS2_BULK.scf.out MoS2_BULK.bands.out bands.out and the corresponding files of the simulations performed with SOC that are called 
MoS2_BULK.scf_wsoc.out MoS2_BULK.bands_wsoc.out bands_wsoc.out

Open them and check everything is ok

There should be also other 6 files Band* 
You can use the python script plot_bands_nsoc.py to plot the B*gnu file without soc

python plot_bands_nsoc.py
 
You can use the python script plot_bands_wsoc.py to plot the B*gnu file with soc

python plot_bands_wsoc.py

At the end you should have two files Bands_MoS2_bulk_PBE-vdW_nSOC.png and Bands_MoS2_bulk_PBE_wSOC.png in a png format 

If you wish you can repeat the same calculations for the LDA and PBE relaxed structures and compare them 
