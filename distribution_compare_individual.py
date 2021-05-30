def distribution_compared_individual(data, sample_size= 10000):
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



    #####################################
    #####################################
    # Individual level comparison
    for jj, ll in zip(graphs['Subject'], graphs['Degree_dist']):
        path = jj[0]
        deg_dist = ll

        centered_deg_mean = np.asarray(deg_dist) - np.mean(deg_dist)

        data_uniform = uniform.rvs(size=sample_size, loc = np.min(centered_deg_mean), scale=np.max(centered_deg_mean))

        data_normal = norm.rvs(size=sample_size,loc=np.median(centered_deg_mean),scale=1)

        data_gamma = gamma.rvs(a=5, size= sample_size)

        data_expon = expon.rvs(scale=1,loc= np.median(centered_deg_mean),size= sample_size)

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


        uniform_test = list(['Uniform:', stats.kstest(centered_deg_mean, data_uniform)])
        normal_test = list(['Normal', stats.kstest(centered_deg_mean, data_normal)])
        gamma_test = list(['Gamma', stats.kstest(centered_deg_mean, data_gamma)])
        exponential_test = list(['Exponential', stats.kstest(centered_deg_mean, data_expon)])
        poisson_test = list(['Poisson', stats.kstest(centered_deg_mean, data_poisson)])
        triang_test = list(['Triang', stats.kstest(centered_deg_mean, data_triang)])
        lognormal_test = list(['Lognormal', stats.kstest(centered_deg_mean, data_lognorm)])
        weibull_test = list(['Weibull', stats.kstest(centered_deg_mean, data_weibull)])

        for ii, kk  in zip(Distributions, dist_names):
            sns.set_context('talk')
            ax = sns.histplot(ii,
                             bins = 50,
                             kde= True,
                            color = 'skyblue')
                            #hist_kws={'linewidth':15, 'alpha':1})
            ax.set(title= kk + ' Sample Degree Distribution', ylabel = 'Frequency')
            aj = sns.histplot(centered_deg_mean,
                      bins= 50,
                      kde=True,
                      color='forestgreen')
            plt.savefig( path + '/reports/' + kk +  ' Sample Degree Distribution.png')
            plt.clf()





        ks_test_results_individual= [uniform_test, normal_test, gamma_test, exponential_test, poisson_test,
                                     triang_test, lognormal_test, weibull_test]

        with open(path + '/reports/' +'ks_test_results' + jj[0] +'.txt', 'w') as filehandle:
            for listitem in ks_test_results_individual:
                filehandle.write('%s\n' % listitem)

    return
