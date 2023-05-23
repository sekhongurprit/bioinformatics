import json as js
import math
with open('res.json', 'r') as f:
    res=js.load(f)
r=sorted(res.items(), key=lambda x: float('inf') if math.isnan(x[1]) else x[1])[:15]
for item in r:
    id=item[0]
    id=list(res.keys()).index(id)
    print(item[0],"\t", item[1], "\t", id)
