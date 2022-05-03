dcc = float(input('Number of Dolomite Cores: '))
dcs = float(input('Number of shale cores: '))
# Total number of Cores
ndc = dcc+dcs
#unconditional probability that the interval is Dolomite or Shale
PD = dcc/ndc
PS = dcs/ndc
#conditional probability of obtaining a gamma log reading greater than 60 in the Dolomite and Shale lithology
loc = float(input('Mean of Dolomite Data: '))
scale = float(input('Standard Deviation of Dolomite Data: '))
loc_S = float(input('Mean of Shale Data: '))
scale_S = float(input('Standard Devition of Shale data: '))
import scipy.stats
PodD60 = 1-scipy.stats.norm(loc,scale).cdf(60)
podS60 = 1-scipy.stats.norm(loc_S,scale_S).cdf(60)
#Baye’s Theorem to classify intervals in the formation as either as Dolomite or Shale
PlD_gamma60 = (PD*PodD60)/((PD*PodD60)+(PS*podS60))
#Classifying The Intervals
if PlD_gamma60 >= 0.5:
    print('The Interval is Dolomite.')
else:
    print('It is a Shale Interval.')
