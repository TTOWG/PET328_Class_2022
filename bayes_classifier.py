loc_dm = float  (input ('What is the mean of dolomite:' ))
scale_dm = float (input ('What is the stadard deviation of dolomite:'))
loc_sh = float (input ('What is the mean of shale:'))
scale_sh = float (input ('What is the standard deviation of shale:'))
count_dm = float (input ('What is the count for dolomite:'))
count_sh = float (input ('What is the count for shale:'))
import scipy.stats
#no_cores == Number of all cores
no_cores = count_dm + count_sh
p_dm = count_dm / no_cores
p_sh = count_sh / no_cores
p_gamma_60_dm = 1- scipy.stats.norm(loc_dm , scale_dm ).cdf(0.5)
p_gamma_60_sh = 1- scipy.stats.norm(loc_sh , scale_sh ).cdf(0.5)
p_dm_gamma_60 = (p_dm * p_gamma_60_dm) / (p_dm * p_gamma_60_dm + p_sh * p_gamma_60_sh)
if p_dm_gamma_60 >= 0.5:
    print ('DOLOMITE')
else:
    print ('SHALE INTERVAL')


