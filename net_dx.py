def net_dx(path_to_csv, path_to_nodes):


"""This function works to provide a number of network diagnostics to get a picture of some basic metrics of a given network or set of networks"""


    import scipy.io
    import numpy as np
    import pandas as pd
    import igraph as ig
    import seaborn as sns
    import glob
    import os
    import matplotlib.pyplot as plt


    os.chdir(path_to_csv)
    FilenamesList = glob.glob('*.csv', recursive=True)

    nets = scipy.io.loadmat(path_to_nodes)

    comms = nets['comms']
    final_comms = []
    for tt in comms:
        for ll in tt:
            final_comms.append(ll)

    nodes = nets['nodes']

    nodes = nodes[0]

    final_node = []
    for ii in nodes:
        for jj in ii:
            final_node.append(jj)



    mats = []
    ad_mat= []
    dfs = []
    graphs = {'Subject': [],
             'graph_obj': [],
              'Strength':[],
              'Degree_Assortativity': []
             };
    for mat in FilenamesList:
        mats.append(scipy.io.loadmat(mat))
        plt.clf();
        for adjacencies in mats:
            plt.clf();
            ad_mat=adjacencies['CorrMat']
            dfs.append(pd.DataFrame(ad_mat,columns = final_node, index=final_comms))
                #df.to_csv(mat + '.csv', index=True, header=True)
        g = ig.Graph.Adjacency((ad_mat > 0).tolist())
        g.es['weight'] = ad_mat[ad_mat.nonzero()]
        g.vs['label'] = final_node
        g.vs.select(_degree = g.maxdegree())
        graphs['Subject'].append(mat)
        graphs['graph_obj'].append(g)
        sns.displot(g.degree(), bins=20)
        plt.title(mat)
        plt.savefig(mat + 'degreedistribution.jpg')
        plt.clf();
        for df in dfs:
            df.to_dict()
            sns.heatmap(df, center = 0)
            plt.title(mat)
            plt.savefig(mat + 'heatmap.png')
            plt.clf();

##############################Compute metrics and diagnostic measures

        strengths = []
        degree_assortativity = []
        for subject in graphs['Subject']:
            for graph in graphs['graph_obj']:
                strengths.append(statistics.mean(graph.strength(loops=False, weights = graph.es['weight'], mode='all')))
                graphs['Strength'].append(statistics.mean(graph.strength(loops=False, weights = graph.es['weight'], mode='all')))
                sns.displot(graph.strength(loops=False, weights = graph.es['weight'], mode='all'), bins = 20)
                plt.title(subject)
                plt.savefig(subject + 'strength_distribution.jpg')
                plt.clf();
                Get Degree Assortativity and append to list and graphs dict.
                degree_assortativity.append(graph.assortativity_degree(directed=False))
                graphs['Degree_Assortativity'].append(graph.assortativity_degree(directed=False))



############################## Distribution comparisons.
