#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines
from scipy import stats
df=pd.read_excel("/home/gurprit/Desktop/preeti/My analysis SM only.xls", sheet_name=None)

cd20P=pd.DataFrame()
cd38P=pd.DataFrame()
cd27N=pd.DataFrame()
cd27P=pd.DataFrame()

cd20P["CTRL"]=df["Controls"]["CD20+ BCs"]
cd20P["INACTIVE"]=df["In-SLE"]["CD20+ BCs"]
cd20P["ACTIVE"]=df["Ac-SLE"]["CD20+ BCs"]

cd38P["Tr_CTRL"]=df["Controls"]["Transitional (IgD+CD38++)"]
cd38P["Tr_INACTIVE"]=df["In-SLE"]["Transitional (IgD+CD38++)"]
cd38P["Tr_ACTIVE"]=df["Ac-SLE"]["Transitional (IgD+CD38++)"]
cd38P["Pl_CTRL"]=df["Controls"]["Plasmablasts  (IgD-CD38++)"]
cd38P["Pl_INACTIVE"]=df["In-SLE"]["Plasmablasts  (IgD-CD38++)"]
cd38P["Pl_ACTIVE"]=df["Ac-SLE"]["Plasmablasts  (IgD-CD38++)"]

cd27N["DN_CTRL"]=df["Controls"]["DN BCs (IgD-CD27-)"]
cd27N["DN_INACTIVE"]=df["In-SLE"]["DN BCs (IgD-CD27-)"]
cd27N["DN_ACTIVE"]=df["Ac-SLE"]["DN BCs (IgD-CD27-)"]
cd27N["N_CTRL"]=df["Controls"]["Naive BCs (IgD+CD27-)"]
cd27N["N_INACTIVE"]=df["In-SLE"]["Naive BCs (IgD+CD27-)"]
cd27N["N_ACTIVE"]=df["Ac-SLE"]["Naive BCs (IgD+CD27-)"]

cd27P["Pre_CTRL"]=df["Controls"]["Pre SMBNCs  (IgD+CD27+)"]
cd27P["Pre_INACTIVE"]=df["In-SLE"]["Pre SMBNCs  (IgD+CD27+)"]
cd27P["Pre_ACTIVE"]=df["Ac-SLE"]["Pre SMBNCs  (IgD+CD27+)"]
cd27P["Post_CTRL"]=df["Controls"]["Post SMBCs   (IgD-CD27+)"]
cd27P["Post_INACTIVE"]=df["In-SLE"]["Post SMBCs   (IgD-CD27+)"]
cd27P["PostACTIVE"]=df["Ac-SLE"]["Post SMBCs   (IgD-CD27+)"]

cd20P.dropna(inplace=True)
cd38P.dropna(inplace=True)
cd27N.dropna(inplace=True)
cd27P.dropna(inplace=True)

data1=cd20P.to_numpy()
data2=cd38P.to_numpy()
data3=cd27N.to_numpy()
data4=cd27P.to_numpy()

plt.figure(figsize=(6,4))

sp1=plt.subplot(221)
sp2=plt.subplot(222)
sp3=plt.subplot(223)
sp4=plt.subplot(224)

sp1.set_ylim(0,20)
sp2.set_ylim(0,60)
sp3.set_ylim(0,100)
sp4.set_ylim(0,60)



bp1=sp1.boxplot(data1, showfliers=False, patch_artist=True)
bp2=sp2.boxplot(data2, showfliers=False, patch_artist=True, positions=[1,2,3,5,6,7])
bp3=sp3.boxplot(data3, showfliers=False, patch_artist=True, positions=[1,2,3,5,6,7])
bp4=sp4.boxplot(data4, showfliers=False, patch_artist=True, positions=[1,2,3,5,6,7])




colors = ("red", "blue", "green", "red", "blue", "green")
for box, color in zip(bp1["boxes"], colors):
    box.set_facecolor(color)
for box, color in zip(bp2["boxes"], colors):
    box.set_facecolor(color)
for box, color in zip(bp3["boxes"], colors):
    box.set_facecolor(color)
for box, color in zip(bp4["boxes"], colors):
    box.set_facecolor(color)
    
labels=["Control", "Inactive", "Active"]
for box, label in zip(bp1["boxes"], labels):
    sp1.set_xticklabels(labels)

#bp2[["boxes"][0]].set_xticklabels("CD38+ B Cells")

#sp1.set_xticklabels([])
sp2.set_xticklabels([])
sp3.set_xticklabels([])
sp4.set_xticklabels([])

#sp1.legend([bp1["boxes"][0], bp1["boxes"][1], bp1["boxes"][2]], ['CTRL', 'INACTIVVE', 'ACTIVE'], loc='upper left', frameon=False, bbox_to_anchor=(1.05, 1))
#sp2.legend([bp2["boxes"][0], bp2["boxes"][1], bp2["boxes"][2]], ['CTRL', 'INACTIVVE', 'ACTIVE'], loc='upper left', frameon=False, bbox_to_anchor=(1.05, 1))
#sp3.legend([bp2["boxes"][0], bp3["boxes"][1], bp3["boxes"][2]], ['CTRL', 'INACTIVVE', 'ACTIVE'], loc='upper left', frameon=False, bbox_to_anchor=(1.05, 1))
#sp4.legend([bp4["boxes"][0], bp4["boxes"][1], bp4["boxes"][2]], ['CTRL', 'INACTIVVE', 'ACTIVE'], loc='upper left', frameon=False, bbox_to_anchor=(1.05, 1))

sp1.spines['right'].set_visible(False)
sp1.spines['top'].set_visible(False)
sp2.spines['right'].set_visible(False)
sp2.spines['top'].set_visible(False)
sp3.spines['right'].set_visible(False)
sp3.spines['top'].set_visible(False)
sp4.spines['right'].set_visible(False)
sp4.spines['top'].set_visible(False)


sp1.annotate("SLE", (130,150), xycoords="figure points")
sp2.annotate("transitional", (260,160), xycoords="figure points")
sp2.annotate("plasmablasts", (330,160), xycoords="figure points")
sp3.annotate("IgD-CD27-", (60,20), xycoords="figure points")
sp3.annotate("IgD+CD27-", (140,20), xycoords="figure points")
sp4.annotate("IgD-CD27+", (260,20), xycoords="figure points")
sp4.annotate("IgD+CD27+", (340,20), xycoords="figure points")

sp1.set_title("A [CD38+ B Cells]",loc='left')
sp2.set_title("B [tranitional/plasmablasts]", loc='left')
sp3.set_title("C [CD27- B Cells]", loc='left')
sp4.set_title("D [CD27+ B Cells]", loc='left')

sp1.set_ylabel("% of B Cells")
sp2.set_ylabel("% of B Cells")
sp3.set_ylabel("% of B Cells")
sp4.set_ylabel("% of B Cells")


x_coordinates = [1.5, 3.5]
y_coordinates = [-4, -4]
sp1.plot(x_coordinates, y_coordinates,clip_on=False, in_layout=True,scalex=False, scaley=False, c="black", linewidth=0.5)


plt.subplots_adjust(hspace=0.75, wspace=0.5)
plt.savefig("plot.tif", dpi=100)


# In[ ]:




