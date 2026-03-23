from networkx.algorithms.community import greedy_modularity_communities
communities = list(greedy_modularity_communities(G))
community_labels = {node: i for i, community in enumerate(communities) for node in community}
print(community_labels)