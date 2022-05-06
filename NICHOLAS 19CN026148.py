dolomite_loc = float  (input ('Enter the mean of dolomite:' ))
dolomite_scale= float (input ('Enter the stadard deviation of dolomite:'))
shale_loc = float (input ('Enter the mean of shale:'))
shale_scale = float (input ('Enter the standard deviation of shale:'))
dolomite_count = float (input ('Enter the count for dolomite:'))
shale_count = float (input ('Enter the count for shale:'))
import scipy.stats
#no_cores == Number of all cores
num_cores = dolomite_count + shale_count
p_dolomite = dolomite_count / num_cores
p_shale = shale_count / num_cores
p_gamma_60_dolomite = 1- scipy.stats.norm(dolomite_loc, dolomite_scale ).cdf(0.5)
p_gamma_60_shale = 1- scipy.stats.norm(shale_loc , shale_scale ).cdf(0.5)
p_dolomite_gamma_60 = (p_dolomite * p_gamma_60_dolomite) / (p_dolomite * p_gamma_60_dolomite + p_shale * p_gamma_60_shale)
if p_dolomite_gamma_60 >= 0.5:
    print ('DOLOMITE')
else:
    print ('SHALE INTERVAL')


