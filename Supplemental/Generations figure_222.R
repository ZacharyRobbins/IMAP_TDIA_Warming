#oviposition
sigma0 = 0.2458         # controls rate variability
TB0 = 7.750          #base temperature in degrees C
DeltaB0 = 10000
TM0 = 35.0           #max temperature in degree C
DeltaM0 = 2.0
omega0 = .0070
psi0 = 0.3200

#parameters for development rate for eggs
sigma1=.3     
Rmax1=0.184          
Tmax1=37.150
Tmin1= 6.38
k1= 1079.233
dm1 = 8.877


# parameters for development rate for larvae
sigma2=.3     
Rmax2=.030           
VTmx2=35.732
VTmn2= 4.768
k2= 784.489
dm2 = 6.847

# parameters for development rate for Prepupae
sigma3=.3     
Rmax3=0.223         
VTmx3=36.637
VTmn3= 6.12
k3= 402.00
dm3 = 9.613

# parameters for development rate for Pupae
sigma4=.3     
Rmax4=.054        
VTmx4=33.34
VTmn4= 6.54
k4= 179.92
dm4 = 10.55

# parameters for development rate for TA
sigma5=.3     
Rmax5=.01568408 
VTmx5=50.8
VTmn5= -0.002603655
k5= -0.003262513
dm5 = 0.0005461579
LoganFunc<-function(Temp,Rmax,Tmax,Tmin,k,dm,DevR){
  DevR =Rmax*(((((Temp-Tmin)**2)/(((Temp-Tmin)**2)+k))-(exp(-(Tmax-(Temp-Tmin))/dm))))
  return(DevR)
}
RegniereFunc<-function(TC,TB,DeltaB,TM,DeltaM,omega,psi){
  if(TC>=TB & TC<=TM){
  Fec1= psi*(exp(omega*(TC - TB)) - (TM - TC)/(TM - TB)*exp(-omega*(TC - TB)/DeltaB) - (TC - TB)/(TM - TB)*exp(omega*(TM - TB) - (TM - TC)/DeltaM))
  }else{Fec1=0}
  return(Fec1) 
}




#Tempmind<-
#Tempmind<-TR_Together_Min$DailyMin[!duplicated(TR_Together_Min$Date)]
#Tempmaxd<-TR_Together_Max$DailyMax[!duplicated(TR_Together_Max$Date)]
#Tempmaxd<-Tempmaxd
#DatesD<-TR_Together_Max$Date[!duplicated(TR_Together_Max$Date)]


Proccess_Rate<-function(Tempmind,Tempmaxd,DatesD){
  Fec=0
  Egg=0
  L1<-0
  L2<-0
  P<-0
  TA<-0
  Gen<-0
  time<-0
  Flycount=0
  landcount=0
  df<-NULL
  Flylog<-NULL
  Templog<-NULL
  
  ### For i 
  time<-0
  #length(Tempmind)
  for(i in 1:(length(Tempmind)-1)){
    time=time+1
    Tmaxstep=DatesD
    Tmintime=Tempmind[i]
    TminNext=Tempmind[i+1]
    TmaxTime=Tempmaxd[i]
    
    CMean=(TmaxTime+Tmintime)/2
    CMean2=(TmaxTime+TminNext)/2
    CDif=(TmaxTime-Tmintime)
    CDif2=(TmaxTime-TminNext)
    fouram=3.8532+(Tmintime*.9677)
    Tmin2=fouram
    sevenam=1.86978+(.93522*(CMean+(.5*CDif*-0.7071068)))
    tenam=(-.4533)+(1.00899*(CMean))
    onepm=(-1.148846)+(.985801*(CMean+(.5*CDif*0.7071068)))
    fourpm=(.0656866)+(.942395*(CMean+(.5*CDif*1)))
    sevenpm=(-0.702683)+(.979172*(CMean2+(.5*CDif2*0.7071068)))
    tenpm=.934665+(.988126*(CMean2))
    oneam=3.2294+(.9842*(CMean2+(.5*CDif2*-0.7071068)))
    Tmax2=fourpm
    
    
    
    #print(time)
    if(Fec<1){
      med0t1<- RegniereFunc(fouram, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t2<- RegniereFunc(sevenam, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t3<- RegniereFunc(tenam, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t4<- RegniereFunc(onepm, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t5<- RegniereFunc(fourpm, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t6<- RegniereFunc(sevenpm, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t7<- RegniereFunc(tenpm, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      med0t8<- RegniereFunc(oneam, TB0, DeltaB0, TM0, DeltaM0, omega0, psi0)   # for pre-eggs
      Fec_a=med0t1+med0t2+med0t3+med0t4+med0t5+med0t6+med0t7+med0t8
      
      Fec1<-1/(log(.50)/-Fec_a)
      
      
      if(Fec1<0){Fec1=0}
      
      Fec=(Fec1)+Fec
      if(Fec>1.0){
        Fec=1.0
        
      }
      
    }
    
    ### Need to remove the a's and i's in max
    
    ###Egg
    if(Fec==1.0&Egg<1){
      med1t1<-LoganFunc(fouram, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t2<-LoganFunc(sevenam, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t3<-LoganFunc(tenam, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t4<-LoganFunc(onepm, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t5<-LoganFunc(fourpm, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t6<-LoganFunc(sevenpm, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t7<-LoganFunc(tenpm, Rmax1,Tmax1,Tmin1,k1,dm1)
      med1t8<-LoganFunc(oneam, Rmax1,Tmax1,Tmin1,k1,dm1)
      Rate=med1t1+med1t2+med1t3+med1t4+med1t5+med1t6+med1t7+med1t8
      if(Rate<0){Rate=0}
      Egg=Egg+Rate
      if(Egg>1.0){
        Egg=1.0
      }
    }
    
    ###Larval
    
    if(L1<1 &Egg==1 & Fec==1){
      med2t1<-LoganFunc(fouram, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t2<-LoganFunc(sevenam, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t3<-LoganFunc(tenam, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t4<-LoganFunc(onepm, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t5<-LoganFunc(fourpm, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t6<-LoganFunc(sevenpm, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t7<-LoganFunc(tenpm, Rmax2,VTmx2,VTmn2,k2,dm2)
      med2t8<-LoganFunc(oneam, Rmax2,VTmx2,VTmn2,k2,dm2)
      Rate=med2t1+med2t2+med2t3+med2t4+med2t5+med2t6+med2t7+med2t8
      if(Rate<0){Rate=0}
      L1<-L1+Rate
      if(L1>1.0){
        L1=1.0}
    }
    ### Pre-Pupal
    
    if(L2<1 & L1==1 &Egg==1 & Fec==1){
      med3t1<-LoganFunc(fouram, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t2<-LoganFunc(sevenam, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t3<-LoganFunc(tenam, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t4<-LoganFunc(onepm, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t5<-LoganFunc(fourpm, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t6<-LoganFunc(sevenpm, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t7<-LoganFunc(tenpm, Rmax3,VTmx3,VTmn3,k3,dm3)
      med3t8<-LoganFunc(oneam, Rmax3,VTmx3,VTmn3,k3,dm3)
      Rate=med3t1+med3t2+med3t3+med3t4+med3t5+med3t6+med3t7+med3t8
     # if(fouram<12.8){Rate=0}
      if(Rate<0){Rate=0}
      L2<-L2+Rate
      if(L2>1.0){
        L2=1.0}
    }
    
    if(P<1 &L2==1 & L1==1 &Egg ==1 & Fec==1){
      med4t1<-LoganFunc(fouram, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t2<-LoganFunc(sevenam, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t3<-LoganFunc(tenam, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t4<-LoganFunc(onepm, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t5<-LoganFunc(fourpm, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t6<-LoganFunc(sevenpm, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t7<-LoganFunc(tenpm, Rmax4,VTmx4,VTmn4,k4,dm4)
      med4t8<-LoganFunc(oneam, Rmax4,VTmx4,VTmn4,k4,dm4)
      Rate=med4t1+med4t2+med4t3+med4t4+med4t5+med4t6+med4t7+med4t8
      if(Rate<0){Rate=0}
      P<-P+Rate
      if(P>1.0){
        P=1.0}
    }
    
    if(TA<1 &P==1 &L2==1 & L1==1 &Egg ==1 & Fec==1){
      med5t1<-LoganFunc(fouram, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t2<-LoganFunc(sevenam, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t3<-LoganFunc(tenam, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t4<-LoganFunc(onepm, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t5<-LoganFunc(fourpm, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t6<-LoganFunc(sevenpm, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t7<-LoganFunc(tenpm, Rmax5,VTmx5,VTmn5,k5,dm5)
      med5t8<-LoganFunc(oneam, Rmax5,VTmx5,VTmn5,k5,dm5)
      Rate=med5t1+med5t2+med5t3+med5t4+med5t5+med5t6+med5t7+med5t8
      if(Rate<0){Rate=0}
      TA<-TA+Rate
      if(TA>=1.0){TA=1.0}
    } 
    if(TA==1 &P==1 &L2==1 & L1==1 &Egg ==1 & Fec==1 & Tempmaxd[i] >18.6 & Tempmaxd[i]<=38.9){
      Fly1<-(-1.299+(Tempmaxd[i]*(.10900))+(-0.0019475*Tempmaxd[i]**2))
      Fly1<-1/(log(.50)/-Fly1)
      Flylog<-c(Flylog,Fly1)
      Flycount=Fly1+Flycount
      Templog<-c(Templog,Tempmaxd[i])
      if(Flycount>=1){Flycount<-1}
    }
    if(TA==1 &P==1 &L2==1 & L1==1 &Egg ==1 & Fec==1 & Flycount==1){
      landcount=landcount+1
    if(landcount>=8){
        Fec=0
        Egg=0
        L1<-0
        L2<-0
        P<-0
        TA<-0
        Gen<-Gen+1
        Flycount=0
        landcount=0
      }
    }
    
    row<-cbind(time,Fec,Egg,L1,L2,P,TA,Gen)  
    df<-rbind(row,df)
  }
  # return(df[order(df[,1],decreasing = F),])
  #}    
  
  df<-df[order(df[,1],decreasing = F),]
  Progression_Daily<-rowSums(df[,c(2:7)])
  return(list(df,Progression_Daily,Flylog,Templog))
}
drive<-"C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/WPB_Inputs/"

Maxs<-read.csv(paste0(drive,'MI_Tmax_6_20.csv'))
Mins<-read.csv(paste0(drive,'MI_Tmin_6_20.csv'))
HistoricMaxs<-read.csv(paste0(drive,'Tmax_Historic.csv'))
HistoricMins<-read.csv(paste0(drive,'Tmin_Historic.csv'))
Rate_LL<-Proccess_Rate(Mins$Low_LowElShape_Out,Maxs$Low_LowElShape_Out,Mins$Dates)
#plot(Rate_LL[[4]],Rate_LL[[3]])
Rate_LM<-Proccess_Rate(Mins$Low_MedElShape_Out,Maxs$Low_MedElShape_Out,Mins$Dates)
Rate_HL<-Proccess_Rate(Mins$High_LowElShape_Out,Maxs$High_LowElShape_Out,Mins$Dates)
Rate_HM<-Proccess_Rate(Mins$High_MedElShape_Out,Maxs$High_MedElShape_Out,Mins$Dates)
plot(as.Date(Mins$Dates[1:6296]),Rate_LL[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Southern Low Elevation",cex.main=4.0)
plot(as.Date(Mins$Dates[1:6296]),Rate_LM[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Southern High Elevation",cex.main=4.0)
plot(as.Date(Mins$Dates[1:6296]),Rate_HL[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Northern Low Elevation",cex.main=4.0)
plot(as.Date(Mins$Dates[1:6296]),Rate_HM[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Northern High Elevation",cex.main=4.0)

length(Rate_LM)




Rate_LL_Historic<-Proccess_Rate(HistoricMins$LowerLow,HistoricMaxs$LowerLow,HistoricMaxs$Dates)
Rate_LM_Historic<-Proccess_Rate(HistoricMins$LowerMed,HistoricMaxs$LowerMed,HistoricMaxs$Dates)
Rate_HL_Historic<-Proccess_Rate(HistoricMins$UpperLow,HistoricMaxs$UpperLow,HistoricMaxs$Dates)
Rate_HM_Historic<-Proccess_Rate(HistoricMins$UpperMed,HistoricMaxs$UpperMed,HistoricMaxs$Dates)


plot(as.Date(Mins$Dates[1:6296]),Rate_LL_Historic[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Southern Low Elevation",cex.main=4.0)
plot(as.Date(Mins$Dates[1:6296]),Rate_LM_Historic[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Southern High Elevation",cex.main=4.0)
plot(as.Date(Mins$Dates[1:6296]),Rate_HL_Historic[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Northern Low Elevation",cex.main=4.0)
plot(as.Date(Mins$Dates[1:6296]),Rate_HM_Historic[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=.5,main="Northern High Elevation",cex.main=4.0)


HistoricRate<-(Rate_LL_Historic[[2]]+Rate_LM_Historic[[2]]+Rate_HL_Historic[[2]]+Rate_HM_Historic[[2]])/4

plot(as.Date(Mins$Dates[1:6296]),Rate_LL[[2]],yaxt='n',xlab=NA,
     ylab=NA,type="l",col="red",cex.axis=2.0,lwd=5.,main="Northern High Elevation",cex.main=4.0)
lines(as.Date(Mins$Dates[1:6296]),Rate_LL_Historic[[2]],col="blue")

df<-Rate_LL[[1]]
Rates_Obs<-((Rate_LL[[1]][,8]+(Rate_LL[[2]]/8))+(Rate_LM[[1]][,8]+(Rate_LM[[2]]/8))+(Rate_HL[[1]][,8]+(Rate_HL[[2]]/8))+(Rate_HM[[1]][,8]+(Rate_HM[[2]]/8)))/4
Rates_Hist<-((Rate_LL_Historic[[1]][,8]+(Rate_LL_Historic[[2]]/8))+(Rate_LM_Historic[[1]][,8]+(Rate_LM_Historic[[2]]/8))+(Rate_HL_Historic[[1]][,8]+(Rate_HL_Historic[[2]]/8))+(Rate_HM_Historic[[1]][,8]+(Rate_HM_Historic[[2]]/8)))/4

par(pty="s")
plot(as.Date(Mins$Dates[1:6296]),Rates_Obs,main="Number of Generations 90th",type="l",
     ylab="Number of Generations",xlab="Dates",lwd=4.0,col="darkgreen",cex.axis=2.0,cex.lab=1.5)     
lines(as.Date(Mins$Dates[1:6296]),Rates_Hist,col="purple",lwd=4.0)
lines(as.Date(Mins$Dates[1:6296]),(2/365)*seq(1,6296),lty=1)
lines(as.Date(Mins$Dates[1:6296]),(3/365)*seq(1,6296),lty=2)
lines(as.Date(Mins$Dates[1:6296]),(4/365)*seq(1,6296),lty=3)
legend(as.Date(Mins$Dates[100]),40,legend=c("Observed","Historic","4 generations","3 generations","2 generations"),lwd=c(4,4,1,1,1),lty=c(1,1,3,2,1),
       col=c("darkgreen","purple","black","black","black"),cex=1.0)

CompareOut<-data.frame(Date=as.Date(Mins$Dates[1:6296]),Observed=Rates_Obs,Historic=Rates_Hist)

write.csv(CompareOut,"C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/Compare_Generations_Median.csv")


print(max(Rates_Hist))
print(max(Rates_Obs))

Rates_Obs_Dates<-data.frame(Date=as.Date(Mins$Dates[1:5296]),Rate=as.numeric(Rates_Obs))
Rates_Obs_Dates<-Rates_Obs_Dates[Rates_Obs_Dates$Date %in% seq(as.Date("2012-01-01"),
                                                                  as.Date("2016-12-30"),by='day'),]
Rates_Obs_Dates$Rate<-Rates_Obs_Dates$Rate-min(Rates_Obs_Dates$Rate)

Rates_Hist_Dates<-data.frame(Date=as.Date(Mins$Dates[1:5296]),Rate=as.numeric(Rates_Hist))

Rates_Hist_Dates<-Rates_Hist_Dates[Rates_Hist_Dates$Date %in% seq(as.Date("2012-01-01"),
                                                             as.Date("2016-12-30"),by='day'),]
Rates_Hist_Dates$Rate<-Rates_Hist_Dates$Rate-min(Rates_Hist_Dates$Rate)

max(Rates_Hist_Dates$Rate)
max(Rates_Obs_Dates$Rate)
