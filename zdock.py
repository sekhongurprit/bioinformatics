import os
import sys
import subprocess as sbp
l=os.listdir()
outl=[]

for item in l:
    if item.endswith(".pdb"):
        num=item.split(".")[1]
        #print(num)
        if not num.isdigit():
            print("check input files: ", item)
            continue
        basename="crp"
        ext=".pdb"
        name=basename+num+ext
        os.rename(item, name)
        #outname = basename+num+ "H.pdb"
        outl.append(name)
        #add_H="reduce -FLIP " + name  + " > " + outname
        #print(add_H)
        #p=sbp.Popen(add_H, shell=True, stdout=sbp.PIPE, stderr=sbp.PIPE)
        #for line in p.stderr:
            #sys.stdout.write(line.decode('utf-8'))
        #ret=p.wait()
        #os.remove(item)
        #print(name, "done", "return code: ", ret)
        print(name, "done")


outf= open("list.txt", "w")
for item in outl:
    outf.write(item)
    outf.write("\n")

