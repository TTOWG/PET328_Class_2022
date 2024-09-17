nmdolo_cr = float(input('What is the number of dolomite'))
nmshle_me = float(input('what is the number of shale'))
mndolo_me = float(input('What is the mean of dolomite'))
mnshle_me = float(input('what is the mean of shale'))
stddolo_st = float(input('whatis the standard deviation of dolomite'))
stdshle_st = float(input('what is the standard deviation of shale'))

nm_allrcs =nmdolo_cr + nmshle_me # number of all cores
P_D = nmdolo_cr/nm_allrcs
P_S = nmshle_me/nm_allrcs


import scipy.stats

pgamgre_60d = 1- scipy.stats.norm(mndolo_me, stddolo_st).cdf(0.5)
pgamgre_60s = 1- scipy.stats.norm(mnshle_me, stdshle_st).cdf(0.5)



pgamgre_60 = P_D*pgamgre_60d/P_D*pgamgre_60d + P_S*pgamgre_60s


if pgamgre_60 >= 0.5:
    print('The interval is dolomite')

else:
    print('The interval is shale')  
