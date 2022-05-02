dcc = float(input('Number of Dolomite Cores: '))
ndc = float(input('Number of all cores: '))
PD = dcc/ndc
loc = float(input('Mean of Dolomite Data: '))
scale = float(input('Standard Deviation of Dolomite Data: '))
import scipy.stats
PodD60 = 1-scipy.stats.norm(loc,scale).cdf(60)

dcs = float(input('Number of shale cores: '))
PS = dcs/ndc
loc = float(input('Mean of Shale Data: '))
scale = float(input('Standard Devition of Shale data: '))
import scipy.stats
podS60 = 1-scipy.stats.norm(loc,scale).cdf(60)
PlD_gamma60 = (PD*PodD60)/(PD*PodD60+PS*podS60)
if PlD_gamma60 >= 0.5:
    print('The Interval is Dolomite')
else:
    print('It is a Shale Interval')
