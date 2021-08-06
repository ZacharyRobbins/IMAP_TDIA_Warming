# -*- coding: utf-8 -*-
"""
Created on Wed May 12 15:10:41 2021

@author: zacha
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches


WPB_LUT=pd.read_csv('C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/WPB_Inputs/WPB_Trees_6_20.csv')
os.chdir('C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/Figures_NCC/')
AllObs=pd.read_csv("Normal_Runs_3_1.csv",index_col=0)
AllObsH=pd.read_csv("Historic_Runs_3_1.csv",index_col=0)


#
cmap=sns.color_palette().as_hex()
cmap1=sns.color_palette('dark',10).as_hex()
color1=cmap[1]
color2=cmap1[0]



Lowq=AllObs.quantile(q=.025,axis=0)
Mq=AllObs.quantile(q=.5,axis=0)
Highq=AllObs.quantile(q=.975,axis=0)

LowqH=AllObsH.quantile(q=.025,axis=0)
MqH=AllObsH.quantile(q=.5,axis=0)
HighqH=AllObsH.quantile(q=.975,axis=0)
#### Fig 1 
#### Sub 1
def SortingitOut(Input):
    BigTrees1=Input[0:13]
    BigTrees2=Input[13:26]
    BigTrees3=Input[26:39]
    BigTrees4=Input[39:52]
    SmallTrees1=Input[52:65]
    SmallTrees2=Input[65:78]
    SmallTrees3=Input[78:91]
    SmallTrees4=Input[91:104]
    return(BigTrees1,BigTrees2,BigTrees3,BigTrees4,
           SmallTrees1,SmallTrees2,SmallTrees3,SmallTrees4)
LBigTrees_Norm1,LBigTrees_Norm2,LBigTrees_Norm3,LBigTrees_Norm4,LSmallTrees_Norm1,LSmallTrees_Norm2,LSmallTrees_Norm3,LSmallTrees_Norm4=SortingitOut(Lowq)
MBigTrees_Norm1,MBigTrees_Norm2,MBigTrees_Norm3,MBigTrees_Norm4,MSmallTrees_Norm1,MSmallTrees_Norm2,MSmallTrees_Norm3,MSmallTrees_Norm4=SortingitOut(Mq)
UBigTrees_Norm1,UBigTrees_Norm2,UBigTrees_Norm3,UBigTrees_Norm4,USmallTrees_Norm1,USmallTrees_Norm2,USmallTrees_Norm3,USmallTrees_Norm4=SortingitOut(Highq)
### Historic
LBigTrees_Hist1,LBigTrees_Hist2,LBigTrees_Hist3,LBigTrees_Hist4,LSmallTrees_Hist1,LSmallTrees_Hist2,LSmallTrees_Hist3,LSmallTrees_Hist4=SortingitOut(LowqH)
MBigTrees_Hist1,MBigTrees_Hist2,MBigTrees_Hist3,MBigTrees_Hist4,MSmallTrees_Hist1,MSmallTrees_Hist2,MSmallTrees_Hist3,MSmallTrees_Hist4=SortingitOut(MqH)
UBigTrees_Hist1,UBigTrees_Hist2,UBigTrees_Hist3,UBigTrees_Hist4,USmallTrees_Hist1,USmallTrees_Hist2,USmallTrees_Hist3,USmallTrees_Hist4=SortingitOut(HighqH)

BigTrees1=MBigTrees_Norm1
SmallTrees1=MSmallTrees_Norm1
BigTrees2=MBigTrees_Norm2
SmallTrees2=MSmallTrees_Norm2
BigTrees3=MBigTrees_Norm3
SmallTrees3=MSmallTrees_Norm3
BigTrees4=MBigTrees_Norm4
SmallTrees4=MSmallTrees_Norm4

#### Large
LandscapeIn=np.array([BigTrees1,BigTrees2,BigTrees3,BigTrees4]).sum(axis=0)
len(LandscapeIn)
MLandscapeNormal=np.array([MBigTrees_Norm1,MBigTrees_Norm2,MBigTrees_Norm3,MBigTrees_Norm4]).sum(axis=0)
MNorm_MortL=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])/4
LLandscapeNormal=np.array([LBigTrees_Norm1,LBigTrees_Norm2,LBigTrees_Norm3,LBigTrees_Norm4]).sum(axis=0)
LNorm_MortL=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])/4
ULandscapeNormal=np.array([UBigTrees_Norm1,UBigTrees_Norm2,UBigTrees_Norm3,UBigTrees_Norm4]).sum(axis=0)
UNorm_MortL=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])/4


#### Small 
LandscapeIn=np.array([SmallTrees1,SmallTrees2,SmallTrees3,SmallTrees4]).sum(axis=0)
len(LandscapeIn)

MLandscapeNormal=np.array([MSmallTrees_Norm1,MSmallTrees_Norm2,MSmallTrees_Norm3,MSmallTrees_Norm4]).sum(axis=0)
MNorm_MortS=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])/4
LLandscapeNormal=np.array([LSmallTrees_Norm1,LSmallTrees_Norm2,LSmallTrees_Norm3,LSmallTrees_Norm4]).sum(axis=0)
LNorm_MortS=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])/4
ULandscapeNormal=np.array([USmallTrees_Norm1,USmallTrees_Norm2,USmallTrees_Norm3,USmallTrees_Norm4]).sum(axis=0)
UNorm_MortS=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])/4


### Observed
All=np.array(WPB_LUT.loc[:,'Large2006Perc':'Large20018Perc'].sum())
#All.set_index(pd.date_range('2008-06-01', periods=10, freq='y'),inplace=True)
Obs_MortL=(All[0:12]-All[1:13])/4

All=np.array(WPB_LUT.loc[:,'Small2006perc':'Small2018perc'].sum())
Obs_MortS=(All[0:12]-All[1:13])/4
from matplotlib.patches import Rectangle

fig = plt.figure(figsize=(20,20))

fig.autofmt_xdate()
fig.tight_layout()
barWidth = 0.20
r1 = np.arange(len(Obs_MortL))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5= [x + barWidth for x in r4]
plt.gca().add_patch(Rectangle((4.8,0), 5.0, 40, facecolor="red",alpha=.1))
#Make the plot
plt.bar(r1, MNorm_MortS,yerr=(MNorm_MortS-LNorm_MortS , UNorm_MortS-MNorm_MortS) ,error_kw=dict(lw=5, capsize=5, capthick=3),color=color1, width=barWidth, edgecolor='white', label='Simulated')
plt.bar(r2, Obs_MortS, color='#7f6d5f', width=barWidth, edgecolor='white', label='Observed')
plt.bar(r3, MNorm_MortL,yerr=(MNorm_MortL-LNorm_MortL , UNorm_MortL-MNorm_MortL) ,hatch="/",error_kw=dict(lw=5, capsize=5, capthick=3),color=color1, width=barWidth, edgecolor='white', label='Simulated')
plt.bar(r4, Obs_MortL, color='#7f6d5f', width=barWidth, edgecolor='white' ,hatch="/",label='Observed')
 #Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth*1.5 for r in range(len(Obs_MortL))], np.arange(2007,2019,1))
red_patch = mpatches.Patch(color='red', label='The red data')
# Create legend & Show graphic
plt.ylim(0,15)
#plt.xlabel("Trees surviving",fontsize=20)
plt.ylabel("Trees Killed per Hectare",fontsize=40)
plt.xlabel("Year",fontsize=50)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=20)
#plt.suptitle("Trees Killed Less than 31.6 cm",fontsize=40)
plt.tick_params(labelsize=30)
legend=plt.legend(fontsize=50,frameon=False);
plt.gca().add_patch(Rectangle((4.8,0), 5.0, 40, facecolor="red",alpha=.1))
ax = legend.axes
from matplotlib.patches import Patch
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='red', alpha=.1))
labels.append("Drought Period")

legend._legend_box = None
legend._init_legend_box(handles, labels)
legend._set_loc(legend._loc)
legend.set_title(legend.get_title().get_text())

#plt.legend(fontsize=50,frameon=False);


MLandscapeHistoric=pd.DataFrame(np.array([MBigTrees_Hist1,MBigTrees_Hist2,MBigTrees_Hist3,MBigTrees_Hist4]))

MLandscapeNormal=pd.DataFrame(np.array([MBigTrees_Norm1,MBigTrees_Norm2,MBigTrees_Norm3,MBigTrees_Norm4]))


LLandscapeHistoric=pd.DataFrame(np.array([LBigTrees_Hist1,LBigTrees_Hist2,LBigTrees_Hist3,LBigTrees_Hist4]))


LLandscapeNormal=pd.DataFrame(np.array([LBigTrees_Norm1,LBigTrees_Norm2,LBigTrees_Norm3,LBigTrees_Norm4]))

ULandscapeHistoric=pd.DataFrame(np.array([UBigTrees_Hist1,UBigTrees_Hist2,UBigTrees_Hist3,UBigTrees_Hist4]))


ULandscapeNormal=pd.DataFrame(np.array([UBigTrees_Norm1,UBigTrees_Norm2,UBigTrees_Norm3,UBigTrees_Norm4]))
Runs=[ULandscapeNormal,MLandscapeNormal,LLandscapeNormal,ULandscapeHistoric,MLandscapeHistoric,LLandscapeHistoric]
AllDataRaw=pd.concat(Runs)

### Big trees
MLandscapeHistoric=np.array([MBigTrees_Hist1,MBigTrees_Hist2,MBigTrees_Hist3,MBigTrees_Hist4]).sum(axis=0)
MHist_MortL=(MLandscapeHistoric[0:12]-MLandscapeHistoric[1:13])/4

MLandscapeNormal=np.array([MBigTrees_Norm1,MBigTrees_Norm2,MBigTrees_Norm3,MBigTrees_Norm4]).sum(axis=0)
MNorm_MortL=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])/4

LLandscapeHistoric=np.array([LBigTrees_Hist1,LBigTrees_Hist2,LBigTrees_Hist3,LBigTrees_Hist4]).sum(axis=0)
LHist_MortL=(LLandscapeHistoric[0:12]-LLandscapeHistoric[1:13])/4

LLandscapeNormal=np.array([LBigTrees_Norm1,LBigTrees_Norm2,LBigTrees_Norm3,LBigTrees_Norm4]).sum(axis=0)
LNorm_MortL=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])/4

ULandscapeHistoric=np.array([UBigTrees_Hist1,UBigTrees_Hist2,UBigTrees_Hist3,UBigTrees_Hist4]).sum(axis=0)
UHist_MortL=(ULandscapeHistoric[0:12]-ULandscapeHistoric[1:13])/4

ULandscapeNormal=np.array([UBigTrees_Norm1,UBigTrees_Norm2,UBigTrees_Norm3,UBigTrees_Norm4]).sum(axis=0)
UNorm_MortL=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])/4

###Small Trees
MLandscapeHistoric=pd.DataFrame(np.array([MSmallTrees_Hist1,MSmallTrees_Hist2,MSmallTrees_Hist3,MSmallTrees_Hist4]))
#MHist_Mort=(MLandscapeHistoric[0:12]-MLandscapeHistoric[1:13])

MLandscapeNormal=pd.DataFrame(np.array([MSmallTrees_Norm1,MSmallTrees_Norm2,MSmallTrees_Norm3,MSmallTrees_Norm4]))
#MNorm_Mort=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])

LLandscapeHistoric=pd.DataFrame(np.array([LSmallTrees_Hist1,LSmallTrees_Hist2,LSmallTrees_Hist3,LSmallTrees_Hist4]))
#LHist_Mort=(LLandscapeHistoric[0:12]-LLandscapeHistoric[1:13])

LLandscapeNormal=pd.DataFrame(np.array([LSmallTrees_Norm1,LSmallTrees_Norm2,LSmallTrees_Norm3,LSmallTrees_Norm4]))
#LNorm_Mort=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])

ULandscapeHistoric=pd.DataFrame(np.array([USmallTrees_Hist1,USmallTrees_Hist2,USmallTrees_Hist3,USmallTrees_Hist4]))
#UHist_Mort=(ULandscapeHistoric[0:12]-ULandscapeHistoric[1:13])

ULandscapeNormal=pd.DataFrame(np.array([USmallTrees_Norm1,USmallTrees_Norm2,USmallTrees_Norm3,USmallTrees_Norm4]))
#UNorm_Mort=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])

Runs=[ULandscapeNormal,MLandscapeNormal,LLandscapeNormal,ULandscapeHistoric,MLandscapeHistoric,LLandscapeHistoric]
AllDataRaw=pd.concat(Runs)
#AllDataRaw.to_csv("Test3.csv")

MLandscapeHistoric=np.array([MSmallTrees_Hist1,MSmallTrees_Hist2,MSmallTrees_Hist3,MSmallTrees_Hist4]).sum(axis=0)
MHist_MortS=(MLandscapeHistoric[0:12]-MLandscapeHistoric[1:13])/4

MLandscapeNormal=np.array([MSmallTrees_Norm1,MSmallTrees_Norm2,MSmallTrees_Norm3,MSmallTrees_Norm4]).sum(axis=0)
MNorm_MortS=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])/4

LLandscapeHistoric=np.array([LSmallTrees_Hist1,LSmallTrees_Hist2,LSmallTrees_Hist3,LSmallTrees_Hist4]).sum(axis=0)
LHist_MortS=(LLandscapeHistoric[0:12]-LLandscapeHistoric[1:13])/4

LLandscapeNormal=np.array([LSmallTrees_Norm1,LSmallTrees_Norm2,LSmallTrees_Norm3,LSmallTrees_Norm4]).sum(axis=0)
LNorm_MortS=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])/4

ULandscapeHistoric=np.array([USmallTrees_Hist1,USmallTrees_Hist2,USmallTrees_Hist3,USmallTrees_Hist4]).sum(axis=0)
UHist_MortS=(ULandscapeHistoric[0:12]-ULandscapeHistoric[1:13])/4

ULandscapeNormal=np.array([USmallTrees_Norm1,USmallTrees_Norm2,USmallTrees_Norm3,USmallTrees_Norm4]).sum(axis=0)
UNorm_MortS=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])/4







plt.figure(figsize=(20,10))
plt.subplot(121)
plt.gca().set_title('a)',fontsize=20,loc="left")
###Sub2
#Make the plot
plt.bar(r1, MHist_MortS, yerr=(MHist_MortS-LHist_MortS , UHist_MortS-MHist_MortS),error_kw=dict(lw=2, capsize=2, capthick=3), 
        color=color2, width=barWidth, edgecolor='white', label='Historical: Small Hosts')
plt.bar(r2, MNorm_MortS,yerr=(MNorm_MortS-LNorm_MortS , UNorm_MortS-MNorm_MortS) ,error_kw=dict(lw=2, capsize=2, capthick=3),
        color=color1, width=barWidth, edgecolor='white', label='Contemporary: Small Hosts')
plt.bar(r3, MHist_MortL, yerr=(MHist_MortL-LHist_MortL , UHist_MortL-MHist_MortL),error_kw=dict(lw=2, capsize=2, capthick=3), 
        color=color2, width=barWidth, edgecolor='white' ,hatch="/",label='Historical: Large Hosts')
plt.bar(r4, MNorm_MortL,yerr=(MNorm_MortL-LNorm_MortL , UNorm_MortL-MNorm_MortL) ,
        hatch="/",error_kw=dict(lw=2, capsize=2, capthick=3),color=color1, width=barWidth, edgecolor='white', label='Contemporary: Large Hosts')
 #Add xticks on the middle of the group bars
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(Obs_MortL))], np.arange(2007,2019,1))
 
# Create legend & Show graphic
plt.ylim(0,15)
#plt.xlabel("Trees surviving",fontsize=20)
plt.ylabel("Trees Killed per Hectare",fontsize=20)
plt.xlabel("Year",fontsize=20)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=17)
#plt.suptitle("Trees Killed Greater than 31.6 cm",fontsize=40)
plt.gca().add_patch(Rectangle((4.8,0), 5.0, 40, facecolor="red",alpha=.05))
legend=plt.legend(fontsize=17,frameon=False,loc='upper left');
ax = legend.axes
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='red', alpha=.1))
labels.append("Drought Period")
legend._legend_box = None
legend._init_legend_box(handles, labels)
legend._set_loc(legend._loc)
legend.set_title(legend.get_title().get_text())

plt.tick_params(labelsize=20)
plt.xticks(rotation=45)

plt.subplot(122)

MLandscapeHistoric=np.array([MSmallTrees_Hist1,MSmallTrees_Hist2,MSmallTrees_Hist3,MSmallTrees_Hist4,MBigTrees_Hist1,MBigTrees_Hist2,MBigTrees_Hist3,MBigTrees_Hist4]).sum(axis=0)
MHist_Mort=(MLandscapeHistoric[0:12]-MLandscapeHistoric[1:13])/4

MLandscapeNormal=np.array([MSmallTrees_Norm1,MSmallTrees_Norm2,MSmallTrees_Norm3,MSmallTrees_Norm4,MBigTrees_Norm1,MBigTrees_Norm2,MBigTrees_Norm3,MBigTrees_Norm4]).sum(axis=0)
MNorm_Mort=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])/4

LLandscapeHistoric=np.array([LSmallTrees_Hist1,LSmallTrees_Hist2,LSmallTrees_Hist3,LSmallTrees_Hist4,LBigTrees_Hist1,LBigTrees_Hist2,LBigTrees_Hist3,LBigTrees_Hist4]).sum(axis=0)
LHist_Mort=(LLandscapeHistoric[0:12]-LLandscapeHistoric[1:13])/4
LLandscapeNormal=np.array([LSmallTrees_Norm1,LSmallTrees_Norm2,LSmallTrees_Norm3,LSmallTrees_Norm4,LBigTrees_Norm1,LBigTrees_Norm2,LBigTrees_Norm3,LBigTrees_Norm4]).sum(axis=0)
LNorm_Mort=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])/4

ULandscapeHistoric=np.array([USmallTrees_Hist1,USmallTrees_Hist2,USmallTrees_Hist3,USmallTrees_Hist4,UBigTrees_Hist1,UBigTrees_Hist2,UBigTrees_Hist3,UBigTrees_Hist4]).sum(axis=0)
UHist_Mort=(ULandscapeHistoric[0:12]-ULandscapeHistoric[1:13])/4
ULandscapeNormal=np.array([USmallTrees_Norm1,USmallTrees_Norm2,USmallTrees_Norm3,USmallTrees_Norm4,UBigTrees_Norm1,UBigTrees_Norm2,UBigTrees_Norm3,UBigTrees_Norm4]).sum(axis=0)
UNorm_Mort=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])/4





#### Normal ###### 
BT1=MBigTrees_Norm1[7:12]
ST1=MSmallTrees_Norm1[7:12]
BT2=MBigTrees_Norm2[7:12]
ST2=MSmallTrees_Norm2[7:12]
BT3=MBigTrees_Norm3[7:12]
ST3=MSmallTrees_Norm3[7:12]
BT4=MBigTrees_Norm4[7:12]
ST4=MSmallTrees_Norm4[7:12]
MLandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)
MSimulated_Mort=(MLandscapeIn[0:4]-MLandscapeIn[1:5])/4
MNorm_Drought_Mortality=MSimulated_Mort.sum()

BT1=UBigTrees_Norm1[7:12]
ST1=USmallTrees_Norm1[7:12]
BT2=UBigTrees_Norm2[7:12]
ST2=USmallTrees_Norm2[7:12]
BT3=UBigTrees_Norm3[7:12]
ST3=USmallTrees_Norm3[7:12]
BT4=UBigTrees_Norm4[7:12]
ST4=USmallTrees_Norm4[7:12]
ULandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)
USimulated_Mort=(ULandscapeIn[0:4]-ULandscapeIn[1:5])/4
UNorm_Drought_Mortality=USimulated_Mort.sum()

BT1=LBigTrees_Norm1[7:12]
ST1=LSmallTrees_Norm1[7:12]
BT2=LBigTrees_Norm2[7:12]
ST2=LSmallTrees_Norm2[7:12]
BT3=LBigTrees_Norm3[7:12]
ST3=LSmallTrees_Norm3[7:12]
BT4=LBigTrees_Norm4[7:12]
ST4=LSmallTrees_Norm4[7:12]
LLandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)
LSimulated_Mort=(LLandscapeIn[0:4]-LLandscapeIn[1:5])/4
LNorm_Drought_Mortality=LSimulated_Mort.sum()




####### Historic ##### 
BT1=MBigTrees_Hist1[7:12]
ST1=MSmallTrees_Hist1[7:12]
BT2=MBigTrees_Hist2[7:12]
ST2=MSmallTrees_Hist2[7:12]
BT3=MBigTrees_Hist3[7:12]
ST3=MSmallTrees_Hist3[7:12]
BT4=MBigTrees_Hist4[7:12]
ST4=MSmallTrees_Hist4[7:12]
MLandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)
MSimulated_Mort=(MLandscapeIn[0:4]-MLandscapeIn[1:5])/4
MHistoric_Drought_Mortality=MSimulated_Mort.sum()


BT1=LBigTrees_Hist1[7:12]
ST1=LSmallTrees_Hist1[7:12]
BT2=LBigTrees_Hist2[7:12]
ST2=LSmallTrees_Hist2[7:12]
BT3=LBigTrees_Hist3[7:12]
ST3=LSmallTrees_Hist3[7:12]
BT4=LBigTrees_Hist4[7:12]
ST4=LSmallTrees_Hist4[7:12]
LLandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)
LSimulated_Mort=(LLandscapeIn[0:4]-LLandscapeIn[1:5])/4
LHistoric_Drought_Mortality=LSimulated_Mort.sum()

BT1=UBigTrees_Hist1[7:12]
ST1=USmallTrees_Hist1[7:12]
BT2=UBigTrees_Hist2[7:12]
ST2=USmallTrees_Hist2[7:12]
BT3=UBigTrees_Hist3[7:12]
ST3=USmallTrees_Hist3[7:12]
BT4=UBigTrees_Hist4[7:12]
ST4=USmallTrees_Hist4[7:12]
ULandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)
USimulated_Mort=(ULandscapeIn[0:4]-ULandscapeIn[1:5])/4
UHistoric_Drought_Mortality=USimulated_Mort.sum()


USimulated_Mort=(ULandscapeHistoric[0:12]-ULandscapeHistoric[1:13])/4
USimAll_Historic=USimulated_Mort.sum()
LSimulated_Mort=(LLandscapeHistoric[0:12]-LLandscapeHistoric[1:13])/4
LSimAll_Historic=LSimulated_Mort.sum()
MSimulated_Mort=(MLandscapeHistoric[0:12]-MLandscapeHistoric[1:13])/4
MSimAll_Historic=MSimulated_Mort.sum()



USimulated_Mort=(ULandscapeNormal[0:12]-ULandscapeNormal[1:13])/4
USimAll_Normal=USimulated_Mort.sum()
LSimulated_Mort=(LLandscapeNormal[0:12]-LLandscapeNormal[1:13])/4
LSimAll_Normal=LSimulated_Mort.sum()
MSimulated_Mort=(MLandscapeNormal[0:12]-MLandscapeNormal[1:13])/4
MSimAll_Normal=MSimulated_Mort.sum()


UNormal=[USimAll_Normal-UNorm_Drought_Mortality,UNorm_Drought_Mortality]
UHistoric=[USimAll_Historic-UHistoric_Drought_Mortality,UHistoric_Drought_Mortality]

MNormal=[MSimAll_Normal-MNorm_Drought_Mortality,MNorm_Drought_Mortality]
MHistoric=[MSimAll_Historic-MHistoric_Drought_Mortality,MHistoric_Drought_Mortality]

LNormal=[LSimAll_Normal-LNorm_Drought_Mortality,LNorm_Drought_Mortality]
LHistoric=[LSimAll_Historic-LHistoric_Drought_Mortality,LHistoric_Drought_Mortality]

LowERNormal=[MNormal[0]-LNormal[0],MNormal[1]-LNormal[1]]
HighERNormal=[UNormal[0]-MNormal[0],UNormal[1]-MNormal[1]]

LowERHistoric=[MHistoric[0]-LHistoric[0],MHistoric[1]-LHistoric[1]]
HighERHistoric=[UHistoric[0]-MHistoric[0],UHistoric[1]-MHistoric[1]]

#fig = plt.figure(figsize=(20,10))

#print(Historic,Normal)
plt.gca().set_title('b)',fontsize=20,loc="left")
barWidth = 0.25
r1 = np.arange(len(UNormal))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
#Make the plo
rects2=plt.bar(r1,MHistoric,yerr=(LowERHistoric,HighERHistoric), color=color2, width=barWidth, error_kw=dict(lw=3, capsize=5, capthick=1),edgecolor='white', label='Historical Mortality')
rects=plt.bar(r2, MNormal,yerr=( LowERNormal ,HighERNormal),color=color1,width=barWidth, error_kw=dict(lw=3, capsize=5, capthick=1), edgecolor='white', label='Contemporary Mortality')

# Add xticks on the middle of the group bars
#plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(UNormal))],["Non-Drought Period","Drought Period"])
plt.tick_params(labelsize=20)
# Create legend & Show graphic
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(round(height,2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0,20),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',size=15)
autolabel(rects)
autolabel(rects2)
plt.ylim(0,40)
plt.xticks(rotation=45)
#plt.xlabel("Trees surviving",fontsize=20)
plt.ylabel("Trees Killed per Hectare",fontsize=20)
#plt.xlabel("Year",fontsize=20)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=18)
#plt.suptitle("Trees Killed Greater than 10 cm",fontsize=20,y=1.05)
legend=plt.legend(fontsize=17,frameon=False,loc='upper left');


#ax.set_xticks([])
plt.savefig('Fig3.png',dpi=200,bbox_inches='tight')


