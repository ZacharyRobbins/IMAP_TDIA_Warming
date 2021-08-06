


BTP=10000
ibeta=seq(0,1,.001)
Ps=1/(1+exp(-(500*(1-ibeta)))) 
plot(Ps,ibeta)
plot(Ps*BTP~ibeta,ylim=c(0,10000),xlim=c(.99,1.0))
points((1-Ps)*BTP~ibeta)


TC<-seq(0,50,.01)
Flying <- 1.42056 + (-0.2430939)*TC + (8.667045e-03)*(TC**2.0) + (5.472634e-04)*(TC**3.0) + 
  (-2.854299e-05)*(TC**4.0) + (3.200559e-07)*(TC**5.0)
plot(TC,Flying,)


temps<-seq(13,40,1)
#print(temps)
#length(temps)
vals=c(.0001,.0001,.0002,.0005,.007,.001,.038,.05,.02,.06,.02,
       .05,.05,.1,.05,.08,.1,.03,.1,.08,.03,.02,.04,.03,.02,.019,.0005,.0004)
sum(vals)
length(vals)
cumsum(vals)
vals_scaled<-vals
barplot(vals_scaled,names.arg = temps)

polynomial_fitter<-function(Temp,par,y_obs){
  y=par[1]+(par[2]*Temp)+(par[3]*Temp**2)+(par[4]*Temp**3)+(par[5]*Temp**4)+(par[6]*Temp**5)
  return(-sum(dnorm(y_obs,mean=y,sd=.001,log=TRUE)))  
}
fit<-optim(fn=polynomial_fitter,par=c(0,-.2439,1e-2,.5e-3, -2e-5,.3e-7),Temp=as.numeric(temps),y_obs=as.numeric(vals_scaled))

(x1<-fit$par[1])
(x2<-fit$par[2])
(x3<-fit$par[3])
(x4<-fit$par[4])
(x5<-fit$par[5])
(x6<-fit$par[6])

polynomial_plotters<-function(Temp,x1,x2,x3,x4,x5,x6){
  y=x1+(x2*Temp)+(x3*Temp**2)+(x4*Temp**3)+(x5*Temp**4)+(x6*Temp**5)
  return(y)
}
temps2<-seq(13,45,1)
Y<-polynomial_plotters(temps2,x1,x2,x3,x4,x5,x6)
#sum(Y)
plot(temps2,Y,xlab="Temperature (C)",ylab="Proportion to leave in flight",ylim=c(0,.12),xlim=c(10,45),
     main="Proportion of a population to take flight at a given Temp")
abline(v=17,col='red')
abline(v=38.9,col='red')


#max(Y)
TC=seq(17,42)
Flying <-2.500e+01 + (-5.324e+00)*TC + (4.277e-01)*(TC**2.0) + (-1.633e-02)*(TC**3.0) + 
  (3.014e-04)*(TC**4.0) + (-2.172e-06)*(TC**5.0)

plot(Flying~TC,ylim=c(0,1.0))
abline(v=17,col='red')
abline(v=42,col='red')
1/.06



