import pyscreener as ps
import ray
import os
ray.init()
os.environ['DOCK6']='/home/bvs/gurprit/soft/dock6/'
#supply=ps.LigandSupply(['/home/bvs/gurprit/dock/gch/ligands.smi','/home/bvs/gurprit/dock/gch/actives.smi', '/home/bvs/gurprit/dock/gch/decoys.smi'])
#supply=ps.LigandSupply(['/home/bvs/gurprit/dock/gch/ligands.smi','/home/bvs/gurprit/dock/gch/actives.smi'])
#supply=ps.LigandSupply(['/home/bvs/gurprit/dock/gch/ligands.smi'])
supply=ps.LigandSupply(['/home/bvs/gurprit/dock/gch/ribA.smi'])
#md = ps.build_metadata("dock", dict(enclose_spheres=False, buffer=1.0, write_conformations='yes', conformer_search_type='rigid'))
md = ps.build_metadata("dock", dict(enclose_spheres=False, buffer=1.0,  dock_params=dict(conformer_search_type='rigid', write_conformations='yes')))
print(md)
#md = ps.build_metadata("dock")
#vs = ps.virtual_screen("dock", ["/home/bvs/gurprit/dock/dhbgch.pdb"], (-19.8395, 4.3085, 79.86250000000001), (15.8535, 15.3065, 13.06349999999999), md, ncpu=8)
vs = ps.virtual_screen("dock", ["/home/bvs/gurprit/dock/gch.pdb"], (-19.8395, 4.3085, 79.86250000000001), (15.8535, 15.3065, 13.06349999999999), md, ncpu=80,) 
vs.collect_files("/home/bvs/gurprit/dock")
scores=vs(supply.ligands)
print(scores)


'''
md = ps.build_metadata("vina")
vs = ps.virtual_screen("vina", ["/home/bvs/gurprit/dock/gch/gch.pdb"], (-19.8395, 4.3085, 79.86250000000001), (15.8535, 15.3065, 13.06349999999999), md, ncpu=6)
vs.collect_files("/home/bvs/gurprit/dock/gch")
scores=vs(supply.ligands)
print(scores)
'''
