#!/bin/zsh

for alat in 4.5 4.55 4.57 4.6 4.63 4.65 4.67 4.7 4.72 
do

echo "starting calculation for alat = $alat"

sed "s/celldm(1) = 4.6640/celldm(1) = $alat/" c_1l.relax.in > alat_$alat.in

pw.x < alat_$alat.in > alat_$alat.out

rm -fr tmp

echo "calculation for kpt = $kpt completed"

done

grep '!  ' *.out >> alattmp.dat
sed -i '' -e "s/alat_//" alattmp.dat
sed -i '' -e "s/.out:!    total energy              =//" alattmp.dat

sort -n alattmp.dat > Etot_vs_alat_pbe-vdW.dat 
rm alattmp.dat
