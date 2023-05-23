import  paramiko 
import os
INFILE='tmp.out'
OUTPATH="/Users/bic/Documents/phoP/final/results/res/"
#OUTPATH="/Users/bic/Documents/phoP/final/results"
s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
MAC="172.16.24.253"
BIC="bic"
PSWD_BIC="Net@bic"
#PORT="22"
s.connect("172.16.24.253",username="bic",password="Net@bic", timeout=4)
sftp = s.open_sftp()
infile=open(INFILE, 'r')
l=[]

for i in range(20):
    for line in infile:
        item=(line.strip()).split("\t")[0]
        outputname=OUTPATH+item
    #l.append(out)
        sftp.put(item, outputname)
        #print(item, outputname)
        #print(item)
        #print(i)
        break
print("done!")
'''
for line in infile:
    for i in range(10):
        item=(line.strip()).split("\t")[0]
    #l.append(out)
        print(item)
        print(i)
        break
    if i == 10:
        break
for line in infile:
    for i in range(10):
        item=(line.strip()).split("\t")[0]
    #l.append(out)
        print(item)
        print(i)
        break
    if i == 10:
        break
    else:
        continue
    #outputname=OUTPATH+item
    #sftp.put(item, outputname)
for item in l[:20]:
    #basename="complex."
    #baseout="CRP."
    #ext=".pdb"
    #name=basename+item+ext
    #outname=item+ext
    outputname=OUTPATH+item
    #os.rename(name, outname)
    sftp.put(item, outputname)
    print(outname, outputname)
'''
