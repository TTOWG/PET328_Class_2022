#defining variables
loc_D = float(input('enter loc for dolomite: '))
scale_D = float(input('enter scale for dolomite: '))

loc_S = float(input('enter loc for shale: '))
scale_S = float(input('enter scale for shale: '))

count_D = float(input('enter count for dolomite: '))
count_S = float(input('enter count for shale: '))

#to get total number of all cores
count_total = count_D + count_S
p_D = (count_D / count_total)
p_S = count_S / count_total

#defining parameters
#p_gamma_D = p(gamma>60|D)
#p_gamma_S = p(gamma>60|S)
#p_gamma_D_60 = p(D|gamma>60)

#import scipy
import scipy.stats
p_gamma_D = 1 - scipy.stats.norm(loc_D, scale_D).cdf(0.5)
p_gamma_S = 1 - scipy.stats.norm(loc_S, scale_S).cdf(0.5)
p_gamma_D_60  = (p_D * p_gamma_D) / ((p_D * p_gamma_D) + (p_S * p_gamma_S))

#the interval classification
if p_gamma_D_60 >= 0.5:
    print('It is a Dolomite interval')
else:
    print('It Shale interval')
