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
    dfs = []
    graphs = {'Subject': [],
             'graph_obj': [],
              'Strength':[],
              'Degree_dist': [],
              'Degree_mean': [],
              'Degree_category': [],
              'Degree_Assortativity': [],
              'Disconnections':[],
              'SWP_binary': []
             };
    for mat in FilenamesList:
        mats.append(scipy.io.loadmat(mat))
        plt.clf();
        # make a folder per each subject
        sub = mat.split('.')
        sub_folder = path + sub[0]
        if not os.path.exists(sub_folder):
            os.makedirs(sub_folder)

        # make reports folder within each subject folder
        dir = 'reports'
        reports_path = os.path.join(sub_folder, dir)
        if not os.path.exists(reports_path):
            os.makedirs(reports_path)

        for adjacencies in mats:
            plt.clf();
            ad_mat=adjacencies['CorrMat']
            my_mat = pd.DataFrame(ad_mat,columns = final_node, index=final_comms)
            # write adjacency csv to subject folder
            my_mat.to_csv(sub_folder +'/' + sub[0] + '.csv', index=True, header=True)

        g = ig.Graph.Weighted_Adjacency((ad_mat > 0).tolist(), attr='weight', mode='max')
        weights = ad_mat[ad_mat.nonzero()]
        g.es['weight'] = ad_mat
        g.vs['label'] = final_node
        g.vs.select(_degree = g.degree)
        g.vs.select(_degree=0).delete()
        g = g.as_undirected()
    #     ig.Graph.write_adjacency(g, sub_folder +'/' + sub[0] + '_for_swp.csv', sep = ',', attribute='weight', eol='\n')
        graphs['Subject'].append(mat.split('.'))
        graphs['graph_obj'].append(g)
        graphs['Degree_dist'].append(g.degree(mode='all'))

        # tells you whether the graph is connected or not or if there are disconnected components.
        graphs['Disconnections'].append(g.is_connected(mode='strong'))

        sns.histplot(g.degree(), bins=20)
        plt.title(mat)
        plt.savefig(reports_path + '/' + sub[0] + '_degreedistribution.jpg')


        my_mat.to_dict()
        sns.heatmap(my_mat, center = 0, square = True)
        plt.figure.figsize=(10,10)
        plt.title(mat)
        plt.tight_layout()
        plt.savefig(reports_path + '/' + sub[0] + '_heatmap.png', transparent = False)
        plt.clf();

############################## Distribution comparisons.
