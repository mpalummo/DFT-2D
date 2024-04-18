#!/bin/zsh

echo "starting bands no SOC calculation "

mpirun pw.x < MoS2_bulk.scf.in > MoS2_bulk.scf.out
mpirun pw.x < MoS2_bulk.bands.in > MoS2_bulk.bands.out
mpirun bands.x < bands.in > bands.out

echo "calculation completed"

echo "starting bands with SOC calculation "

mpirun pw.x < MoS2_bulk.scf_wsoc.in > MoS2_bulk.scf_wsoc.out
mpirun pw.x < MoS2_bulk.bands_wsoc.in > MoS2_bulk.bands_wsoc.out
mpirun bands.x < bands_wsoc.in > bands_wsoc.out

echo "calculation with SOC completed"

