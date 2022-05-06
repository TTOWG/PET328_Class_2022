dolo_num = float(input('What is the number of dolomite'))
sha_num = float(input('What is the number of shale'))
dolo_mean = float(input('What is the mean of dolomite'))
sha_mean = float(input('What is the mean of shale'))
dolo_sta = float(input('What is the standard deviation of dolomite'))
sha_sta = float(input('What is the standard deviation of shale'))

allcrs_num = dolo_num + sha_num #number of all cores
P_D = dolo_num/allcrs_num
P_S = sha_num/allcrs_num

import scipy.stats

pgamgre_60d = 1 - scipy.stats.norm(dolo_mean, dolo_sta).cdf(0.5)
pgamgre_60s = 1 - scipy.stats.norm(sha_mean, sha_sta).cdf(0.5)


pdgamgre_60 = P_D*pgamgre_60d/P_D*pgamgre_60d + P_S*pgamgre_60s


if pdgamgre_60 >= 0.5:
    print('The interval is Dolomite')
else:
    print('The interval is Shale')
