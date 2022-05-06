Num_of_dolo= float(input('Enter number of dolomite cores: '))
Num_of_Shale= float(input('Enter number of Shale cores: '))

Mean_of_dolo= float(input('Enter the mean of dolomite: '))
Mean_of_Shale= float(input('Enter the mean of Shale: '))

Dev_of_dolo= float(input('Enter the standard Dev of dolomite: '))
Dev_of_Shale= float(input('Enter the standard Dev of Shale: '))

Total = Num_of_dolo + Num_of_Shale
P_D = Num_of_dolo/Total
P_S = Num_of_Shale/Total

print('P(D) =',P_D)
print('P(S) =',P_S)

import scipy.stats

p_gamma_greaterthan_60_D = 1 - scipy.stats.norm(Mean_of_dolo, Dev_of_dolo).cdf(60)
p_gamma_greaterthan_60_S = 1 - scipy.stats.norm(Mean_of_Shale, Dev_of_Shale).cdf(60)

print('P(gamma>60(D) =',p_gamma_greaterthan_60_D)
print('P(gamma>60(S) =',p_gamma_greaterthan_60_S)

P_D_GAMMA_GREATERTHAN_60 = ((P_D + p_gamma_greaterthan_60_D)/((P_D * p_gamma_greaterthan_60_D)+\
                                                             (P_S * p_gamma_greaterthan_60_S)))

if P_D_GAMMA_GREATERTHAN_60 >= 0.5:
    print('The interval is dolomite')
else:
    print('It is a Shale interval')
