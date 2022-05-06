nsc = float(input('What is the number of shale cores?'))
ndc = float(input('What is the number of dolomite cores?'))
nac = float(input('What is the number of total cores?'))

pd = ndc/nac
ps = nsc/nac

import scipy.stats

locD = float(input('Enter the mean value of Dolomite'))
locS = float(input('Enter the mean value of Shale'))
scaleD = float(input('Enter the standard deviation value of Dolomite'))
scaleS = float(input('Enter the standard deviation value of Shale'))

pgamma_greaterthan60D = 1- scipy.stats.norm(loc = locD, scale = scaleD).cdf(60)
pgamma_greaterthan60S = 1- scipy.stats.norm(loc = locS, scale = scaleD).cdf(60)

pDgamma_greaterthan60 = (pd*pgamma_greaterthan60D)/((pd*pgamma_greaterthan60D)+(ps*pgamma_greaterthan60S))

if pDgamma_greaterthan60 >= 0.5:
    print('The value gotten is {0:.3f}' .format(pDgamma_greaterthan60))
    print('The interval is Dolomite')
else:
    print('The value gotten is {0:.3f}' .format(pDgamma_greaterthan60))
    print('It is a Shale interval')
