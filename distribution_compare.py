def distribution_compare(sample_size= 10000, data):
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
    from scipy.stats import uniform, norm, gamma, expon, poisson, triang, lognorm
    from numpy.random import weibull

    Distributions = [data_uniform, data_normal, data_gamma, data_expon, data_poisson, data_triang, data_lognorm, data_weibull]

    data_uniform = uniform.rvs(size=n, loc = start, scale=width)
    data_normal = norm.rvs(size=n,loc=0,scale=1)
    data_gamma = gamma.rvs(a=5, size=n)
    data_expon = expon.rvs(scale=1,loc=0,size=n)
    mu=3
    data_poisson = poisson.rvs(mu=mu, size=n)
    c= 0.158
    data_triang = triang.rvs(c=c, size = n)
    s = 0.954
    data_lognorm = lognorm.rvs(s=s, size = n)
    data_weibull = np.random.weibull(a, n)

    for ii in Distributions:
        ax = sns.displot(ii,
                         bins = 100,
                         kde= True,
                        color = 'skyblue',
                        hist_kws={'linewidth':15, 'alpha':1})
        ax.set(label= str(ii), ylabel = 'Frequency')
