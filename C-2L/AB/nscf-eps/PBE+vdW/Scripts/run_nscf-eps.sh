#!/bin/zsh

mpirun pw.x < c_2l_AB.scf.in > c_2l_AB.scf.out
for i in 3; do 
kpt=$i
echo "starting nscf calculation for kpt = $kpt"
cp -r tmp tmp_$kpt
sed "s/tmp/tmp_${kpt}/" c_2l_AB.nscf.in	 > aa 
sed "s/16 16 1 0 0 0/$kpt $kpt 1 0 0 0/" aa > c_2l_AB.nscf_${kpt}.in	 
sed "s/tmp/tmp_${kpt}/" epsilon.in > epsilon_$kpt.in 

mpirun pw.x < c_2l_AB.nscf_${kpt}.in > c_2l_AB.nscf_${kpt}.out
mpirun epsilon.x < epsilon_${kpt}.in> epsilon_${kpt}.out
echo "calculation for kpt = $kpt completed"
!rm -rf aa
done

