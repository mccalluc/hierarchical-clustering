from scipy.cluster.hierarchy import linkage, leaves_list

class Cluster:

    def __init__(self, data):
        self.data = data

    def cluster(self):
        Z = linkage(self.data, 'ward')
        return leaves_list(Z).tolist()