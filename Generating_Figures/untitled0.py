# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:18:27 2021

@author: zacha
"""



import pandas as pd
w_dir="C:/Users/zacha/Desktop/Scrpple_72921/Inputs/"
out_dir="C:/Users/zacha/Desktop/Scrpple_72921/Outputs/"
climateday=pd.read_csv(out_dir+ "climate_runs.csv")
fwi_date=pd.read_csv(w_dir+"Climate_Log_FWI_728.csv")
#finefuels=pd.read_csv("R:/fer/rschell/Robbins/Sapps/Model_Prep/Scrapple_Prep/Spread/finefuels.csv")
wsv=pd.read_csv(w_dir+"Wind_Gridmet.csv")
frame=pd.DataFrame()
climateday.rename(columns={'Unnamed: 0': 'ID','X11_Ecoregions.1':'wind_region',
                           'V2':'date'}, inplace=True)
wsv.rename(columns={'Unnamed: 0': "date"}, inplace=True)
fwi_date.rename(columns={'Unnamed: 0': "date"}, inplace=True)
fwi_date['Month']=pd.to_datetime(fwi_date['Timestep'], format='%j').dt.strftime('%m')
fwi_date['Day']=pd.to_datetime(fwi_date['Timestep'], format='%j').dt.strftime('%d')
fwi_date['Date']=pd.to_datetime(fwi_date[['Year', 'Month','Day']],errors='coerce')



for i in list(range(0,(len(climateday)-1))):
    print(i)
    fire_cell_select=climateday.iloc[i,]
    fire_ID=fire_cell_select.ID
    windregion=fire_cell_select.wind_region
    wsv_day=wsv.loc[wsv.date==(fire_cell_select.date+'T00:00:00Z'),]
    wsvday=wsv_day.iloc[0,fire_cell_select.wind_region]
        
    
    fwi_day=fwi_date.loc[fwi_date.Date==fire_cell_select.date,]
    fwiday=fwi_day.loc[fwi_day.EcoregionName.values==" eco"+str(windregion),]
    fwiday=fwiday.iloc[:,26]
    fwi=float(fwiday.values)
    ## This is not nessecary now that we use the LANDIS_+II inputs
    #fuelslocate=finefuels.loc[finefuels.fueltype==fire_cell_select.fuel_number,]
    #fuelslocate=fuelslocate.iloc[0,2]
    fuelslocation=fire_cell_select.InterpolatedFuels
    
    FWI=pd.DataFrame([[fire_ID,fwi]],columns=["FireID","FWI"])
    Fuels=pd.DataFrame([[fire_ID,fuelslocation]],columns=["FireID","Fuels"])
    WSV=pd.DataFrame([[fire_ID,wsvday]],columns=["FireID","WSV"])
    One=pd.merge(FWI,Fuels, how='inner', on="FireID")
    Two=pd.merge(One,WSV,how='inner', on="FireID" )
    frame=frame.append(Two)    

ClimateFuel_Df=pd.DataFrame(frame)
ClimateFuel_Df.to_csv(w_dir+"ClimateFuel_Df.csv")
