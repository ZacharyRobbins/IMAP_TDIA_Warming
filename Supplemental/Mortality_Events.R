
drive<-"C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/WPB_Inputs/"

Maxs<-read.csv(paste0(drive,'MI_Tmax_6_20.csv'))
Mins<-read.csv(paste0(drive,'MI_Tmin_6_20.csv'))
HistoricMaxs<-read.csv(paste0(drive,'Tmax_Historic.csv'))
HistoricMins<-read.csv(paste0(drive,'Tmin_Historic.csv'))

ProcessTemp<-function(Maxin,Minin,Dates){
  LP_Out<-NULL
  P_Out<-NULL
  A_Out<-NULL
  E_Out<-NULL
  Date_Out<-NULL
  MinVector<-NULL
  reset=288
  ColdestDay<-100
  for(i in 1:(length(Maxin)-1)){
    
    TmaxTime<-Maxin[i]
    Tmintime<-Minin[i]
    TminNext<-Minin[i-1]
    DateToday<-Dates[i]
    CMean=(TmaxTime+Tmintime)/2
    CMean2=(TmaxTime+TminNext)/2
    CDif=(TmaxTime-Tmintime)
    CDif2=(TmaxTime-TminNext)
    reset<-reset+1
    
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
    Fector<-c(fouram,sevenam,tenam,onepm,fourpm,sevenpm,tenpm,oneam)
    Tmin<-fouram
    if(reset== 91){ColdestDay=100}
    if(reset >=365){
      reset=1

    }
    if(Tmintime < ColdestDay){ColdestDay<-Tmintime}
    Larval_Percent<-1.0/(1.0 + exp(-(ColdestDay + 28.391)/6.124))
    Larval_Percent<-1-Larval_Percent
    if(Tmin< -20.6){PupalMort<-1}else{PupalMort<-0}
    if(Tmin< -12.2){AdultMort<-1}else{AdultMort<-0}
    if(Tmin< -20.6){EggMort<-1}else{EggMort<-0}
    LP_Out<-c(Larval_Percent,LP_Out)
    P_Out<-c(PupalMort,P_Out)
    A_Out<-c(AdultMort,A_Out)
    E_Out<-c(EggMort,E_Out)
    Date_Out<-c(DateToday,Date_Out)
    MinVector<-c(Tmin,MinVector)
  }  #return(list(LP_Out,P_Out,A_Out,E_Out))
  Dataframe<-data.frame(Dates=Date_Out,Tmin=MinVector,LarvalMort=LP_Out,Pupae=P_Out,Adults=A_Out,Eggs=E_Out)  
  return(Dataframe)
}  


LL<-ProcessTemp(Maxs$Low_LowElShape_Out,Mins$Low_LowElShape_Out,Mins$Dates)
LM<-ProcessTemp(Maxs$Low_MedElShape_Out,Mins$Low_MedElShape_Out,Mins$Dates)
HL<-ProcessTemp(Maxs$High_LowElShape_Out,Mins$High_LowElShape_Out,Mins$Dates)
HM<-ProcessTemp(Maxs$High_MedElShape_Out,Mins$High_MedElShape_Out,Mins$Dates)

#fouram=3.8532+(HistoricMins$LowerMed*.9677)
#plot(fouram)
#abline(h=-12.2)
LL_Historic<-ProcessTemp(HistoricMaxs$LowerLow,HistoricMins$LowerLow,HistoricMaxs$Dates)
LM_Historic<-ProcessTemp(HistoricMaxs$LowerMed,HistoricMins$LowerMed,HistoricMaxs$Dates)
HL_Historic<-ProcessTemp(HistoricMaxs$UpperLow,HistoricMins$UpperLow,HistoricMaxs$Dates)
HM_Historic<-ProcessTemp(HistoricMaxs$UpperMed,HistoricMins$UpperMed,HistoricMaxs$Dates)





library(dplyr)
library(lubridate)
Aggregating<-function(One){
  Agged<-One %>%
  mutate(year=year(as.Date(Dates,tryFormats="%Y-%m-%d"))) %>%
  dplyr::group_by(year)%>%
  dplyr::summarise(LarvalMort=mean(LarvalMort),Pupae=sum(Pupae),Adults=sum(Adults),Eggs=sum(Eggs))
  #summarise
return(Agged)}

LL_Agg<-Aggregating(LL)
LM_Agg<-Aggregating(LM)
HL_Agg<-Aggregating(HL)
HM_Agg<-Aggregating(HM)


LL_Historic_Agg<-Aggregating(LL_Historic)
LM_Historic_Agg<-Aggregating(LM_Historic)
HL_Historic_Agg<-Aggregating(HL_Historic)
HM_Historic_Agg<-Aggregating(HM_Historic)

library(ggplot2)

Obs_Events<-data.frame(Year=LL_Agg$year,Simulation="Observed",
           Average_Larval_Percent=(LL_Agg$LarvalMort+LM_Agg$LarvalMort+HL_Agg$LarvalMort+HM_Agg$LarvalMort)/4,
           Average_Pupae=(LL_Agg$Pupae+LM_Agg$Pupae+HL_Agg$Pupae+HM_Agg$Pupae),
           Average_Adults=(LL_Agg$Adults+LM_Agg$Adults+HL_Agg$Adults+HM_Agg$Adults),
           Average_Eggs=(LL_Agg$Eggs+LM_Agg$Eggs+HL_Agg$Eggs+HM_Agg$Eggs))
           
His_Events<-data.frame(Year=LL_Historic_Agg$year,Simulation="Historic",
                       Average_Larval_Percent=(LL_Historic_Agg$LarvalMort+LM_Historic_Agg$LarvalMort+HL_Historic_Agg$LarvalMort+HM_Historic_Agg$LarvalMort)/4,
                       Average_Pupae=(LL_Historic_Agg$Pupae+LM_Historic_Agg$Pupae+HL_Historic_Agg$Pupae+HM_Historic_Agg$Pupae),
                       Average_Adults=(LL_Historic_Agg$Adults+LM_Historic_Agg$Adults+HL_Historic_Agg$Adults+HM_Historic_Agg$Adults),
                       Average_Eggs=(LL_Historic_Agg$Eggs+LM_Historic_Agg$Eggs+HL_Historic_Agg$Eggs+HM_Historic_Agg$Eggs))

AllData<-rbind(Obs_Events,His_Events)

write.csv(AllData,"C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/Figures_NCC/Mortality_Events_new.csv")



ggplot(AllData,aes(factor(Year),Average_Adults,fill=Simulation))+
  geom_bar(stat="identity",position="dodge")+
  scale_fill_manual("legend", values = c("Historic" = "darkgreen", "Observed" = "purple")) + 
  theme_light()+
  theme( axis.text.x = element_text(size=10, angle=35),
         axis.text.y = element_text(size=10))+
  xlab("Year")+
  ylab("Max Adult Mortality Events")+
  ggtitle("Max Mortality Events by Year")

par()
dev.off()


Plotty<-data.frame(Year=c(His_Events$Year,His_Events$Year),
                   Model=c(rep("Historic",length(His_Events$Year)),rep("Contemporary",length(His_Events$Year))),
                   Value=c(His_Events$Average_Larval_Percent,Obs_Events$Average_Larval_Percent))
Plotty
ggplot(Plotty,aes(factor(Year),Value,fill=Model))+
  geom_bar(stat="identity",position="dodge")+
  scale_fill_manual("legend", values = c("Historic" = "darkgreen", "Contemporary" = "purple")) + 
  theme_light()+
  theme( axis.text.x = element_text(size=10, angle=35),
          axis.text.y = element_text(size=10))+
   xlab("Year")+
   ylab("Max Larval Mortality Percentage")+
   ggtitle("Max Larval Mortality Percentage by Year")


plot(His_Events$Year, His_Events$Average_Larval_Percent,main="Maximum Larval Rate of Mortality",ylab="Maximum Larval Mortality Rate",
     xlab=("Year"))
points(His_Events$Year,Obs_Events$Average_Larval_Percent,col="red")
legend(His_Events$Year[12],.0013,legend=c("Historic","Observed"),pch=c(1,1),col=c("black","red"))

Output<-data.frame(Year=His_Events$Year,Historical=His_Events$Average_Larval_Percent,Observed=Obs_Events$Average_Larval_Percent, Differnce=(Obs_Events$Average_Larval_Percent-His_Events$Average_Larval_Percent)/(Obs_Events$Average_Larval_Percent))
mean(Output$Differnce)
sum(Output$Historical-Output$Observed)
