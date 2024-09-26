loc_dolo = float (input('Enter your loc for dolomite:' ))
scale_dolo = float (input('Enter your scale for dolomite:' ))
loc_sha = float (input ('Enter your loc for shale:' ))
scale_sha = float (input ('Enter your scale for shale:' ))
count_dolo = float (input('Enter count for dolomite:'))
count_sha = float (input('Enter count for shale:'))
import scipy.stats

no_c = count_d + count_s
p_D = count_d / no_c
p_S = count_s / no_c

p_gamma_D =1 - scipy.stats.norm(loc_dolo, scale_dolo).cdf(0.5)
p_gamma_S =1 - scipy.stats.norm(loc_sha, scale_sha).cdf(0.5)
p_D_gamma_60 =(p_D * p_gamma_D) /(p_D * p_gamma_D + p_S * p_gamma_S)

if p_D_gamma_60>= 0.5:
    print ('DOLOMITE INTERVAL')
else:
    print ('It is SHALE INTERVAL')
