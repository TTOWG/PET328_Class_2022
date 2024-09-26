number_of_dolomite_cores = float(input('Enter the number of dolomite cores\n'))
number_of_shale_cores = float(input('Enter the number of shale cores\n'))
loc_D = float(input('Enter the mean value for dolomite\n'))
scale_D = float(input('Enter the standard deviation value for dolomite\n'))
loc_S = float(input('Enter the mean value for shale\n'))
scale_S = float(input('Enter the standard deviation value for shale\n'))


number_of_all_cores = number_of_dolomite_cores + number_of_shale_cores
P_D = number_of_dolomite_cores/number_of_all_cores
P_S = number_of_shale_cores/number_of_all_cores

print('P_D =',P_D)
print('P_S =',P_S)


import scipy.stats


p_gamma_greaterthan_60_D= 1-scipy.stats.norm(loc_D,scale_D).cdf(60)
p_gamma_greaterthan_60_S= 1-scipy.stats.norm(loc_S,scale_S).cdf(60)

P_Dgamma_greaterthan60 = ((P_D*p_gamma_greaterthan_60_D)/((P_D*p_gamma_greaterthan_60_D)+ (P_S*p_gamma_greaterthan_60_S)))


if P_Dgamma_greaterthan60 >= 0.5:
    print('P_Dgamma_greaterthan60 value is ',P_Dgamma_greaterthan60)
    print('The interval is dolomite!')
else:
    print('P_Dgamma_greaterthan60 value is ',P_Dgamma_greaterthan60)
    print('The interval is shale!')

