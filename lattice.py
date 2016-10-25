from ase.calculators.vasp import Vasp
from ase.lattice.cubic import FaceCenteredCubic
from ase.io import write
calc = Vasp(xc='PBE', kpts=(3,3,3), ismear=0, sigma=0.1, ediff=1e-10, lcharg=False, lwave=False, encut=400,
            nelmin=4, nelmdl=6, ispin=1,lvdw=True, vdw_version=3,isif=3,ibrion=1,nsw=500)

#a = 5.0
#c = 3.5
#iro2 = crystal(['Ir', 'O'], basis=[(0,0,0), (0.3,0.3,0)], cellpar=[a, a, c, 90, 90, 90], spacegroup=136)
#FCC

Cell = FaceCenteredCubic(symbol='Ag') 
Cell.set_calculator(calc)

calc.initialize(Cell)
calc.write_incar(Cell)
calc.write_potcar()
calc.write_kpoints()
write('POSCAR', calc.atoms_sorted)  # this will write a "sorted" POSCAR


#sf = StrainFilter(Cell)

#opt = LBFGS(sf, trajectory=traj('atom-cell.traj', 'w', Cell))
#opt.run(fmax=0.01)

#opt = LBFGS(Cell, trajectory=traj('atom.traj', 'w', Cell))
#opt.run(fmax=0.01)

