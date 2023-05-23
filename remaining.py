import os
sra_list=os.listdir("Sstrain")
with open('Sstrain.txt', 'r') as f:
    for line  in f.readlines():
        sra_id=line.strip()
        if sra_id in sra_list:
            print(sra_id)
            with open('remaining.txt', 'a') as f2:
                f2.write(line)
