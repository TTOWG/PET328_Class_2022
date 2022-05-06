import scipy.stats
dol = float(input('Enter Dolomite core number:'))
shl = float(input('Enter Shale core number:'))
dol_mean = float(input('Enter Dolomite Mean value:'))
shl_mean = float(input('Enter Shale Mean value:'))
dolSD = float(input('Enter Dolomite Standard Deviation:'))
shlSD = float(input('Enter Shale Standard Deviation:'))
Tcore = dol + shl
#P(D) and P(s) being calculated
PD = dol/Tcore
PS = shl/Tcore
#P(gamma>60|D) and P(gamma>60|S) being calculated
PDF = 1 - scipy.stats.norm(loc = dol_mean, scale = dolSD).cdf(0.5)
PSF = 1 - scipy.stats.norm(loc = shl_mean, scale = shlSD).cdf(0.5)
#Define the formula
a = PD*PDF
b = PS*PSF
ab = (a)/(a+b)
#Define intervals
if ab >= 0.5:
    print('The interval is Dolomite')
else:
    print('The interval is shale')


