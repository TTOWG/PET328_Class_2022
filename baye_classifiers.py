loc_Dm = float(input('Enter the value of the mean of dolomite:'))
loc_Sh = float(input('Enter the value of the mean of shale:'))
scale_Dm = float(input('Enter the value of the standard deviation of dolomite:'))
scale_Sh = float(input('Enter the value of the standard deviation of shale:'))
count_Dm = float(input('Enter the value of the count of dolomite:'))
count_Sh = float(input('Enter the value of the count of shale:'))
import scipy.stats
Num_of_all_cores = count_Dm + count_Sh
P_Dm = count_Dm/Num_of_all_cores
P_Sh = count_Sh/Num_of_all_cores
P_Dm_gamma_greater_than60 = 1-scipy.stats.norm(loc_Dm,scale_Dm).cdf(0.5)
P_Sh_gamma_greater_than60 = 1-scipy.stats.norm(loc_Sh,scale_Sh).cdf(0.5)
P_D_gamma_greater_than_60 = (P_Dm * P_Dm_gamma_greater_than60)/((P_Dm * P_Dm_gamma_greater_than60)+(P_Sh * P_Sh_gamma_greater_than60))
if P_D_gamma_greater_than_60>=0.5:
    print('DOLOMITE')
else:
    print('SHALE')
