#!/bin/zsh

echo "starting bands no SOC calculation "

mpirun pw.x < MoS2_1L.scf.in > MoS2_1L.scf.out
mpirun pw.x < MoS2_1L.bands.in > MoS2_1L.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

echo "starting bands with SOC calculation "

mpirun pw.x < MoS2_1L.scf_wsoc.in > MoS2_1L.scf_wsoc.out
mpirun pw.x < MoS2_1L.bands_wsoc.in > MoS2_1L.bands_wsoc.out
mpirun bands.x < bands_wsoc.in > bands_wsoc.out

echo "calculation with SOC completed"

