#!/bin/zsh

#mpirun pw.x < c_2l_AB.scf.in > c_2l_AB.scf.out
for i in 16; do 
kpt=$i
cp -r tmp tmp_$kpt
sed "s/tmp/tmp_${kpt}/" c_2l_AB.nscf.in	 > aa 
sed "s/16 16 1 0 0 0/$kpt $kpt 1 0 0 0/" aa > c_2l_AB.nscf_${kpt}.in	 
sed "s/tmp/tmp_${kpt}/" epsilon1.in > epsilon1_$kpt.in
sed "s/tmp/tmp_${kpt}/" epsilon2.in > epsilon2_$kpt.in 
echo "starting nscf calculation for kpt = $kpt"
mpirun pw.x < c_2l_AB.nscf_${kpt}.in > c_2l_AB.nscf_${kpt}.out
echo "starting eps calculation for kpt = $kpt"
mpirun epsilon.x < epsilon1_${kpt}.in> epsilon1_${kpt}.out
mpirun epsilon.x < epsilon2_${kpt}.in> epsilon2_${kpt}.out
echo "calculation for kpt = $kpt completed"
rm -rf aa
done

