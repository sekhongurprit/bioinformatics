import os
l=os.listdir()
for  f in l:
    if f.lower().endswith(".mol2"):
        nl=f.split('_')
        out=nl[5]+nl[6]
        os.rename(f, out)
