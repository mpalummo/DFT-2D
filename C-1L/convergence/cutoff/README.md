# Convergence on the kinetic energy cutoff
 We start by testing convergence with respect to the kinetic energy cutoff, ecutwfc.
  1. First take a look at the system with xcrysden.
      ```
      % xcrysden --pwi C_1L.scf.in
      ```
      First leave "Do not reduce dimensionality" checked.
      Click Modify -> Numer of units drawn -> Expand to 3x3x3.
     ![Graphene geometry](Ref/graphene-supercell.png?raw=true "Graphene geometry")

      We have constructed what is known as a "supercell". Each supercell contains a thin slab sandwiched between thicker layers of empty space (vacuum). The unit cell contains 2 atoms of C, and the slab is only a single atom thick (a monolayer). Since quantum-ESPRESSO uses periodic boundary conditions, the system is composed of infinite sheets in the x-y plane, periodically repeated in the z direction. We will look more closely at the geometry in the following tutorials. First, however, we must carry out some convergence tests.

  2. As in the case of bulk Si, we start with the kinetic energy cutoff. You can Change manually the value of `ecutwfc` from 10 up to 100 Ry in regular steps.
     and then Change the name of the output file each time such as:
      ```
      % pw.x < C_1L.scf.in > C_1L.scf.out_10Ry
      ```
      
  3. or use directly the script run_ecut.sh which will run the inputs with increasing cutoff and will create a file call 'Etot_vs_Ecut.dat' at the end 

     ![Total energy vs kinetic energy cutoff](Ref/Etot_vs_Ecut.png?raw=true "Total energy vs kinetic energy cutoff")

     You will notice that a much higher cutoff is needed for C than for Si, for the same pseudopotential: we say C is "harder" than Si.     For the sake of this tutorial, however, let's keep a low cutoff of 20 Ry.
  6. ADVANCED USERS: The shell scripts 'run_ecut' and 'run_plots' in the 'Script' directory will do everything automatically from step 3 to 5 (explained using comments inside the script). You may first have to modify the ENVIRONMENT_VARIABLES file in the root directory. The scripts must be run from the main 0_cutoff directory (or copied there). Hit 'q' to cycle through plot windows as they appear. Inspect the PDFs or PNGs that are created.
      ```
      ./Script/run_ecut
      ./Script/run_plots
      ```
      NB: Do not use the scripts for your own projects unless you understand well how they work!
