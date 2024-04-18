#!/bin/zsh

mpirun pw.x < BN_bulkAA1.vcrelax.in > BN_bulkAA1.vcrelax.out
mpirun pw.x < BN_bulkAA1.vcrelaxd3.in > BN_bulkAA1.vcrelaxd3.out
mpirun pw.x < BN_bulkAA1.vcrelaxts.in > BN_bulkAA1.vcrelaxts.out
