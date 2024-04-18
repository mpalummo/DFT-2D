#!/bin/zsh

for kpt in  60 
do

echo "starting scf 12x12x1 and nscf and pdos calculation for kpt = $kpt"

mpirun pw.x < bn_1l.scf.in > bn_1l.scf.out
mpirun pw.x < bn_1l.nscf.in > bn_1l.nscf.out
mpirun projwfc.x < pdos.in > pdos.out

echo "calculation for kpt = $kpt completed"

done

