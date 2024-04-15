#!/bin/zsh

mpirun pw.x < c_2l_AB.scf.in > c_2l_AB.scf.out
for kpt in  20 40 50 60 
do

echo "starting nscf calculation for kpt = $kpt"

cp -r tmp tmp$kpt
sed "s/12 12/$kpt $kpt/" c_2l_AB.nscf.in > kpttmp_$kpt.in
sed "s/tmp/tmp$kpt/"  kpttmp_$kpt.in > kpt_$kpt.in
sed "s/tmp/tmp$kpt/"  dos.in > dostmp_$kpt.in
sed "s/graphene_PBE_vdW_DOS/graphene_PBE_vdW_DOS$kpt/"  dostmp_$kpt.in > dos_$kpt.in
mpirun pw.x < kpt_$kpt.in > kpt_$kpt.out
mpirun dos.x < dos_$kpt.in > dos_$kpt.out

echo "calculation for kpt = $kpt completed"

done

grep '!  ' *.out >> kpttmp.dat
sed -i '' -e "s/kpt_//" kpttmp.dat
sed -i '' -e "s/.out:!    total energy              =//" kpttmp.dat

sort -n kpttmp.dat > Etot_vs_kpt.dat 
rm kpttmp.dat
