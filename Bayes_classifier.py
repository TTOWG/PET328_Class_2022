loc_d = float (input('Enter your loc for dolomite:' ))
scale_d = float (input('Enter your scale for dolomite:' ))
loc_s = float (input ('Enter your loc for shale:' ))
scale_s = float (input ('Enter your scale for shale:'))
count_d = float (input('Enter count for dolomite:'))
count_s = float (input('Enter count for shale:'))
#no_c =  Number of all cores
no_c = count_d + count_s
p_D = count_d / no_c
p_S = count_s / no_c
#Let p_gamma_D = p_gamma>60|D
#Let p_gamma_S = p_gamma>60|S
#Let p_D_gamma_60 = p_D|gamma>60
import scipy.stats
p_gamma_D =1 - scipy.stats.norm(loc_d, scale_d).cdf(0.5)
p_gamma_S =1 - scipy.stats.norm(loc_s, scale_s).cdf(0.5)
p_D_gamma_60 =(p_D * p_gamma_D) /(p_D * p_gamma_D + p_S * p_gamma_S)
print ('p_D|gamma>60=',p_D_gamma_60)
if p_D_gamma_60>= 0.5:
    print ('Therefore it is DOLOMITE INTERVAL')
else:
    print ('It is SHALE INTERVAL')
