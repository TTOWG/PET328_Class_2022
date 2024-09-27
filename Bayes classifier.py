import scipy.stats
dolV =float(input('Enter Dolomite core count: '))
shaV =float(input('Enter Shale core count: '))
dolM =float(input('Enter Dolomite Mean value: '))
shaM =float(input('Enter Shale Mean value: '))
dolSD =float(input('Enter Dolomite Standard Deviation: '))
shalSD =float(input('Enter Shale Standard Deviation: '))
Tcore = dolV + shaV
#P(D) and P(S) being calculated
PD = dolV/Tcore
PS = shaV/Tcore
#P(gamma>60|D) and P(gamma>60|S) being calculated
PDF = 1 - scipy.stats.norm(loc = dolM, scale = dolSD).cdf(0.5)
PSF = 1 - scipy.stats.norm(loc = shaM, scale = shalSD).cdf(0.5)
#Define the formula
x = PD * PDF
y = PS * PSF
xy = (x)/ (x + y)
#Define intervals
if xy >= 0.5:
    print('Your interval is Dolomite')
else:
    print('Your interval is Shale')































1 - scipy.stats.norm(loc = 0, scale = 1).cdf(0.5)
