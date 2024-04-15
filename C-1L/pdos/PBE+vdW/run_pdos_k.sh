#!/bin/zsh

for kpt in 50 
do

echo "starting nscf calculation for kpt = $kpt"

cp -r tmp tmp$kpt
sed "s/12 12/$kpt $kpt/" c_1l.nscf.in > kpttmp_$kpt.in
sed "s/tmp/tmp$kpt/"  kpttmp_$kpt.in > kpt_$kpt.in
sed "s/tmp/tmp$kpt/"  pdos.in > pdostmp_$kpt.in
sed "s/graphene_PBE_vdW_DOS/graphene_PBE_vdW_DOS$kpt/"  pdostmp_$kpt.in > pdos_$kpt.in
mpirun pw.x < kpt_$kpt.in > kpt_$kpt.out
mpirun projwfc.x < pdos_$kpt.in > pdos_$kpt.out

echo "calculation for kpt = $kpt completed"

done

