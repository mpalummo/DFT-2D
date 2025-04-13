
# Graphene monolayer (C_1L)
Here we will learn how to do simulations for a 2D material, like graphene, that is not periodic in all dimensions.
The system will still be calculated using the periodic boundary conditions.
The trick is to put enough vacuum between the 2D layers and the cell border, 
so that the repeating layers are far enough apart that they do not interact.
We will learn how to relax the atomic structure and obtain the equilibrium lattice parameters. 
How to calculate the bandstructure, DOS , STM images and pDOS.
We will use python scripts to plot results

## Purpose
  1. Calculate the convergence parameters: cutoff, k-points, vacuum along the non-periodic direction
  2. Calculate the equilibrium atomic structure through vc-relax simulation 
and possibly relax by using different xc-functionals
  3. Calculate the charge density, bandstructure, dos, pdos at the  equilibrium atomic structure

## Running the exercise
  1. Run the exercises in the folder [convergence]
  2. Run the exercises in the folder [vc-relax]
  3. Run the exercises in the folder [scf]
  4. Run the exercises in the folder [bands]
  5. Run the exercises in the folder [nscf-dos]
  6. Run the exercises in the folder [pdos]
