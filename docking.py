import pyscreener as ps
import ray
import os
import json
from pathlib import Path


ray.init()
DIR=Path.cwd()
LIG='etz.csv'
REC='dhbps.pdb'
LIG_PATH=DIR.joinpath(LIG)
REC_PATH=DIR.joinpath(REC)
CENTRE_ribA= (-19.8395, 4.3085, 79.86250000000001)
SIZE_ribA= (15.8535, 15.3065, 13.06349999999999)
CENTRE_ribB= (-10.7515, -17.4355, 2.665)
SIZE_ribB= (13.2625, 12.065500000000002, 12.312000000000001)

os.environ['DOCK6']='/home/bvs/gurprit/soft/dock6/'
supply=ps.LigandSupply([LIG_PATH])
md = ps.build_metadata("dock", dict(enclose_spheres=False))
#md = ps.build_metadata("vina")
#vs = ps.virtual_screen("dock", [REC_PATH], CENTRE_ribA, SIZE_ribA, md) 
vs = ps.virtual_screen("dock", [REC_PATH], CENTRE_ribB, SIZE_ribB, md) 
#vs = ps.virtual_screen("vina", [REC_PATH], CENTRE_ribA, SIZE_ribA, md) 
#vs = ps.virtual_screen("vina", [REC_PATH], CENTRE_ribB, SIZE_ribB, md) 
scores=vs(supply.ligands)
vs.collect_files()


score={}
i=0
for elem in vs.simulations():
    lig=elem.smi.split('\t')[1]
    score[lig]=scores[i]
    i+=1
with open('resD.json', 'w') as f:
    json.dump(score, f)
