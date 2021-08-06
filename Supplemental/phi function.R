




Phi<-exp(10.03+(1.545*SPI)+.505)
plot(SPI,Phi)


SPI<-seq(-3,1,.1)
Phi<-exp(10.03+(1.545*SPI)+.505)
Phi2<-exp(10.03+(1.545*SPI))


SPI<-seq(-3,1.0,.1)
Phi<-exp(10.03+(1.545*SPI)+.505)
Phi2<-exp(10.03+(1.545*SPI))
dev.off()
par(mfrow=c(1,2))
plot(SPI,Phi,ylim=c(0,30000),col="blue",pch=19)
points(SPI,Phi2,ylim=c(0,30000),col="red",pch=19)
plot(SPI,Phi,col="blue",pch=19)
points(SPI,Phi2,,col="red",pch=19)

#min(Phi)
#min(Phi2)

SPI_4<-read.csv("C:/Users/zacha/Documents/GitHub/IMAP_Python_Project/WPB_Model/WPB_Inputs/WPB_SPI_620.csv")
MeanLS<-rowMeans(SPI_4[,c(3:6)])


par(mfrow=c(2,1))
plot(as.Date(SPI_4$Dates),exp(10.03+(1.545*MeanLS)+.505),type="l",col="purple",
     ylab="phi",xlab="Date")
lines(as.Date(SPI_4$Dates),exp(10.03+(1.545*MeanLS)),lty=1,col="orange")


plot(as.Date(SPI_4$Dates),exp(10.03+(1.545*MeanLS)+.505),
     type="l",col="purple",ylim=c(0,15000),ylab="phi",xlab="Date")
lines(as.Date(SPI_4$Dates),exp(10.03+(1.545*MeanLS)),lty=1,col="orange")


