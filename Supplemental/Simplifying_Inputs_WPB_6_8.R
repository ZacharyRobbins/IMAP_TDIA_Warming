library(sf)
library(rgdal)
library(plyr)
library(raster)
library(RColorBrewer)
library(dplyr)
options(scipen = 1e8)
Dark2<-brewer.pal(8,'Dark2')
ff<-function(x){
  return(as.numeric(as.character(x)))
}
Pal_1<-brewer.pal(9,"Set3")

'%!in%' <- function(x,y)!('%in%'(x,y))

dft<-function(x){as.data.frame(table(x))}


###Check for points per raster
Drive<-'C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/'
###Prepare Tree File
Years<-seq(2005,2018)

CA_Tree<-read.csv(paste0(Drive,'Inputs/Input_Data_Scripts/CA_TREE.csv'))
CA_Tree<-CA_Tree[CA_Tree$INVYR %in% Years,]

##Set projection for project 
proj<-("+init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0")

### Data Location 
FIA_Dir<-paste0(Drive,'Input_Data_Scripts/')
##FIA_Plot location 
CA_Plot<-read.csv(paste0(Drive,'Inputs/Input_Data_Scripts/CA_PLOT.csv'))
###Remove data without geolocation 
CA_Plot<-CA_Plot[!is.na(CA_Plot$LAT),]
CA_Plot<-CA_Plot[!is.na(CA_Plot$LON),]

###StudyArea to clip to 
SNV_Outline<-readOGR(paste0(Drive,"Inputs/StudyArea/New_Study_Area.shp"))
# #To LAT:LONG
SNV_Outline<-spTransform(SNV_Outline,crs(proj))

#length(unique(CA_Plot$CN))
LL_Points<-cbind(CA_Plot['LON'],CA_Plot['LAT'])
LL_Points<-na.omit(LL_Points)

### Make into spatial points
sp_LL<-sp::SpatialPoints(LL_Points,proj4string = CRS(proj))

## Create the plots as a shape 
DT_sf = sf::st_as_sf(CA_Plot, coords = c("LON", "LAT"), 
                     crs = 4326, agr='constant')
#Do the Intesection
Plots_In_AOI<-sf::st_intersection(sf::st_as_sf(DT_sf),sf::st_as_sf(SNV_Outline))
### Get cordinates back
XYS<-st_coordinates(Plots_In_AOI)

###Check out geospatial locations
par(mar=c(5,5,5,5))
plot(sf::st_geometry(sf::st_as_sf(SNV_Outline)),axes=TRUE)
plot(sf::st_geometry(Plots_In_AOI),cex=.1,add=TRUE,axes=TRUE)

###Number of plots is 3505



### Find  the plots in that are in the area.  Remains at 3504 
Plots<-as.data.frame(CA_Plot[CA_Plot$CN %in% Plots_In_AOI$CN,])

### Get the elevation from each plot in meters
Plots$ELEV_m<-Plots$ELEV*.3408

SortPlots<-function(one,Sp){
  
  PltsSorted<-Plots[Plots$ELEV_m>one$LowEl & Plots$ELEV_m<one$HighEl,]
  PltsSorted<-PltsSorted[PltsSorted$LAT>one$LatLow & PltsSorted$LAT<one$LatHigh,]
  #PltsSorted<-PltsSorted[PltsS]
  hist(PltsSorted$INVYR,breaks=c(50))
  Subset<-CA_Tree %>%
    ### Get just one plot
    subset(CA_Tree$PLT_CN %in% PltsSorted$CN)%>%  # %>%
    ## Subset to just species of intrest (for now).
    subset(SPCD %in% Sp) %>%
    # ### Get Ht in M
    mutate(DIA_cm= (DIA*2.54))
  Subset<-Subset[,c("PLT_CN","INVYR","SPCD","DIA_cm","MORTYR","TPA_UNADJ")]
  hist(Subset$INVYR)
  return(Subset)
}

Cal_Mort<-function(Subset){
  UPY<-Subset %>%
    group_by(INVYR,PLT_CN)%>%
    summarise_at(vars("TPA_UNADJ"),list(sum=sum))
  HasTrees<-UPY[!is.na(UPY$sum),]
  Relevent_Plots<-Subset[Subset$PLT_CN %in% HasTrees$PLT_CN,]
  Relevent_Plots$MORTYR[Relevent_Plots$MORTYR==30|Relevent_Plots$MORTYR==80]<-NA
  MORTYR<-Relevent_Plots %>%
    group_by(year=MORTYR)%>% 
    dplyr::summarise(n())
  MORTYR$year<-MORTYR$year-1
  ALLYR<-Relevent_Plots %>%
    group_by(year=INVYR)%>% 
    dplyr::summarise(n())
  ALLYR$mean=mean(ALLYR$`n()`)
  
  MortalityTable<-merge(MORTYR,ALLYR,by='year',all.y=T)
  MortalityTable[is.na(MortalityTable)]<-0
  MortalityTable$per<-MortalityTable$`n().x`/(MortalityTable$mean+MortalityTable$`n().x`)
  # MortalityTable$per<-MortalityTable$`n().x`/(MortalityTable$`n().y`+MortalityTable$`n().x`)
  
  return(MortalityTable)
}
CalculateTrees<-function(Subset){
  UPY<-Subset %>%
    group_by(INVYR,PLT_CN)%>%
    summarise_at(vars("TPA_UNADJ"),list(sum=sum,length=length))
  HasTrees<-UPY[!is.na(UPY$sum),]
  Relevent_Plots<-Subset[Subset$PLT_CN %in% HasTrees$PLT_CN,]
  Plots_Year<-Relevent_Plots[Relevent_Plots$INVYR%in%c(2005,2006),]
  TPA_1<-Plots_Year %>%
    group_by(INVYR,PLT_CN)%>%
    summarise_at(vars("TPA_UNADJ"),list(sum=sum))
  (TPH<-(sum(TPA_1$sum)*2.47105)/(length(unique(TPA_1$PLT_CN))))
  return(TPH)}

Sp=122

#PltsLUT<-data.frame(Name=c("UpperLow","UpperMed","UpperHigh","LowerLow","LowerMed","LowerHigh"),
#                    Patch=c(1,2,3,4,5,6),
#                    LowEl=c(400,914,1374, 400,914,1374),
#                    HighEl=c(1400,1371,1829,1400,1371,1829),
#                    LatLow=c(37.5,37.5,37.5,33,33,33),
#                    LatHigh=c(40,40,40,37.5,37.5,37.5))
PltsLUT<-data.frame(Name=c("UpperLow","UpperMed","HighLatitude","LowerLow","LowerMed","LowLatitude"),
                    Patch=c(1,2,3,4,5,6),
                    LowEl=c(400,1400,400, 800,1500,800),
                    HighEl=c(1400,2000,2000,1500,2200,2200),
                    LatLow=c(37.5,37.5,37.5,33,33,33),
                    LatHigh=c(40,40,40,37.5,37.5,37.5))



DF<-NULL
#one<-PltsLUT[1,]

for(i in c(1,2,4,5)){
  print(paste0("Study Area ",i))
  Subset<-SortPlots(PltsLUT[i,],Sp)
  Lrg<-Subset[Subset$DIA_cm>31.6,]
  #LrgSub<-Lrg[Lrg$INVYR %in% c(2005,2006),]
  Mortlrg<-Cal_Mort(Lrg)
  barplot(Mortlrg[[5]],names.arg=Mortlrg[[1]])
  Lrgtree<-CalculateTrees(Lrg)
  
  Smll<-Subset[Subset$DIA_cm<31.6|Subset$DIA_cm>10.0,]
  Smll<-Smll[!is.na(Smll$PLT_CN),]
  SmllSub<-Smll[Smll$INVYR %in% c(2005,2006),]
  Mortsmll<-Cal_Mort(Smll)
  barplot(Mortsmll[[5]],names.arg=Mortsmll[[1]])
  Smlltree<-CalculateTrees(Smll)
  #Smlltree[1]
  
  for(j in 1:10){
    Ms<-Mortsmll[[5]][3+j]
    print(paste0("ms=",Ms))
    Ml<-Mortlrg[[5]][3+j]
    print(paste0("ml=",Ml))
    #print(Mortlrg[[1]][3+j])
    Smlltree<-c(Smlltree,Smlltree[j]*(1-Ms))
    Lrgtree<-c(Lrgtree,Lrgtree[j]*(1-Ml))
  }
  plot(Smlltree)
  plot(Lrgtree)
  
  Row<-c(PltsLUT[i,1],round(Lrgtree),round(Smlltree))
  DF<-rbind(Row,DF)
}
DF_Out<-as.data.frame(DF)
colnames(DF_Out)<-c("Location","Initial_above_20","Large2008perc","Large2009perc",
                    "Large2010perc","Large2011perc","Large2012perc","Large2013perc",
                    "Large2014perc","Large2015perc",
                    "Large2016perc","Large2017perc","Initial_below_20","Small2008perc","Small2009perc",
                    "Small2010perc","Small2011perc","Small2012perc","Small2013perc",
                    "Small2014perc","Small2015perc","Small2016perc","Small2017perc")

DF_Out2<-DF_Out[,c(1,2,13,3:12,14:23)]

#write.csv(DF_Out2,paste0(Drive,"Inputs/WPB/WPB_Trees_5_29.csv"))



###All plots
PltsLUT[5,1]
Subset_North<-SortPlots(PltsLUT[3,],Sp)
Subset_South<-SortPlots(PltsLUT[6,],Sp)

Subset_All<-rbind(Subset_North,Subset_South)
Lrg<-Subset_All[Subset_All$DIA_cm>31.6,]
LrgSub<-Lrg[Lrg$INVYR %in% c(2005,2006),]
Mort<-Cal_Mort(Lrg)
barplot(Mort[[5]])
CalculateTrees(Lrg)

Smll<-Subset_All[Subset_All$DIA_cm<31.6|Subset_All$DIA_cm>10.0,]
Smll<-Smll[!is.na(Smll$PLT_CN),]
SmllSub<-Smll[Smll$INVYR %in% c(2005,2006),]
Mort<-Cal_Mort(Smll)
barplot(Mort[[5]])
CalculateTrees(Smll)


library(RColorBrewer)
Dark2<-brewer.pal(6,"Dark2")
#colnames(MPB3)
MPB3_plotter<-as.data.frame(DF_Out[,c(1:12)])
MPB3_plotter<-t(MPB3_plotter)
colnames(MPB3_plotter)<-MPB3_plotter[1,]
MPB3_plotter<-MPB3_plotter[-1,]
fix<-function(x){
  as.numeric(as.character(x))
}

Dates<-seq(
  from=as.POSIXct("2007-06-01 0:00", tz="UTC"),
  to=as.POSIXct("2017-06-01 0:00", tz="UTC"),
  by="year"
)  
#MPB3_plotter$Dates<-Dates

plot(MPB3_plotter[,1],ylim=c(0,250),xaxt='n',main="MPB Host(>20 cm) Tree Density Over Time",ylab="Tree Density Per Ha",xlab="Date",cex=1.5,cex.axis=1.5,cex.lab=1.5)
axis(1, at=1:11,labels =Dates, las=1,cex.axis=1.0,pch=15,cex=1.5,cex.axis=1.5,cex.lab=2.0)
##points(MPB3_plotter[,2],pch=16,col=Dark2[1],cex=1.5)
points(MPB3_plotter[,2],pch=17,col=Dark2[2],cex=1.5)
#points(MPB3_plotter[,4],pch=18,col=Dark2[3],cex=1.5)
points(MPB3_plotter[,3],pch=19,col=Dark2[4],cex=1.5)
points(MPB3_plotter[,4],pch=0,col=Dark2[5],cex=1.5)
legend(9.0,500,legend=c("LowLat_HE","LowLat_LE","HighLat_HE","HighLat_LE"),cex=1.5,pch=c(15,17,19,0),col=c("Black",Dark2[2],Dark2[3],Dark2[5]))

plot(fix(MPB3_plotter[,1])/fix(max(MPB3_plotter[,1])),pch=15,ylim=c(0,1.2),main="MPB Host(> 20 cm) Population remaining",xaxt='n',xlab="Date",ylab="Intial population remaining",cex=1.5,cex.axis=1.5,cex.lab=1.5)
axis(1, at=1:11,labels =Dates, las=1,cex=1.5,cex.axis=1.5,cex.lab=1.5)
#points(fix(MPB3_plotter[,2])/fix(max(MPB3_plotter[,2])),pch=16,col=Dark2[1],cex=1.5)
points(fix(MPB3_plotter[,2])/fix(max(MPB3_plotter[,2])),pch=17,col=Dark2[2],cex=1.5)
#points(fix(MPB3_plotter[,4])/fix(max(MPB3_plotter[,4])),pch=18,col=Dark2[3],cex=1.5)
points(fix(MPB3_plotter[,3])/fix(max(MPB3_plotter[,3])),pch=19,col=Dark2[4],cex=1.5)
points(fix(MPB3_plotter[,4])/fix(max(MPB3_plotter[,4])),pch=0,col=Dark2[5],cex=1.5)
legend(1.2,.3,legend=c("LowLat_HE","LowLat_LE","HighLat_HE","HighLat_LE"),cex=1.5,pch=c(15,17,19,0),col=c("Black",Dark2[2],Dark2[3],Dark2[5]))



MPB3_plotter<-as.data.frame(DF_Out[,c(1,13:23)])
MPB3_plotter<-t(MPB3_plotter)
colnames(MPB3_plotter)<-MPB3_plotter[1,]
MPB3_plotter<-MPB3_plotter[-1,]
fix<-function(x){
  as.numeric(as.character(x))
}

Dates<-seq(
  from=as.POSIXct("2007-01-01 0:00", tz="UTC"),
  to=as.POSIXct("2017-01-01 0:00", tz="UTC"),
  by="year"
)  


plot(MPB3_plotter[,1],ylim=c(0,250),xaxt='n',main="MPB Host(>20 cm) Tree Density Over Time",ylab="Tree Density Per Ha",xlab="Date",cex=1.5,cex.axis=1.5,cex.lab=1.5)
axis(1, at=1:11,labels =Dates, las=1,cex.axis=1.0,pch=15,cex=1.5,cex.axis=1.5,cex.lab=2.0)
##points(MPB3_plotter[,2],pch=16,col=Dark2[1],cex=1.5)
points(MPB3_plotter[,2],pch=17,col=Dark2[2],cex=1.5)
#points(MPB3_plotter[,4],pch=18,col=Dark2[3],cex=1.5)
points(MPB3_plotter[,3],pch=19,col=Dark2[4],cex=1.5)
points(MPB3_plotter[,4],pch=0,col=Dark2[5],cex=1.5)
legend(9.0,300,legend=c("LowLat_HE","LowLat_LE","HighLat_HE","HighLat_LE"),cex=1.5,pch=c(15,17,19,0),col=c("Black",Dark2[2],Dark2[3],Dark2[5]))

plot(fix(MPB3_plotter[,1])/max(fix(MPB3_plotter[,1])),pch=15,ylim=c(0,1.2),main="MPB Host(> 20 cm) Population remaining",xaxt='n',xlab="Date",ylab="Intial population remaining",cex=1.5,cex.axis=1.5,cex.lab=1.5)
axis(1, at=1:11,labels =Dates, las=1,cex=1.5,cex.axis=1.5,cex.lab=1.5)
#points(fix(MPB3_plotter[,2])/fix(max(MPB3_plotter[,2])),pch=16,col=Dark2[1],cex=1.5)
points(fix(MPB3_plotter[,2])/max(fix(MPB3_plotter[,2])),pch=17,col=Dark2[2],cex=1.5)
#points(fix(MPB3_plotter[,4])/fix(max(MPB3_plotter[,4])),pch=18,col=Dark2[3],cex=1.5)
points(fix(MPB3_plotter[,3])/max(fix(MPB3_plotter[,3])),pch=19,col=Dark2[4],cex=1.5)
points(fix(MPB3_plotter[,4])/max(fix(MPB3_plotter[,4])),pch=0,col=Dark2[5],cex=1.5)
legend(1.2,.5,legend=c("LowLat_HE","LowLat_LE","HighLat_HE","HighLat_LE"),cex=1.5,pch=c(15,17,19,0),col=c("Black",Dark2[2],Dark2[3],Dark2[5]))

