
# Graphene monolayer (C_1L)
Here we will learn how to run a calculation for a material, like graphene, that is not periodic in all dimensions.
The system will still be calculated using the periodic boundary condition.
The trick is to put enough vacuum between the 2D layer and the cell border, 
so that the repeating layers are far enough apart that they do not interact.
We will learn how relax the atomic structure and cell parameters. How to calculate the bandstructure, DOS and pDOS

## Purpose
  1. Calculate the convergence parameters: cutoff, k-points, vacuum along the non-periodic direction
  2. Calculate the equlibrium atomic structure through vc-relax using different xc-functionals
  3. Calculate the charge density at equilibrium
  4. Calculate and plot the dos, pdos, bandstructure

## Running the exercise
  1. Run the exercises in the folder [convergence].
  2. Run the exercises in the folder [vc-relax].
  3. Run the exercised in the folder [scf]
  4. Run the exercised in the folder [nscf-dos]
  5. Run the exercised in the folder [pdos]
  6. Run the exercised in the folder [bands]


