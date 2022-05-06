n_DC = float(input('Number Of Dolomite Cores: '))
n_SC = float(input('Number Of Shale Cores: '))
n_TC = n_DC + n_SC
PD = n_DC / n_TC
PS = n_SC / n_TC
locD = float(input('Mean of Dolomite Data : '))
sdD = float(input('Standard Deviation of Dolomite data: '))
locS = float(input('Mean of Shale Data: '))
sdS = float(input('Standard Deviation of Shale Data: '))
import scipy.stats
#pgD = conditionals for gamma readings
pgD = 1-scipy.stats.norm(locD,sdD).cdf(60)
pgS = 1-scipy.stats.norm(locS,sdS).cdf(60)
# computing baye's Theorem
pdG = (PD * pgD) / ((PD * pgD) + (PS * pgS))
#Determining the interval
if pdG>=0.5:
    print('interval is Dolomite')
else:
    print('interval is Shale')
