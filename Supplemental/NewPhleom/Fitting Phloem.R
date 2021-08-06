library(dplyr)
setwd("C:/Users/zacha/Desktop/NewPhleom/")

PonderosaData<-read.csv("ponderosapinephloem.csv")

PonderosaTrunc<-data.frame(Tree1=(PonderosaData$T1N+PonderosaData$T1S)/2,
                           Tree2=(PonderosaData$T2N+PonderosaData$T2S)/2,
                           Tree3=(PonderosaData$T3N+PonderosaData$T3S)/2,
                           Tree4=(PonderosaData$T4N+PonderosaData$T4S)/2,
                           AirTemp=PonderosaData$Air)
                           
#plot(PonderosaTrunc$AirTemp)
#points(PonderosaTrunc$Tree2,col="red")

PonderosaTrunc$meanT<-(PonderosaTrunc$Tree1+PonderosaTrunc$Tree2+PonderosaTrunc$Tree3+PonderosaTrunc$Tree4)/4
#plot(PonderosaTrunc$AirTemp,col="blue")
#points(PonderosaTrunc$meanT,col="red")
PonderosaTrunc$Day<-PonderosaData$JD
PonderosaTrunc$Year<-PonderosaData$Year
PonderosaTrunc$Hour<-PonderosaData$Time
###Missing Data
PonderosaTrunc<-PonderosaTrunc[c(-8073),]
PonderosaTrunc$Day[PonderosaTrunc$Year=="1995"]<-PonderosaTrunc$Day[PonderosaTrunc$Year=="1995"]+365


PonderosaTrunc$Date<-as.Date(PonderosaTrunc$Day-1,origin = "1994-01-01")

DayAir<-PonderosaTrunc %>%
  group_by(Date=Date) %>%
  summarise(Max=max(AirTemp),Min=min(AirTemp))

HourlyAir<-PonderosaTrunc %>%
  group_by(Date=Hour) %>%
  summarise(Max=max(AirTemp),Min=min(AirTemp),Mean=mean(AirTemp))

plot(HourlyAir$Max,col="red",ylim=c(-30,30))
points(HourlyAir$Min,col="blue")
points(HourlyAir$Mean)
abline(v=4)
abline(v=7,lty=2)
abline(v=10,lty=2)
abline(v=13,lty=2)
abline(v=16)
abline(v=19,lty=2)
abline(v=22,lty=2)

Tmax<-DayAir$Max
Tmin<-DayAir$Min
vector<-NULL
for(i in 1:length(Tmax)-1){
  Min<-Tmin[i]
  Max<-Tmax[i]
  Min2<-Tmin[i+1]
  Mean=(Max+Min)/2
  Mean2=(Max+Min2)/2
  Dif=(Max-Min)
  Dif2=(Max-Min2)
  Fouram<-Min
  Sevenam<-Mean+(.5*Dif*sin(-pi/4))
  Tenam<-Mean+(.5*Dif*sin(0))
  Onepm<-Mean+(.5*Dif*sin(pi/4))
  Fourpm<-Mean+(.5*Dif*sin(pi/2))
  Sevenpm<-Mean2+(.5*Dif2*sin(pi/4))
  Tenpm<-Mean2+(.5*Dif2*sin(0))
  OneAm<-Mean2+(.5*Dif2*sin(-pi/4))
  
  
  if(i==1){vector<-cbind(Fouram,Sevenam,Tenam,Onepm,Fourpm,Sevenpm,Tenpm,OneAm)}
  else{vector<-rbind(vector,cbind(Fouram,Sevenam,Tenam,Onepm,Fourpm,Sevenpm,Tenpm,OneAm))}
}
SimData<-as.data.frame(vector)


#### Four Am

FourAMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="400"]
lm1<-lm(FourAMphl~SimData$Fouram[1:386])
plot(FourAMphl,3.8532+(.9677*SimData$Fouram[1:386]),xlim=c(-15,25),ylim=c(-15,25))
abline(1,1)
summary(lm1)
text(-10, 10, "B0=3.8532, B1=.9677,R2=.9328", pos = 4)

###2
SevenAMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="700"]
lm2<-lm(SevenAMphl~SimData$Sevenam[1:386])
plot(SevenAMphl,1.86978+(.93522*SimData$Sevenam[1:386]),xlim=c(-15,25),ylim=c(-15,25))
abline(1,1)
summary(lm2)
text(-10, 10, "B0=1.86978, B1=.93522,R2=0.9459", pos = 4)


###3
TenAMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="1000"]
lm3<-lm(TenAMphl~SimData$Tenam[1:388])
summary(lm3)

plot(TenAMphl,-.45333+(1.00899*SimData$Tenam[1:388]),xlim=c(-15,25),ylim=c(-15,25))
abline(1,1)
text(-10, 10, "B0=-.45333, B1=1.00899,R2=.9269", pos = 4)



### One PM (4)

OnePMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="1300"]
lm4<-lm(OnePMphl~SimData$Onepm[1:387])
summary(lm4)

plot(OnePMphl,-1.148846 +(0.985801*SimData$Onepm[1:387]),xlim=c(-10,35),ylim=c(-10,35))
abline(1,1)
text(-10, 20, "B0=-1.148846, B1=0.985801,R2=.9665", pos = 4)


### Four Pm (5)
FourPMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="1600"]
lm5<-lm(FourPMphl~SimData$Fourpm[1:386])
summary(lm5)

plot(FourPMphl,0.065686 +(0.942395*SimData$Fourpm[1:386]),xlim=c(-10,35),ylim=c(-10,35))
abline(1,1)
text(-10, 20, "B0=-1.148846, B1=0.985801,R2=.9665", pos = 4)

### Seven Pm (6)
SevenPMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="1900"]
lm6<-lm(SevenPMphl~SimData$Sevenpm[1:386])
summary(lm6)


plot(SevenPMphl,-0.54496 +(0.96128*SimData$Sevenpm[1:386]),xlim=c(-10,35),ylim=c(-10,35))
abline(1,1)
text(-10, 20, "B0=-1.148846, B1=0.985801,R2=.9665", pos = 4)

#### Ten Pm
TenPMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="2200"]
lm7<-lm(TenPMphl~SimData$Tenpm[1:386])
summary(lm7)

plot(TenPMphl,0.934665 +(0.988126*SimData$Tenpm[1:386]),xlim=c(-10,35),ylim=c(-10,35))
abline(1,1)
text(-10, 20, "B0=0.934665 , B1=0.988126,R2=0.9645", pos = 4)

#### One Am (8)
par(pty="s")
OneAMphl<-PonderosaTrunc$meanT[PonderosaTrunc$Hour=="100"]
lm8<-lm(OneAMphl~SimData$OneAm[1:386])
summary(lm8)

plot(OneAMphl,3.18995 +(1.005804*SimData$OneAm[1:386]),xlim=c(-10,35),ylim=c(-10,35))
abline(1,1)
text(-10, 20, "B0=0.934665 , B1=0.988126,R2=0.9645", pos = 4)



####Comparing the whole thing 

Tmax<-DayAir$Max
Tmin<-DayAir$Min
Fittedvector<-NULL
for(i in 1:length(Tmax)-1){
  Min<-Tmin[i]
  Max<-Tmax[i]
  Min2<-Tmin[i+1]
  Mean=(Max+Min)/2
  Mean2=(Max+Min2)/2
  Dif=(Max-Min)
  Dif2=(Max-Min2)
  Fouram<-as.numeric(lm1$coefficients[1]+lm1$coefficients[2]*(Min))
  Sevenam<-as.numeric(lm2$coefficients[1]+lm2$coefficients[2]*(Mean+(.5*Dif*sin(-pi/4))))
  Tenam<-as.numeric(lm3$coefficients[1]+lm3$coefficients[2]*(Mean+(.5*Dif*sin(0))))
  Onepm<-as.numeric(lm4$coefficients[1]+lm4$coefficients[2]*(Mean+(.5*Dif*sin(pi/4))))
  Fourpm<-as.numeric(lm5$coefficients[1]+lm5$coefficients[2]*(Mean+(.5*Dif*sin(pi/2))))
  Sevenpm<-as.numeric(lm6$coefficients[1]+lm6$coefficients[2]*(Mean2+(.5*Dif2*sin(pi/4))))
  Tenpm<-as.numeric(lm7$coefficients[1]+lm7$coefficients[2]*(Mean2+(.5*Dif2*sin(0))))
  OneAm<-as.numeric(lm8$coefficients[1]+lm8$coefficients[2]*(Mean2+(.5*Dif2*sin(-pi/4))))
  
  
  if(i==1){Fittedvector<-c(Fouram,Sevenam,Tenam,Onepm,Fourpm,Sevenpm,Tenpm,OneAm)}
  else{Fittedvector<-c(Fittedvector,c(Fouram,Sevenam,Tenam,Onepm,Fourpm,Sevenpm,Tenpm,OneAm))}
}

plot(Fittedvector,ylim=c(0,30))
plot(PonderosaTrunc$meanT,ylim=c(0,30))
#Obs<-c(FourAMphl,SevenAMphl,TenAMphl,OnePMphl,FourPMphl,SevenPMphl,TenPMphl,OneAMphl)
for(i in 1:length(FourAMphl)){

if(i==1){Obs<-c(FourAMphl[i],SevenAMphl[i],TenAMphl[i],OnePMphl[i],
                FourPMphl[i],SevenPMphl[i],TenPMphl[i],OneAMphl[i])  }
else{Obs<-c(Obs,c(FourAMphl[i],SevenAMphl[i],TenAMphl[i],OnePMphl[i],
                             FourPMphl[i],SevenPMphl[i],TenPMphl[i],OneAMphl[i]))}
}


Fit<-Fittedvector[1:3088]
plot(Obs,Fit)
abline(1,1)
Test<-lm(Obs~Fit)
summary(Test)
library(grDevices)
plot(Obs,col=adjustcolor("red",alpha.f = .5))
points(Fit,col=adjustcolor("grey",alpha.f = .5))

RepeatedFit<-rep(Fit,each=3)
MeanPheolm<-PonderosaTrunc$meanT[1:9264]
plot(RepeatedFit,MeanPheolm)
abline(1,1)

Tree1<-PonderosaTrunc$Tree1[1:9264]
plot(RepeatedFit,Tree1)
abline(1,1)

Tree2<-PonderosaTrunc$Tree2[1:9264]
plot(RepeatedFit,Tree2)
abline(1,1)

Tree3<-PonderosaTrunc$Tree3[1:9264]
plot(RepeatedFit,Tree3)
abline(1,1)

Tree4<-PonderosaTrunc$Tree4[1:9264]
plot(RepeatedFit,Tree4)
abline(1,1)

dev.off()
plot(MeanPheolm)
points(RepeatedFit,col="red")
