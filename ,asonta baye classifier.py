loc_Dolomite = float(input('Enter the value of the mean of dolomite:'))
loc_Shale = float(input('Enter the value of the mean of shale:'))
scale_Dolomite = float(input('Enter the value of the standard deviation of the dolomite:'))
scale_Shale = float(input('Enter the value of the standard deviation of the shale:'))
count_Dolomite = float(input('Enter the value of the count of the dolomite:'))
count_Shale = float(input('Enter the value of the count of the shale:'))
import scipy.stats
Num_of_all_cores = count_Dolomite + count_Shale
Prob_Dolomite = count_Dolomite/Num_of_all_cores
Prob_Shale = count_Shale/Num_of_all_cores
Prob_gamma_greater_than60_Dolomite = 1-scipy.stats.norm(loc_Dolomite,scale_Dolomite).cdf(0.5)
Prob_gamma_greater_than60_Shale = 1-scipy.stats.norm(loc_Shale,scale_Shale).cdf(0.5)
Prob_Dolomite_gamma_greater_than_60 = (Prob_Dolomite * Prob_gamma_greater_than60_Dolomite)/((Prob_Dolomite * Prob_gamma_greater_than60_Dolomite)+(Prob_Shale * Prob_gamma_greater_than60_Shale))
if Prob_Dolomite_gamma_greater_than_60>=0.5:
    print('DOLOMITE')
else:
    print('SHALE')
