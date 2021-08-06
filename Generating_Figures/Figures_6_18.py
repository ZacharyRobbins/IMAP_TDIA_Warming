 # -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 17:30:57 2020

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

#fig, axs = plt.subplots(2,figsize=(20,20))
#fig.autofmt_xdate()
#fig.tight_layout()


### Figure 1 Validations

plt.figure(figsize=(20,10))
fig.autofmt_xdate()
fig.tight_layout()
barWidth = 0.20
r1 = np.arange(len(Obs_MortL))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5= [x + barWidth for x in r4]

plt.subplot(121)
plt.gca().set_title('a)',fontsize=20,loc="left")
#Make the plot
plt.bar(r1, MNorm_MortS,yerr=(MNorm_MortS-LNorm_MortS , UNorm_MortS-MNorm_MortS) ,error_kw=dict(lw=2, capsize=2, capthick=3),color=color1, width=barWidth, edgecolor='white', 
        label='Simulated: Small Hosts')
plt.bar(r2, Obs_MortS, color='#7f6d5f', width=barWidth, edgecolor='white', label='FIA: Small Hosts')
plt.bar(r3, MNorm_MortL,yerr=(MNorm_MortL-LNorm_MortL , UNorm_MortL-MNorm_MortL) ,hatch="/",error_kw=dict(lw=2, capsize=2, capthick=3),
        color=color1, width=barWidth, edgecolor='white', label='Simulated: Large Hosts')
plt.bar(r4, Obs_MortL, color='#7f6d5f', width=barWidth, edgecolor='white' ,hatch="/",label='FIA: Large Hosts')
 #Add xticks on the middle of the group bars#
plt.xlabel('group', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(Obs_MortL))], np.arange(2007,2019,1))
 
# Create legend & Show graphic
plt.ylim(0,15)
#plt.xlabel("Trees surviving",fontsize=20)
plt.ylabel("Trees Killed per Hectare",fontsize=20)
plt.xlabel("Year",fontsize=20)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=20)
#plt.suptitle("Trees Killed Greater than 31.6 cm",fontsize=40)

plt.tick_params(labelsize=20)
plt.xticks(rotation=45)
legend=plt.legend(fontsize=20,frameon=False,loc='upper left');
plt.gca().add_patch(Rectangle((4.8,0), 5.0, 40, facecolor="red",alpha=.05))
ax = legend.axes
from matplotlib.patches import Patch
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='red', alpha=.1))
labels.append("Drought Period")
legend._legend_box = None
legend._init_legend_box(handles, labels)
legend._set_loc(legend._loc)
legend.set_title(legend.get_title().get_text())


### 1b
Validationset=pd.read_csv("C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/Figures_NCC/WPB_Data2/MortValues_Reg.csv")
AllT=Validationset.Sim
LandscapeT=Validationset.Obs

from scipy import stats
plt.subplot(122)
plt.gca().set_title('b)',fontsize=20,loc="left")
plt.scatter(AllT,LandscapeT,color=color1,alpha=.5,s=100)
linreg = stats.linregress(AllT,LandscapeT)
plt.plot(AllT, linreg.intercept + linreg.slope*AllT, 'r',label="Regression between model and data",
         color=color1)
plt.xlabel('Actual Host Mortality',size=20)
plt.ylabel('Predicted Host Mortality',size=20)
ident = [0.0, 71.5]
plt.plot(ident,ident,"black",linestyle='dotted',label="1:1 line")
plt.ylim(-2.5,22.5)
plt.xlim(-2.5,22.5)

plt.text(-2, 21.0, ("$R^2$="+str(round(linreg.rvalue,2))),size=30)
#plt.text(-2,19.2, ("p-value="+str(round(linreg.pvalue,19))),size=60)
plt.tick_params(labelsize=25)
plt.legend(loc=4, prop={'size': 15})
#plt.plot((linreg.intercept + linreg.slope*AllT)+stats.norm.ppf(95)*linreg.stderr)

plt.savefig('WPB_GCB_1.png',dpi=200)










##### Figure 2 (Generations,Larval,Flight)
#####
#####
Flight_DF=pd.read_csv("FlightOut_3_1.csv")



LowERFlight=np.array([Flight_DF.Mq-Flight_DF.Lowq])
HighERFlight=np.array([Flight_DF.Highq-Flight_DF.Mq])
HLowERFlight=np.array([Flight_DF.MqH-Flight_DF.LowqH])
HHighERFlight=np.array([Flight_DF.HighqH-Flight_DF.MqH])


#Generations2=Generations
#Generations.Observed2=np.int(Generations.Observed)
# As an example, the quickest generation in 2016 was conducted in historic driver between June -11 and August 12 or in 66 days. June -8 and August 11 or in 64 days.  9/24
Generations=pd.read_csv("Compare_Generations_Median.csv")
#fig.autofmt_xdate()
6296/365
17.24*3

Generations.Observed.max()/17.24


plt.figure(figsize=(15,15))
#plt.subplots_adjust(right=.9,top=.5)
#fig.tight_layout()


#fig.tight_layout()


plt.figure(figsize=(10,12))
#plt.subplot(221)
#plt.tight_layout()
#plt.figure(figsize=(20,20))
#plt.plot(list(range(1,len(Generations.Observed)+2,len(Generations.Observed))),list(range(0,19,17)),color='black',linewidth=2.0,alpha=.1)
plt.plot(list(range(1,len(Generations.Observed)+2,len(Generations.Observed))),list(range(0,36,35)),color='black',linewidth=3.0,alpha=.1)
plt.plot(list(range(1,len(Generations.Observed)+2,len(Generations.Observed))),list(range(0,53,52)),color='black',linewidth=3.0,alpha=.1)
plt.plot(list(range(1,len(Generations.Observed)+2,len(Generations.Observed))),list(range(0,71,70)),color='black',linewidth=3.0,alpha=.1)
#plt.axhline(y=52, color='r', linestyle='-')
plt.plot(Generations.Historic, color=color2, linewidth=5.0,label="Historical")
plt.plot(Generations.Observed, color=color1, linewidth=5.0,label="Contemporary")
plt.text(2000, 56, '4 generations per year',size=30.0,  rotation=50,alpha=.6)
plt.text(2250, 47, '3 generations per year',size=30.0,  rotation=40,alpha=.6)
plt.text(2500, 30.2, '2 generations per year',size=30.0,  rotation=30,alpha=.6)

plt.xticks(list(range(1,len(Generations.Observed),365*2)), np.arange(2001,2018,2))



plt.ylabel("Generations Completed",fontsize=30)
plt.xlabel("Year",fontsize=30)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=30)
plt.xticks(rotation=45)
#plt.suptitle("Annual flight at all sites",fontsize=40)
plt.legend(fontsize=25,frameon=False);
legend=plt.legend(fontsize=30,frameon=False,loc='upper left');
plt.gca().add_patch(Rectangle((4000.8,-10), 1800.9, 100000, facecolor="red",alpha=.1))
ax = legend.axes
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='red', alpha=.1))
labels.append("Drought Period")
legend._legend_box = None
legend._init_legend_box(handles, labels)
legend._set_loc(legend._loc)
legend.set_title(legend.get_title().get_text())

plt.gca().set_title('a)',fontsize=20,loc="left")
barWidth = 0.45
jet = plt.get_cmap('Dark2') 
plt.savefig('WPB_GCB_2_1.png',dpi=200,bbox_inches='tight')


#plt.subplot(222)

plt.figure(figsize=(10,12))
Mortality=pd.read_csv("Mortality_Events_New.csv")
Observed_Mort=Mortality.loc[Mortality.Simulation=="Observed"]
Historic_Mort=Mortality.loc[Mortality.Simulation=="Historic"]


np.mean(Historic_Mort.Average_Larval_Percent*100)-np.mean(Observed_Mort.Average_Larval_Percent*100)




barWidth = 0.4
r1 = np.arange(len(Historic_Mort.Year))
r2 = [x + barWidth for x in r1]
#fig.autofmt_xdate()
plt.bar(r1,Historic_Mort.Average_Larval_Percent*100, color=color2, width=barWidth, edgecolor='white', label='Historical')
plt.bar(r2,Observed_Mort.Average_Larval_Percent*100, color=color1, width=barWidth, edgecolor='white', label='Contemporary')
plt.xticks([r + barWidth for r in range(len(Historic_Mort.Year))], np.arange(2001,2019,1))
plt.ylabel("Average Percent Larval Mortality",fontsize=30)
plt.xlim(6.7,18)
plt.xlabel("Year",fontsize=30)
plt.ylim(0.0,7)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=30)
plt.xticks(rotation=45)
#plt.suptitle("Annual flight at all sites",fontsize=40)
legend=plt.legend(fontsize=25,frameon=False,loc='upper left');
#plt.legend(fontsize=20,frameon=False);
plt.gca().add_patch(Rectangle((10.8,-10),4.9, 100000, facecolor="red",alpha=.1))
ax = legend.axes
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='red', alpha=.1))
labels.append("Drought Period")
legend._legend_box = None
legend._init_legend_box(handles, labels)
legend._set_loc(legend._loc)
legend.set_title(legend.get_title().get_text())

plt.gca().set_title('b)',fontsize=20,loc="left")
barWidth = 0.20
jet = plt.get_cmap('Accent') 
plt.savefig('WPB_GCB_2_2.png',dpi=200,bbox_inches='tight')


plt.subplot(223)
#flight=pd.DataFrame(data={"Flight":Flight_DF.MeanN})
#flight.index=pd.to_datetime(Flight_DF.Dates)
#Frs=flight.resample('Y').sum()
#flight=pd.DataFrame(data={"Flight":Flight_DF.MeanH})
#flight.index=pd.to_datetime(Flight_DF.Dates)
#HFrs=flight.resample('Y').sum()

#pd.DataFrame({'index':Frs.index,'FlightObs':Frs,'FlighHis':HFrs})
#Annuals=HFrs.merge(Frs,left_on='Dates',right_on='Dates')
#Xhange=(Frs-HFrs)/Frs 

#print(Xhange)
#fig.autofmt_xdate()

plt.figure(figsize=(10,12))
#plt.subplots_adjust(right=.9,top=.5)
barWidth = 0.45
r1 = np.arange(len(Flight_DF.MqH))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
#Make the plot
plt.bar(r1,Flight_DF.MqH, color=color2,  yerr=( np.array(HLowERFlight)[0],np.array(HHighERFlight)[0]), 
        error_kw=dict(lw=2, capsize=5, capthick=2), 
width=barWidth, edgecolor='white', label='Historical')
plt.bar(r2,Flight_DF.Mq, color=color1, yerr=( np.array(LowERFlight)[0],np.array(HighERFlight)[0]), 
        error_kw=dict(lw=2, capsize=5, capthick=2), 
        width=barWidth, edgecolor='white', label='Contemporary')

# Add xticks on the middle of the group bars
#plt.xlabel('group', fontweight='bold')
plt.xticks([r +  barWidth for r in range(len(Flight_DF.Mq))], np.arange(2001,2019,1))
plt.xlim(6.7,18)
# Create legend & Show graphic
#plt.xlim(2008,2018)
#plt.xlabel("Trees surviving",fontsize=20)
plt.ylabel("Annual Beetles in Flight",fontsize=30)
plt.xlabel("Year",fontsize=30)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=30)
plt.xticks(rotation=45)
plt.gca().set_title('c)',fontsize=20,loc="left")
r1
legend=plt.legend(fontsize=25,frameon=False,loc='upper left');
plt.gca().add_patch(Rectangle((10.8,0), 4.9, 1000000, facecolor="red",alpha=.1))
ax = legend.axes
handles, labels = ax.get_legend_handles_labels()
handles.append(Patch(facecolor='red', alpha=.1))
labels.append("Drought Period")
legend._legend_box = None
legend._init_legend_box(handles, labels)
legend._set_loc(legend._loc)
legend.set_title(legend.get_title().get_text())
plt.savefig('WPB_GCB_2_3.png',dpi=200,bbox_inches='tight')

#plt.savefig("Images/Barplot_Large.png")


##at 2012-01-01 : Hisotric 19.97 obs is at 24.83
##at 2016-01-01 historic is 28.74 obs is at 35.05
(35.05-24.83)-(28.74-19.97)

##at 2012-01-01 : Hisotric 26.68 obs is at 33.569
##at 2016-01-01 historic is 38.80 obs is at 48.0781
(48.08-33.569)-(38.80-26.68)

###For the 90th percentile 
#(37.2948-)-(33.4765-26.39)
.98/4
1.5/4
### for the 50th percentile
(43.0557-30.35)-(37.64-26.39)
#Generations.Historic[4000]
1.4557/4


plt.savefig('WPB_GCB_2.png',dpi=200)

##########
##################End 2
###########

### Climate optional
###Panel 2 
plt.figure(figsize=(10,7))
#fig.tight_layout()
plt.subplots_adjust(top=.9)
plt.subplot(111)
#plt.gca().set_title('b)',fontsize=20,loc="left")
Dates_Temp=pd.read_csv("Temp_Historical.csv")
plt.plot(Dates_Temp.Dates,Dates_Temp.History,'o',color=color2, markersize=10,label="Historical")
plt.plot(Dates_Temp.Dates,Dates_Temp.Observed,'o',color=color1, markersize=10,label="Contemporary")
plt.ylabel("Temperature $^\circ$C",fontsize=20)
plt.xlabel("Month",fontsize=20)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=17)
#plt.suptitle("Trees Killed Greater than 31.6 cm",fontsize=40)
plt.legend(fontsize=20,frameon=False,loc='upper left');
plt.tick_params(labelsize=20)
#plt.xticks(rotation=45)
plt.savefig('WPB_GCB_Climate.png',dpi=200)


#### Fig 4 ###
#######################################################



























########################## BEGIN FIGURE 2

#### Panel Four 
MortPheno=pd.read_csv("MortPheno_3_1.csv")
Lowq_Normal=MortPheno['Lowq_Normal']
Mq_Normal=MortPheno['Mq_Normal']
Highq_Normal=MortPheno['Highq_Normal']
Lowq_HPheno=MortPheno['Lowq_HPheno']
Mq_HPheno=MortPheno['Mq_HPheno']
Highq_HPheno=MortPheno['Highq_HPheno']
Lowq_HMort=MortPheno['Lowq_HMort']
Mq_HMort=MortPheno['Mq_HMort']
Highq_HMort=MortPheno['Highq_HMort']
Lowq_Historic=MortPheno['Lowq_Historic']
Mq_Historic=MortPheno['Mq_Historic']
Highq_Historic=MortPheno['Highq_Historic']


def SortingitOut(Input):
    BigTrees1=Input[0:13]
    BigTrees2=Input[13:26]
    BigTrees3=Input[26:39]
    BigTrees4=Input[39:52]
    SmallTrees1=Input[52:65]
    SmallTrees2=Input[65:78]
    SmallTrees3=Input[78:91]
    SmallTrees4=Input[91:104]
    Landscape=np.array([BigTrees1,BigTrees2,BigTrees3,BigTrees4,
                            SmallTrees1,SmallTrees2,SmallTrees3,SmallTrees4]).sum(axis=0)
    Mort=(Landscape[0:12]-Landscape[1:13])/4
    Total=Mort.sum()

    BT1=BigTrees1[7:12]
    ST1=SmallTrees1[7:12]
    BT2=BigTrees2[7:12]
    ST2=SmallTrees2[7:12]
    BT3=BigTrees3[7:12]
    ST3=SmallTrees3[7:12]
    BT4=BigTrees4[7:12]
    ST4=SmallTrees4[7:12]
    LandscapeIn=np.array([BT1,BT2,BT3,BT4,ST1,ST2,ST3,ST4]).sum(axis=0)

    Mort=(LandscapeIn[0:4]-LandscapeIn[1:5])/4
    Drought_Mortality=Mort.sum()
    
    return(Total,Drought_Mortality)
### Historic 
Highq_Historic_Total,Highq_Historic_DM=SortingitOut(Highq_Historic)
Mq_Historic_Total,Mq_Historic_DM=SortingitOut(Mq_Historic)
Lowq_Historic_Total,Lowq_Historic_DM=SortingitOut(Lowq_Historic)


Highq_HPheno_Total,Highq_HPheno_DM=SortingitOut(Highq_HPheno)
Mq_HPheno_Total,Mq_HPheno_DM=SortingitOut(Mq_HPheno)
Lowq_HPheno_Total,Lowq_HPheno_DM=SortingitOut(Lowq_HPheno)


Highq_HMort_Total,Highq_HMort_DM=SortingitOut(Highq_HMort)
Mq_HMort_Total,Mq_HMort_DM=SortingitOut(Mq_HMort)
Lowq_HMort_Total,Lowq_HMort_DM=SortingitOut(Lowq_HMort)

Highq_Normal_Total,Highq_Normal_DM=SortingitOut(Highq_Normal)
Mq_Normal_Total,Mq_Normal_DM=SortingitOut(Mq_Normal)
Lowq_Normal_Total,Lowq_Normal_DM=SortingitOut(Lowq_Normal)



LowERHistoric=[Mq_Historic_Total-Lowq_Historic_Total,Mq_Historic_DM-Lowq_Historic_DM]
HighERHistoric=[Highq_Historic_Total-Mq_Historic_Total,Highq_Historic_DM-Mq_Historic_DM]

LowERHMort=[Mq_HMort_Total-Lowq_HMort_Total,Mq_HMort_DM-Lowq_HMort_DM]
HighERHMort=[Highq_HMort_Total-Mq_HMort_Total,Highq_HMort_DM-Mq_HMort_DM]

LowERNormal=[Mq_Normal_Total-Lowq_Normal_Total,Mq_Normal_DM-Lowq_Normal_DM]
HighERNormal=[Highq_Normal_Total-Mq_Normal_Total,Highq_Normal_DM-Mq_Normal_DM]

LowERHPheno=[Mq_HPheno_Total-Lowq_HPheno_Total,Mq_HPheno_DM-Lowq_HPheno_DM]
HighERHPheno=[Highq_HPheno_Total-Mq_HPheno_Total,Highq_HPheno_DM-Mq_HPheno_DM]


### Panel four
###Panel 2 
plt.figure(figsize=(10,10))
plt.subplot(111)
#lt.gca().set_title('d)',fontsize=20,loc="left")
#print(Historic,Normal)
barWidth = 0.20
#fig,ax=plt.subplots(figsize=(20,20))
fig.autofmt_xdate()
fig.tight_layout()
Observed=[Mq_Normal_Total,Mq_Normal_DM]
HistoricMortal=[Mq_HMort_Total,Mq_HMort_DM]
HistoricPheno=[Mq_HPheno_Total,Mq_HPheno_DM]
HistoricAll=[Mq_Historic_Total,Mq_Historic_DM]
r1 = np.arange(len(HistoricAll))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
#Make the plo
rects2=plt.bar(r4,HistoricAll, yerr=( LowERHistoric ,HighERHistoric), error_kw=dict(lw=2, capsize=10, capthick=2), color=color2, width=barWidth, edgecolor='white',
              label='Historical Development, Historical Mortality')
rects3=plt.bar(r3,HistoricPheno, yerr=( LowERHPheno ,HighERHPheno), error_kw=dict(lw=2, capsize=10, capthick=2),color='darkmagenta', width=barWidth,
             edgecolor='white',
              label='Historical Development, Contemporary Mortality')
rects=plt.bar(r2, HistoricMortal,color=jet(2),width=barWidth,
             edgecolor='white', yerr=( LowERHMort ,HighERHMort), error_kw=dict(lw=2, capsize=10, capthick=2), 
             label="Contemporary Development, Historical Mortality")
rects4=plt.bar(r1,Observed, yerr=( LowERNormal ,HighERNormal), error_kw=dict(lw=2, capsize=10, capthick=2),color=color1, width=barWidth, 
              edgecolor='white', label='Contemporary Development, Contemporary Mortality')




plt.legend( prop={'size': 15},frameon=False)



def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(round(height,2)),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 20),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom',size=15)
# Add xticks on the middle of the group bars
plt.xlabel('', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(Observed))],["Total Simulation","Drought Period"])
plt.tick_params(labelsize=0)
plt.ylim(0,45)
#plt.xlabel("Trees surviving",fontsize=20)
plt.ylabel("Trees Killed per Hectare",fontsize=20)
#plt.xlabel("Year",fontsize=50)
#plt.ylabel("Trees surviving",fontsize=40)
plt.tick_params(labelsize=20)
autolabel(rects)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

#ax.set_xticks([])
plt.savefig('WPB_Figure4.png',dpi=200)