from openbabel import pybel
import os
files=os.listdir()
for item in files:
    if  item.endswith('.sdf'):
        infile=pybel.readfile('sdf', item)
for item in infiles, names in files:
    filename=name.split('.')[0]
    out=filename + '.pdb' 
    outfile=pybel.Outputfile('pdb', out, overwrite=True)
    infile.write(out)
