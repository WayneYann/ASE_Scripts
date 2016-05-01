from ase.constraints import FixAtoms
from ase.visualize import view
from ase.io import read
from ase.io.vasp import write_vasp

#Read in previous POSCAR
slab = read('POSCAR',format='vasp')
slab.center()

#freeze all atoms but adsorbate and NN

atomIndex = [36, 27, 28, 30]

constraint = FixAtoms(indices=[atom.index for atom in slab if atom.index not in atomIndex])
slab.set_constraint(constraint)

view(slab) # View the slab, frozen atoms will be marked with a "X"
write_vasp('POSCAR', slab, direct=False, long_format=True, vasp5=True)
