def graph_strength(data):
    strengths = []
    degree_assortativity = []
    for subject, graph in zip(graphs['Subject'], graphs['graph_obj']):
        graphs['Strength'].append(stat.mean(graph.strength(loops=False)))

        sns.displot(graph.strength(loops=False), bins = 20);
        plt.title(subject);
        plt.savefig(subject[0] + '/' + '/reports/'  + subject[0] + '_strength_distribution.png', transparent = False);
        plt.clf();
#         Get Degree Assortativity and append to list and graphs dict.
        degree_assortativity.append(graph.assortativity_degree(directed=False))
        graphs['Degree_Assortativity'].append((graph.assortativity_degree(directed=False)))
