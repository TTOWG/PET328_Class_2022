numdolo_cr = float(input('What is the number of dolomite'))
numsha_cr = float(input('What is the number of shale'))
meandolo_me = float(input('What is the mean of dolomite'))
meansha_me = float(input('What is the mean of shale'))
stadolo_st = float(input('What is the standard deviation of dolomite'))
stasha_st = float(input('What is the standard deviation of shale'))

numb_allcrs = numdolo_cr + numsha_cr #number of all cores
P_D = numdolo_cr/numb_allcrs
P_S = numsha_cr/numb_allcrs

import scipy.stats

pgamgre_60d = 1 - scipy.stats.norm(meandolo_me, stadolo_st).cdf(0.5)
pgamgre_60s = 1 - scipy.stats.norm(meansha_me,stasha_st ).cdf(0.5)


pdgamgre_60 = P_D*pgamgre_60d/P_D*pgamgre_60d + P_S*pgamgre_60s


if pdgamgre_60 >= 0.5:
    print('The interval is Dolomite')
else:
    print('The interval is Shale')

