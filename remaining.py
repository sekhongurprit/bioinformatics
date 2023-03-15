import os
list=os.listdir("Sstrain")
with open('Sstrain.txt', 'r') as f:
    for id in f.readlines():
        if strip(id) in list:
            pass
        else:
            with open('remaining.txt', 'w') as f2:
                f2.write(id)
