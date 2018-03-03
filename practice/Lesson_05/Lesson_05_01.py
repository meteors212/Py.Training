from scipy import stats
one_sample_data = [15.48,4.4,5.81,6.07,5.19,3.25,4.41,5.05,11.63,8.99]
one_sample = stats.ttest_1samp(one_sample_data, 8)
print(one_sample[1]/2)