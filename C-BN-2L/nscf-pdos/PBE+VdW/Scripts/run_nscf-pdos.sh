#!/bin/zsh

for kpt in  60 
do

echo "starting scf 12x12x1 and nscf calculation for kpt = $kpt"

mpirun pw.x < cbn_2l_AB.scf.in > cbn_2l_AB.scf.out 
mpirun pw.x < cbn_2l_AB.nscf.in > cbn_2l_AB.nscf.out
mpirun projwfc.x < pdos.in > pdos.out

echo "calculation for kpt = $kpt completed"

done

