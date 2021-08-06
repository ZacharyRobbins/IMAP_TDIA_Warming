#library(rstanarm)
library(deBInfer)

Eggs<-data.frame(Temp=c(53,55,60,70,90),
                 Days=c(114,57,40,7,7))
Eggs$Temp<-F2C(Eggs$Temp)

DataE<-Eggs
TmE=38.889
#Rate*((((T-Tb)**2)/((T-Tb)**2+k))-exp(-(Tm-(T-Tb))/dm))
#<-par=c(.18,10,1000,.5)
TmE<- debinfer_par(name = "TmE", var.type = "de", fixed = FALSE,
               value = 38.889, prior = "norm", hypers = list(mean = 0, sd = .5),
               prop.var = 0.001, samp.type="rw")
Tmb<- debinfer_par(name = "Tmb", var.type = "de", fixed = FALSE,
                   value = 10, prior = "norm", hypers = list(mean = 0, sd = .5),
                   prop.var = 0.01, samp.type="rw")
Rate<- debinfer_par(name = "Rate", var.type = "de", fixed = FALSE,
                   value = .18, prior = "norm", hypers = list(mean = 0, sd = 10),
                   prop.var = 0.0001, samp.type="rw")
k<- debinfer_par(name = "k", var.type = "de", fixed = FALSE,
                   value = 1000, prior = "norm", hypers = list(mean = 0, sd = .5),
                   prop.var = 0.0001, samp.type="rw")
dm<- debinfer_par(name = "dm", var.type = "de", fixed = FALSE,
                 value = .5, prior = "norm", hypers = list(mean = 0, sd = .5),
                 prop.var = 0.0001, samp.type="rw")


logistic_obs_model <- function(data, sim.data, samp){
  llik.N <- sum(dnorm(data$Days,mean=sim.data[,"N"],sd=2 ))
  return(llik.N)
}

LoganFunction=function (Temp,y,parms){
  with(as.list(c(y, parms)), {
  #Rt= par[1]*exp(-.5*(((Temp-par[2])/par[3])^2))
  #Rt=par[1]*((((Temp-par[2])**2)/(((Temp-par[2])**2)+par[3]))-exp(-(TmE-(Temp-par[2]))/par[4]))
  dN<-Rate+(((Temp-Tmb)**2)/(((Temp-Tmb)**2)+k)-exp(-(TmE-(Temp-Tmb))/dm))
  #-sum(dnorm(k,mean=Rt,sd=1,log=TRUE))
  list(dN)
  })
}
N <- debinfer_par(name = "N", var.type = "init", fixed = TRUE, value = 0)
mcmc.pars <- setup_debinfer(TmE,Tmb,Rate,k,dm, N)

iter <- 5000
# inference call
MCMC<-mcmc_samples <- de_mcmc(N = iter, data = Eggs, de.model = LoganFunction,
                        obs.model = logistic_obs_model, all.params = mcmc.pars,
                        Tmax = max(Eggs$Temp), data.times = c(0,Eggs$Temp), cnt = 500)

