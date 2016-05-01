import sys
from ase.io import read
from ase.visualize import view
CONTCAR_file = sys.argv[1]

atomfile = read(CONTCAR_file,format='vasp')
view(atomfile)
