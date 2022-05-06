N_D= float(input('Enter the number of dolomite cores'))
N_S= float(input('Enter the number of shale cores'))
N_T= float(input('Enter the number of total cores'))

P_D = N_D/N_T
P_S = N_S/N_T

import scipy.stats

loc_D = float(input('Enter the mean for dolomite'))
scale_D = float(input('Enter the standard deviation for dolomite'))
loc_S = float(input('Enter the mean for shale'))
scale_S = float(input('Enter the standard deviation for shale'))


P_gamma_greaterthan_60D = 1-scipy.stats.norm(loc_D, scale_D).cdf(60)
P_gamma_greaterthan_60S = 1-scipy.stats.norm(loc_S, scale_S).cdf(60)

P_gamma_greaterthan_60 = P_D*P_gamma_greaterthan_60D/((P_D*P_gamma_greaterthan_60D)+(P_S*P_gamma_greaterthan_60S))


if P_gamma_greaterthan_60>0.5 or P_gamma_greaterthan_60==0.5:
    print('P_gamma_greaterthan_60 value is ', P_gamma_greaterthan_60)
    print('The formation is more of dolomite!')
else:
    print('P_gamma_greaterthan_60 value is ', P_gamma>60)
    print('Th formation is more of shale')
    
