from ase.constraints import FixAtoms
from ase.constraints import FixedLine
from ase.visualize import view
from ase.io import read
from ase.io.vasp import write_vasp
#Read in previous CONTCAR
slab = read('CONTCAR',format='vasp')
slab.center()

#Freeze all atoms except NN and adsorbate. Freeze in all directions but one
atomIndex = [36, 27, 28, 30]

constraint1 = FixAtoms(indices=[atom.index for atom in slab if atom.index not in atomIndex])
constraint2 = FixedLine(36,[0, 0, 1])
constraint3 = FixedLine(27,[0, 0, 1])
constraint4 = FixedLine(28,[0, 0, 1])
constraint5 = FixedLine(30,[0, 0, 1])
slab.set_constraint([constraint1,constraint2,constraint3,constraint4,constraint5])

view(slab) # View the slab, frozen atoms will be marked with a "X"

write_vasp('POSCAR', slab, direct=False, long_format=True, vasp5=True)
