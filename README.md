# DFT-2D

# DFT Tutorial 
Beginner tutorial for Density Functional Theory (DFT) calculations for 2D materials using [Quantum Espresso](https://www.quantum-espresso.org/)(QE) [1,2]. 

## Required packages
* A working version of QE (>=6.4) needs to be installed/compiled and the executables needs to be located in the PATH environmental variable or specified manually in the variable BIN_DIR.
* A working version of gnuplot (>=5.0) (Some scripts will generate gnuplot files to plot the results. Other programs can also be used)
* A working version of XCrySDen (http://www.xcrysden.org/), a program that can visualize input and output files of QE.
* A working version of avogadro (https://avogadro.cc/), a program for creating and viewing molecular structures
* A working version of python (>=3) with matplotlib and numpy installed 


## Installing/Compiling QE
* QE can be installed from repository for Debian based linux distros (e.g.: Ubuntu) by running the command
    ```
    % sudo apt-get install quantum-espresso
    ```
    PS: The latest available version is shown at: https://packages.ubuntu.com/groovy/quantum-espresso (>6.5-1)

* QE can be compiled from source:
 1. Download the desired release version from the GitHub page "https://github.com/QEF/q-e/releases". 
 2. Unzip/tar the downloaded package and go inside the folder.
 3. From terminal run the commands

     ```
     % ./configure --prefix=path for installation
     % make all
     % make install
NOTE: options for the configuration / use of external libraries for optimized executables is beyond the purpose of this tutorial.


## Downloading the exercises 

To download the exercise repository, run
  ```
  git clone https://github.com/mpalummo/DFT-2D.git DFT-2D
  cd DFT-2D
  ```
The repository can be updated by running
  ```
  git pull
  ```
Alternatively, you can download a static copy by browsing to https://github.com/mpalummo/DFT-2D , click the green Code button and Download zip (unzip to extract)

#  Go in the different subdirectories in this order

C_1L, C_2L, BN_1L, BN_2L, MoS2-BULK, MoS2-1L,MoS2-2L

optionally you can go also in C-BULK and BN-BULK to check how different xc-vdW functionals influence the equibrium atomic structure andconsequently all the electronic properties

and you can go also in CBN-2L to see how graphene properties change when it is interfaced with a BN monolayer
An averaged lattice parameter between graphene and Bn has been selected to relax the heterobilayer
About 1% of strain is then present both layers 
This is done to have the minumum commensurate 1x1 supercell for the hetero-bilayer


If something goes wrong try to open inputs and scripts files and check them to understand which is the problem!
