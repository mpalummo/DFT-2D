# DFT-2D

# DFT Tutorial 
Beginner tutorial for Density Functional Theory (DFT) calculations for 2D materials using [Quantum Espresso](https://www.quantum-espresso.org/)(QE) [1,2]. 

## Required packages
* A working version of QE (>=6.4) needs to be installed/compiled and the executables needs to be located in the PATH environmental variable or specified manually in the variable BIN_DIR.
* A working version of gnuplot (>=5.0) (Some scripts will generate gnuplot files to plot the results. Other programs can also be used)
* A working version of XCrySDen (http://www.xcrysden.org/), a program that can visualize input and output files of QE.
* A working version of avogadro (https://avogadro.cc/), a program for creating and viewing molecular structures

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

### [Graphene monolayer (C_1L)](C_1L)
  1. Run calculations for graphene monolayer : fixed/not-fixed occupations
  2. Check the supercell size for a 2D material : Compute the vacuum level and work function.
