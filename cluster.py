from scipy.cluster.hierarchy import linkage, leaves_list


# Good tutorial on hierarchical clustering:
# https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/

class Cluster:
    def __init__(self, data):
        self.data = data

    def cluster(self):
        Z = linkage(self.data, 'ward')
        return leaves_list(Z).tolist()
