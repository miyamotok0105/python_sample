import pymc
import mymodel1

S = pymc.MCMC(mymodel1, db='pickle')
S.sample(iter=10000, burn=5000, thin=2)
pymc.Matplot.plot(S)
