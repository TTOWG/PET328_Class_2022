loc_dol=float(input('Enter the mean of dolomite:'))
scale_dol=float(input('Enter the standard deviation of dolomite:'))
loc_sh=float(input('Enter the mean of shale:'))
scale_sh=float(input('Enter the standard deviation of shale:'))
count_dol=float(input('Enter the count for dolomite:'))
count_sh=float(input('Enter the count for shale:'))
import scipy.stats
#no_cores==Number of all cores
no_cores=count_dol+count_sh
p_dol=count_dol/no_cores
p_sh=count_sh/no_cores
p_gamma_60_dol=1-scipy.stats.norm(loc_dol,scale_dol).cdf(0.5)
p_gamma_60_sh=1-scipy.stats.norm(loc_sh,scale_sh).cdf(0.5)
p_dol_gamma_60=(p_dol*p_gamma_60_dol)/(p_dol*p_gamma_60_dol+p_sh*p_gamma_60_sh)
if p_dol_gamma_60>=0.5:
    print('DOLOMITE')
else:
    print('SHALE INTERVAL')
