ndc = float(input('Enter the number of dolomite cores'))
nsc = float(input('Enter the number of shale cores'))
nac = ndc + nsc

P_D = ndc/nac
P_S = nsc/nac

import scipy.stats

loc_D = float(input('Enter the mean value for dolomite'))
scale_D = float(input('Enter the standard deviation value for dolomite'))
loc_S = float(input('Enter the mean value for shale'))
scale_S = float(input('Enter the standard deviation value for shale'))



P_gamma_greaterthan_60_D = 1-scipy.stats.norm(loc_D,scale_D).cdf(60)
P_gamma_greaterthan_60_S = 1-scipy.stats.norm(loc_S,scale_S).cdf(60)

P_Dgamma_greaterthan60 = P_D*P_gamma_greaterthan_60_D/((P_D*P_gamma_greaterthan_60_D)+ (P_S*P_gamma_greaterthan_60_S))


if P_Dgamma_greaterthan60>=0.5:
    print('P_Dgamma_greaterthan60 value is', P_Dgamma_greaterthan60)
    print('The interval is dolomite!')
else:
    print('P_Dgamma_greaterthan60 value is', P_Dgamma_greaterthan60)
    print('The interval is shale!')


