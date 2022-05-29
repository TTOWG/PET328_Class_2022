loc_Dmt = float(input('Enter the value of the mean of dolomite:'))
loc_Shl = float(input('Enter the value of the mean of shale:'))
scale_Dmt = float(input('Enter the value of the standard deviation of dolomite:'))
scale_Shl = float(input('Enter the value of the standard deviation of shale:'))
count_Dmt = float(input('Enter the value of the count of dolomite:'))
count_Shl = float(input('Enter the value of the count of shale:'))
import scipy.stats
No_of_all_cores = count_Dmt + count_Shl
P_Dmt = count_Dmt/No_of_all_cores
P_Shl = count_Shl/No_of_all_cores
P_Dmt_gamma_greater_than60 = 1-scipy.stats.norm(loc_Dmt,scale_Dmt).cdf(0.5)
P_Shl_gamma_greater_than60 = 1-scipy.stats.norm(loc_Shl,scale_Shl).cdf(0.5)
P_D_gamma_greater_than_60 = (P_Dmt * P_Dmt_gamma_greater_than60)/((P_Dmt * P_Dmt_gamma_greater_than60)+(P_Shl * P_Shl_gamma_greater_than60))
if P_D_gamma_greater_than_60>=0.5:
    print('DOLOMITE')
else:
    print('SHALE')
