#!/bin/zsh

for i in  12 14 16 
do

kpt=$i
echo "starting calculation for kpt = $kpt"

sed "s/3 3/$kpt $kpt/" bn_1l.scf.in > kpt_$kpt.in

pw.x < kpt_$kpt.in > kpt_$kpt.out

rm -fr tmp

echo "calculation for kpt = $kpt completed"

done

grep '!  ' *.out >> kpttmp.dat
sed -i '' -e "s/kpt_//" kpttmp.dat
sed -i '' -e "s/.out:!    total energy              =//" kpttmp.dat

sort -n kpttmp.dat > Etot_vs_kpt1.dat 
rm kpttmp.dat
