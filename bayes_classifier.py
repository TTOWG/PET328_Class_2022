
no_of_dolo_cores= input('Enter no of dolomite cores:')
no_of_shale_cores=input('Enter no of shale cores:')
no_of_all_cores=input('Enter no of all cores:')

no_of_dolo_cores=float(no_of_dolo_cores)
no_of_shale_cores=float(no_of_shale_cores)
no_of_all_cores=float(no_of_all_cores)

P_D= no_of_dolo_cores/no_of_all_cores
P_S= no_of_shale_cores/no_of_all_cores


import scipy.stats

loc_D= input('Enter the dolomite mean:')
scale_D= input('Enter the standard deviation of dolomite:')
loc_S= input('Enter the shale mean:')
scale_S=input ('Enter the standard deviation of shale:')

loc_D= float(loc_D)
scale_D=float(scale_D)
loc_S=float(loc_S)
scale_S=float(scale_S)

P_gamma_greater_than_60_D= 1-scipy.stats.norm(loc_D, scale_D).cdf(60)
P_gamma_greater_than_60_S= 1-scipy.stats.norm(loc_S, scale_S).cdf(60)


P_D_gamma_greater_than_60=(P_D*P_gamma_greater_than_60_D)/((P_D*P_gamma_greater_than_60_D)\
                             + (P_S* P_gamma_greater_than_60_S))
if P_D_gamma_greater_than_60_D >= 0.5:
    print('P(D|gamma > 60)= ',P_D_gamma_greater_than_60)
   
else:
    print('P(D|gamma > 60)= ',P_D_gamma_greater_than_60)

    
