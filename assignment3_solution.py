# to the only wise God!!!

# Bayes Classifier script

# Input statements - 1 mark
count_dolomite = float(input('How many Dolomite cores samples?'))
count_shale = float(input('How many Shale cores samples?'))
mean_dolomite = float(input('What is the mean of gamma ray data for Dolomite?'))                   
mean_shale = float(input('What is the mean of gamma ray data for Shale?'))
stdev_dolomite = float(input('What is the standard deviation of gamma ray data for Dolomite?'))                   
stdev_shale = float(input('What is the standard deviation of gamma ray data for Shale?'))

# Import needed library
import scipy.stats

# Computations - 1 mark
uncond_prob_dolomite = count_dolomite/(count_dolomite + count_shale)
cond_prob_gamma60_dolomite = 1 - scipy.stats.norm(loc = mean_dolomite, scale = stdev_dolomite).cdf(60)
uncond_prob_shale = count_shale/(count_dolomite + count_shale)
cond_prob_gamma60_shale = 1 - scipy.stats.norm(loc = mean_shale, scale = stdev_shale).cdf(60)

total_prob_gamma60 = (uncond_prob_dolomite*cond_prob_gamma60_dolomite) + (uncond_prob_shale*cond_prob_gamma60_shale)
cond_prob_dolomite = (uncond_prob_dolomite*cond_prob_gamma60_dolomite)/total_prob_gamma60

# Facie classification - 1 mark
if cond_prob_dolomite >= 0.5:
    print("Interval is Dolomite")
else:
    print("Interval is Shale")
        


