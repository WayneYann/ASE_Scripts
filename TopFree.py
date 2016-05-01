from ase import Atoms
from ase.lattice import surface
from ase.constraints import FixAtoms
from ase.calculators.vasp import Vasp
from ase.visualize import view
from ase.io import write

calc = Vasp(xc='PW91', kpts=(3,3,1), nwrite=1, lwave=False, lcharg=False,lvtot=False
            , encut=400, algo='Fast', ismear=1, sigma=0.1, voskown=1, istart=0, nelm=400, nelmdl=-10, ediff=1e-6, ispin=2
            ,nsw=1000, isif=2, ibrion=1, nfree=2, potim=0.2, ediffg=-0.04
            ,npar=2
            ,lreal='Auto')

# Create a c(2x2) surface with 4 layers and 14 Angstrom of vacuum
slab = surface.fcc111('Pt', size=(3,3,4), a=3.99,vacuum=14.0)
adsorbate = surface.Atoms('O')

surface.add_adsorbate(slab, adsorbate, 1.23, 'fcc')

slab.center()

#freeze all layers below top layer
mask = [atom.tag > 1 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

view(slab) # View the slab, frozen atoms will be marked with a "X"


#slab.set_calculator(calc)

calc.initialize(slab)
calc.write_incar(slab)
calc.write_potcar()
calc.write_kpoints()
write('POSCAR', calc.atoms_sorted)  # this will write a "sorted" POSCAR
