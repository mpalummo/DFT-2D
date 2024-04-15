#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name="1L"
#SBATCH --get-user-env
#SBATCH --output=_scheduler-stdout.txt
#SBATCH --error=_scheduler-stderr.txt
#SBATCH --time=24:00:00
#SBATCH --partition=jobs
####SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=32
#SBATCH --cpus-per-task=2
#SBATCH --qos=normal_theos

export OMP_NUM_THREADS=2

module purge
module load intel/19.1.3.304
module load intel-mkl/2020.4.304
module load quantum-espresso/6.8.0-mpi



mpirun -n $SLURM_NTASKS pw.x -in 1L-MoS2-scf-SOC.in > 1L-MoS2-scf-SOC.out
mpirun -n $SLURM_NTASKS pw.x -npool 8 -in 1L-MoS2-bands-SOC.in > 1L-MoS2-bands-SOC.out
mpirun -n $SLURM_NTASKS bands.x -npool 4 -in bandspp.in > bandspp.out
