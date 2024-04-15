#!/bin/zsh

for kpt in  50 
do

echo "starting nscf calculation for kpt = $kpt"

#mpirun pw.x < c_2l_AB.scf.in > c_2l_AB.scf.out
mpirun pw.x < c_2l_AB.nscf.in > c_2l_AB.nscf.out
mpirun projwfc.x < pdos.in > pdos.out

echo "calculation for kpt = $kpt completed"

done

