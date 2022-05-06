number_of_dolomite_cores = float(input('Enter the number of dolomite cores\n'))
numner_of_shale_cores = float(input('Enter the number of shale cores\n'))
number_of_all_cores = number_of_dolomite_cores + numner_of_shale_cores

P_D = number_of_dolomite_cores/number_of_all_cores
P_S = numner_of_shale_cores/number_of_all_cores

import scipy.stats

loc_D = float(input('Enter the mean value for dolomite\n'))
scale_D = float(input('Enter the standard deviation value for dolomite\n'))
loc_S = float(input('Enter the mean value for shale\n'))
scale_S = float(input('Enter the standard deviation value for shale\n'))



P_gamma_greaterthan_60D = 1-scipy.stats.norm(loc_D,scale_D).cdf(60)
P_gamma_greaterthan_60S = 1-scipy.stats.norm(loc_S,scale_S).cdf(60)

P_Dgamma_greaterthan60 = P_D*P_gamma_greaterthan_60D/((P_D*P_gamma_greaterthan_60D)+ (P_S*P_gamma_greaterthan_60S))


if P_Dgamma_greaterthan60>0.5:
    print('The interval is dolomite!')
else:
    print('The interval is shale!')
