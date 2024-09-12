Num_of_Dolo= float(input('Enter number of Dolomite cores:'))
Num_of_shale= float(input('Enter number of shale cores:'))

Mean_Dolo= float(input('Enter the mean of Dolomite:'))
Mean_Shale= float(input('Enter the mean of Shale:'))

Dev_Dolo= float(input('Enter the Standard Dev of Dolomite:'))
Dev_Shale= float(input('Enter the Standard Dev of Shale:'))

Total = Num_of_Dolo + Num_of_shale
P_D = Num_of_Dolo/Total
P_S= Num_of_shale/Total


print('P(D) =',P_D)
print('P(S) =',P_S)


import scipy.stats


p_gamma_greaterthan_60_D = 1 - scipy.stats.norm(Mean_Dolo, Dev_Dolo).cdf(60)
p_gamma_greaterthan_60_S = 1 - scipy.stats.norm(Mean_Shale, Dev_Shale).cdf(60)


print('P(gamma>60|D) =',p_gamma_greaterthan_60_D)
print('P(gamma>60|S) =',p_gamma_greaterthan_60_S)


P_D_GAMMA_GREATERTHAN_60 = (P_D * p_gamma_greaterthan_60_D)/((P_D * p_gamma_greaterthan_60_D)+\
                                        (P_S * p_gamma_greaterthan_60_S))


if P_D_GAMMA_GREATERTHAN_60  >= 0.5:
    print('The interval is Dolomite')
else:
    print('It is a shale interval')

