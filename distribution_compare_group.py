def distribution_compared_group(data, sample_size= 10000, reports_path='.'):
    '''
    This function works to compare the degree distribution at the individual and group mean level to
    a number of standard distribution: Uniform, Normal, Gamma, Exponential, Poisson, Triangular,
    LogNormal, and Weibull. Further, the comparison is made using a one-way
    Kolmogorov-Smirnov test for goodness of fit and a p-value is computed at the individual
    and group level.

    params:
    sample size = number of random values to generate per distribution test--default val = 10000
    data = list of degree distributions
     '''
    from scipy import stats
    from scipy.stats import uniform, norm, gamma, expon, poisson, triang, lognorm, weibull_min
    import numpy as np
    from numpy.random import weibull
    import os
    import statistics


    #####################################
    # Group level comparison
    group_deg_mean = []
    for jj in data['Degree_dist']:
        group_deg_mean.append(statistics.mean(jj))

    group_deg_array = np.array(group_deg_mean)
    group_centered_deg_mean = group_deg_array - np.mean(group_deg_array)

    data_uniform = uniform.rvs(size=sample_size, loc = np.min(group_centered_deg_mean), scale=np.max(group_centered_deg_mean))

    data_normal = norm.rvs(size=sample_size,loc=np.median(group_centered_deg_mean),scale=1)

    data_gamma = gamma.rvs(a=5, size= sample_size)

    data_expon = expon.rvs(scale=1,loc= np.median(group_centered_deg_mean),size= sample_size)

    mu=3
    data_poisson = poisson.rvs(mu=mu, size= sample_size)

    c= 0.158
    data_triang = triang.rvs(c=c, size = sample_size)

    s = 0.954
    data_lognorm = lognorm.rvs(s=s, size = sample_size)

    a = 5.0
    data_weibull = np.random.weibull(a = a, size = sample_size)


    Distributions = [data_uniform, data_normal, data_gamma, data_expon, data_poisson, data_triang, data_lognorm, data_weibull]
    dist_names = ['Uniform', 'Normal', 'Gamma', 'Exponential', 'Poisson', 'Triangular', 'LogNormal', 'Weibull']


    group_uniform = ['Uniform:', stats.kstest(group_centered_deg_mean, data_uniform)]
    group_normal = ['Normal', stats.kstest(group_centered_deg_mean, data_normal)]
    group_gamma = ['Gamma', stats.kstest(group_centered_deg_mean, data_gamma)]
    group_exponential = ['Exponential', stats.kstest(group_centered_deg_mean, data_expon)]
    group_poisson = ['Poisson', stats.kstest(group_centered_deg_mean, data_poisson)]
    group_traing = ['Triang', stats.kstest(group_centered_deg_mean, data_triang)]
    group_lognormal = ['Lognormal', stats.kstest(group_centered_deg_mean, data_lognorm)]
    group_weibull = ['Weibull', stats.kstest(group_centered_deg_mean, data_weibull)]


    for ii, jj  in zip(Distributions, dist_names):
        sns.set_context('talk')
        ax = sns.histplot(ii,
                         bins = 50,
                         kde= True,
                        color = 'skyblue')
                        #hist_kws={'linewidth':15, 'alpha':1})
        ax.set(title= jj + ' Sample Degree Distribution', ylabel = 'Frequency')
        aj = sns.histplot(group_centered_deg_mean,
                  bins= 50,
                  kde=True,
                  color='forestgreen')
        plt.savefig(reports_path+ '/' + jj + ' Sample Degree Distribution.png')
        plt.clf()




    ks_test_results_group= [group_uniform, group_normal, group_gamma, group_exponential, group_poisson, group_traing, group_lognormal,
                            group_weibull]

    with open(reports_path + '/' + 'ks_test_results_group.txt', 'w') as filehandle:
                for listitem in ks_test_results_group:
                    filehandle.write('%s\n' % listitem)

    return ks_test_results_group
