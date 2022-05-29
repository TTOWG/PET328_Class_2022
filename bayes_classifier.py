loc_dolo=float(input("Enter the mean of Dolomite:"))
loc_shale=float(input("Enter the mean of Shale:"))
scale_dolo=float(input("Enter the standard deviation of Dolomite:"))
scale_shale=float(input("Enter the standard deviation of Shale:"))
count_dolo=float(input("Enter the count for Dolomite:"))
count_shale=float(input("Enter the count for Shale:"))

import scipy.stats

no_cores=count_dolo+count_shale
p_dolo=count_dolo/no_cores
p_shale=count_shale/no_cores
p_gamma_60_dolo=1-scipy.stats.norm(loc_dolo,scale_dolo).cdf(0.5)
p_gamma_60_shale=1-scipy.stats.norm(loc_shale,scale_shale).cdf(0.5)
p_dolo_gamma_60=(p_dolo*p_gamma_60_dolo)/(p_dolo*p_gamma_60_dolo+p_shale*p_gamma_60_shale)
if p_dolo_gamma_60>=0.5:
    print("DOLOMITE")
else:
    print("SHALE INTERVAL")
