#!/bin/zsh

for kpt in  60 
do

echo "starting nscf calculation for kpt = $kpt"

mpirun pw.x < c_2l_AA.scf.in > c_2l_AA.scf.out
mpirun pw.x < c_2l_AA.nscf.in > c_2l_AA.nscf.out
#mpirun dos.x < dos.in > dos.out
mpirun pp.x < stm.in > stm.out

echo "calculation for kpt = $kpt completed"

done

