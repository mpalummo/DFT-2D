#!/bin/zsh

#mpirun pw.x <  bn_2l_AA1.scf.in > bn_2l_AA1.scf.out
for i in 16; do 
kpt=$i
cp -r tmp tmp_$kpt
sed "s/tmp/tmp_${kpt}/" bn_2l_AA1.nscf.in > aa 
sed "s/12 12 1 0 0 0/$kpt $kpt 1 0 0 0/" aa > bn_2l_AA1.nscf_${kpt}.in	 
sed "s/tmp/tmp_${kpt}/" epsilon.in > epsilon_$kpt.in
echo "starting nscf calculation for kpt = $kpt"
mpirun pw.x < bn_2l_AA1.nscf_${kpt}.in > bn_2l_AA1.nscf_${kpt}.out
echo "starting eps calculation for kpt = $kpt"
mpirun epsilon.x < epsilon_${kpt}.in> epsilon_${kpt}.out
echo "calculation for kpt = $kpt completed"
rm -rf aa
done

