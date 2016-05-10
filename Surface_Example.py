from ase import Atoms
from ase.lattice import surface
from ase.constraints import FixAtoms
from ase.calculators.vasp import Vasp
from ase.visualize import view
from ase.io import write
from ase.io import read

#for vibrations sigma=0.1, ibrion=5, nwrite is off, ediff=1e-8, potim = 0.02, prec='accurate', kpoints = 9 9 1

calc = Vasp(xc='PBE', kpts=(3,3,1), nwrite=1, lwave=False, lcharg=False,lvtot=False
            , encut=400, algo='Fast', ismear=1, sigma=0.2, voskown=1, istart=0, nelm=400, nelmdl=-12, ediff=1e-4, ispin=1
            ,nsw=1000, isif=2, ibrion=2, nfree=2, potim=0.2
            ,npar=2, lvdw=True, vdw_version=3
            ,lreal='Auto')

# Create a 4X4 surface with 4 layers and 14 Angstrom of vacuum
#slab = surface.fcc111('Pt', size=(4,4,4), a=3.92,vacuum=20.0)
slab = read('CONTCAR')
#adsorbate = surface.Atoms('O')
#surface.add_adsorbate(slab, adsorbate, 1.25, 'fcc')
for atom in slab:
        if atom.symbol == 'O':
                print(atom.symbol)
                atom.symbol = 'H'

slab.center(vacuum=20.0,axis=2)

#freeze all layers below top two layers
mask = [atom.tag > 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

#write_vasp('POSCAR', slab,  long_format=True, vasp5=True)

view(slab) # View the slab, frozen atoms will be marked with a "X"


#slab.set_calculator(calc)

calc.initialize(slab)
calc.write_incar(slab)
calc.write_potcar()
calc.write_kpoints()
write('POSCAR', calc.atoms_sorted)  # this will write a "sorted" POSCAR
