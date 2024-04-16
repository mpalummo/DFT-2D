#!/bin/zsh

for kpt in 60 
do

echo "starting nscf calculation for kpt = $kpt"

mpirun pw.x < bn_1l.scf.in > bn_1l.scf.out
mpirun pw.x < bn_1l.nscf.in > bn_1l.nscf.out
mpirun dos.x < dos.in > dos.out
mpirun pp.x < stm.in > stm.out

echo "calculation for kpt = $kpt completed"

done

