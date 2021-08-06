library(rFIA)
library(rgdal)
library(raster)
library(sf)
library(rgeos)
Drive<-'C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/'
ShapesDir<-"C:/Users/zacha/Maps/WPB/"
One<-read_sf(paste0(ShapesDir,"HE_HL_WPB.shp"))
Two<-read_sf(paste0(ShapesDir,"HE_LL_WPB.shp"))
st_crs(Two)<-st_crs(One)
One <- st_buffer(One, 0)
Two<- st_buffer(Two, 0)
set_1<-st_union(One,Two)
plot(set_1)
Three<-read_sf(paste0(ShapesDir,"HE_HL_WPB.shp"))
Four<-read_sf(paste0(ShapesDir,"HE_LL_WPB.shp"))
st_crs(Three)<-st_crs(One)
st_crs(Four)<-st_crs(One)
Three <- st_buffer(Three, 0)
Four<- st_buffer(Four, 0)
set_2<-st_union(Three,Four)
set_3<-st_union(set_1,set_2)
plot(set_3)
##Set projection for project 
proj<-("+init=epsg:4326 +proj=longlat +datum=WGS84 +no_defs +ellps=WGS84 +towgs84=0,0,0")
###StudyArea to clip to 
SNV_Outline<-read_sf(paste0(Drive,"Inputs/StudyArea/New_Study_Area.shp"))
# #To LAT:LONG
SNV_Outline<-st_transform(SNV_Outline,crs(proj))
plot(SNV_Outline)
CA_FIA=getFIA(states='CA')
Clipped=clipFIA(CA_FIA,SNV_Outline,mostRecent = F)
Out=tpa(Clipped,treeType = "all",
        method='TI',
        treeDomain =SPCD==122&  DIA>3.93,
        areaDomain = ELEV >1312& ELEV< 7217,
    nCores = 4)
Out$TPA*Out$TPA_SE*.01
1.388906/(271**.5)