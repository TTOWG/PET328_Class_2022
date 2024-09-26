number_of_dol_cores=input('Enter no of dolomite cores:')
number_of_shale_cores=input('Enter no of shale cores:')
number_of_all_cores=input('Enter no of total cores:')

number_of_dol_cores=float(number_of_dol_cores)
number_of_shale_cores=float(number_of_shale_cores)
number_of_all_cores=float(number_of_all_cores)

P_D= number_of_dol_cores/number_of_all_cores
P_S= number_of_shale_cores/number_of_all_cores

import scipy.stats

loc_D=input('Enter the mean of dolomite:')
scale_D=input('Enter the standard deviation of dolomite:')
loc_S=input('Enter the mean of shale:')
scale_S=input('Enter the standard deviation of shale:')

loc_D=float(loc_D)
scale_D=float(scale_D)
loc_S=float(loc_S)
scale_S=float(scale_S)


P_gamma_greater_than_60_D=  1 - scipy.stats.norm(loc_D, scale_D).cdf(60)
P_gamma_greater_than_60_S=  1 - scipy.stats.norm(loc_S, scale_S).cdf(60)

P_D_gamma_greater_than_60= (P_D*P_gamma_greater_than_60_D)/(P_D*P_gamma_greater_than_60_D) + (P_S*P_gamma_greater_than_60_S)

if P_D_gamma_greater_than_60 >= 0.5:
                           print('𝑃(𝐷|𝑔𝑎𝑚𝑚𝑎 > 60)=',P_D_gamma_greater_than_60)
                           print(P_D_gamma_greater_than_60,'is greater or equals to 0.5 therefore the interval is Dolomite!')

else:
                           print('𝑃(𝐷|𝑔𝑎𝑚𝑚𝑎 > 60)=',P_D_gamma_greater_than_60)
                           print(P_D_gamma_greater_than_60,'is less than and 0.5 therefore the interval is Shale!')
                           





