from __future__ import division
import numpy as np
from ase import Atoms
from ase.io.trajectory import Trajectory as traj
from ase.lattice import surface
from ase.constraints import FixAtoms
from ase.optimize import LBFGS
from ase.calculators.vasp import Vasp
from ase.io.vasp import write_vasp
from ase.visualize import view
from ase.io import write

calc = Vasp(xc='PBE', kpts=(1,1,1), nwrite=1, lwave=False, lcharg=False,lvtot=False
            , encut=400, algo='Fast', ismear=0, sigma=0.003, voskown=1, istart=0, nelm=400, nelmdl=-10, ediff=1e-6, ispin=2
            ,nsw=1000, isif=2, ibrion=1, nfree=2, potim=0.2,lvdw=True, vdw_version=3
            ,isym=0
            ,lreal='Auto')

# Create a c(2x2) surface with 4 layers and 14 Angstrom of vacuum
d=0.9575
t = np.pi/180*104.51
molecule = Atoms('H2O',
              positions=[(d, 0, 0),(d * np.cos(t), d * np.sin(t), 0),(0, 0, 0)])

molecule.center(vacuum=20.0)
view(molecule) # View the slab, frozen atoms will be marked with a "X"


#slab.set_calculator(calc)

calc.initialize(molecule)
calc.write_incar(molecule)
calc.write_potcar()
calc.write_kpoints()
write('POSCAR', calc.atoms_sorted)  # this will write a "sorted" POSCAR

