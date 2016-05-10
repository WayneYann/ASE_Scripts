from ase import Atoms
from ase.lattice import surface
from ase.constraints import FixAtoms
from ase.calculators.vasp import Vasp
from ase.visualize import view
from ase.io import write
from ase.io import read

#sigma=0.01 for gases and edif=13-8

calc = Vasp(xc='PBE', kpts=(9,9,1), lwave=False, lcharg=False,lvtot=False, nwrite=1
            , encut=400, algo='Fast', ismear=1, sigma=0.1, voskown=1, istart=0, nelm=400, nelmdl=-12, ediff=1e-6, ispin=1
            ,nsw=100, isif=2, ibrion=5, nfree=2, potim=0.015
            ,npar=2, lvdw=True, vdw_version=3
            ,lreal='Auto')

slab = read('CONTCAR')


slab.center(vacuum=20.0,axis=2)

#freeze all atoms but adsorbate and whichever others are in atomIndex
atomIndex = [65]
constraint = FixAtoms(indices=[atom.index for atom in slab if atom.index not in atomIndex])
slab.set_constraint(constraint)

view(slab) # View the slab, frozen atoms will be marked with a "X"


#slab.set_calculator(calc)

calc.initialize(slab)
calc.write_incar(slab)
calc.write_potcar()
calc.write_kpoints()
write('POSCAR', calc.atoms_sorted)  # this will write a "sorted" POSCAR
