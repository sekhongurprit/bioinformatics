#!/usr/bin/env python
# coding: utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams
%matplotlib inline
from scipy.stats import pearsonr
rcParams['font.family'] = 'helvetica'


def histogram_intersection(a, b):

    v = np.minimum(a, b).sum().round(decimals=1)

    return v

plt.figure(figsize=[3.25, 3])
df=pd.read_csv("df1.dat", sep = '\t')

# d1=pd.read_csv("../../d1.dat", sep='\s+')
# d2=pd.read_csv("../../d2.dat", sep='\s+')
# # d1=d1.join(oc)
# # data=d1[['cys98', 'oc2']]
# d1.keys()
# # d2.keys()
# data1=d1['Dis_00001'] 
# data2=d2['Dis_00002']
# plt.plot(data1)
# plt.plot(data2)
# corr=pearsonr(data1, data2)
# corr
# # # res=data.corr('pearso
# corr=data.cor(method=histogram_intersection)
# corr
# # res=d1.corrwith(d2)
# res
# d1=d1['cys98'].astype(float)
# d1.plot.line()
# d1['cys98'].plot.line()
# plt.scatter(d1['cys98'], d2['oc2'])
# plt.show()

# data=d1['cys98', 'oc2']
# CORR=data.corr('pearson')
# CORR

# index=[]
# index=df.iloc[0:0, 0:]
# df2=pd.DataFrame()
# df2.index=index
# df.loc[0,0:]
# df.set_index('Sr.No.')
# df.columns=
# df.head()
# df.transp1se()

# # df2.columns=[df.loc[0:, :0]]
# df2=df.transpose()
# df.index
df=df.transpose()
df*=100
ax=df.plot.bar()
csfont = {'fontname':'Comic Sans MS'}
hfont = {'fontname':'Helvetica'}
# plt.title('title',**csfont)
#plt.xlabel('xlabel', **hfont)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.ylabel("Hydrogen bond ccupancy (%)")

# xmin, xmax = plt.xlim()
# ymin, ymax = plt.ylim()
# scale_factor1=1/10
# scale_factor2=100
# #plt.xlim(xmin * scale_factor1, xmax * scale_factor1)
# plt.ylim(ymin * scale_factor2, ymax * scale_factor2)


for label in ax.get_xticklabels():
    label.set_ha("right")
    label.set_rotation(60)
plt.legend(['500 ns', '1-79 ns', '79-216 ns', '216-500 ns'],bbox_to_anchor=(1.0, 1.1), frameon=False)
plt.gcf().subplots_adjust(bottom=0.35)
plt.savefig("bar.png", dpi=600)
plt.show()



#dTrue.index=df.iloc[0]
# df2=df.transpose(copy=True)
# df2
# # df2.keys
# # df2=df2['500ns'].astype(float)
# df2['500ns'].plot.bar()
# df2.500ns()


# df1=pd.read_csv("avgt.dat", sep="\s+")
# df2=pd.read_csv("avg1.dat", sep="\s+")
# df3=pd.read_csv("avg2.dat", sep="\s+")
# df4=pd.read_csv("avg3.dat", sep="\s+")
# df1S=df1.loc[df1["Frac"] > 0.10]
# df2S=df2.loc[df2["Frac"] > 0.10]
# df3S=df3.loc[df3["Frac"] > 0.10]



# # labels = ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']

# x = np.arange(len(labels))  # the label locations
# width = 0.3 # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width*3/4, df1S["Frac"], width, label='Ist', color='black')
# rects2 = ax.bar(x - width*1/4, df2S["Frac"], width, label='Ist', color='red')
# rects3 = ax.bar(x + width*3/4, df3S["Frac"], width, label='Ist', color='blue')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Fraction')
# ax.set_title('')
# ax.set_xticks(x)
# #ax.set_xticklabels(labels)
# ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)
# autolabel(rects3)
# # autolabel(rects4)

# fig.tight_layout()

# plt.show()

# colnames=df.index
# colnames
# In[ ]:





# In[ ]:




