loc_dolomite = float  (input ('What is the mean of dolomite:' ))
scale_dolomite= float (input ('What is the stadard deviation of dolomite:'))
loc_shale = float (input ('What is the mean of shale:'))
scale_shale = float (input ('What is the standard deviation of shale:'))
count_dolomite = float (input ('What is the count for dolomite:'))
count_shale = float (input ('What is the count for shale:'))
import scipy.stats
#no_cores == Number of all cores
no_cores = count_dolomite + count_shale
p_dolomite = count_dolomite / no_cores
p_shale = count_shale / no_cores
p_gamma_60_dolomite = 1- scipy.stats.norm(loc_dolomite , scale_dolomite ).cdf(0.5)
p_gamma_60_shale = 1- scipy.stats.norm(loc_shale , scale_shale ).cdf(0.5)
p_dolomite_gamma_60 = (p_dolomite * p_gamma_60_dolomite) / (p_dolomite * p_gamma_60_dolomite + p_shale * p_gamma_60_shale)
if p_dolomite_gamma_60 >= 0.5:
    print ('DOLOMITE')
else:
    print ('SHALE INTERVAL')


