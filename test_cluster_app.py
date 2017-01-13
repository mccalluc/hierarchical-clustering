import cluster_app
import unittest
import numpy as np
import json


class ClusterAppTestCase(unittest.TestCase):
    def setUp(self):
        cluster_app.app.config['TESTING'] = True
        self.app = cluster_app.app.test_client()

    def tearDown(self):
        pass

    def test_small_matrix(self):
        r = self.app.get('/cluster?matrix=[[101],[1],[11],[2],[12],[102]]')
        self.assertEqual(r.data, '[0, 5, 2, 4, 1, 3]')

    def test_medium_matrix(self):
        def random_matrix(means, rows):
            cols = len(means)
            covariance = [[1] * cols] * cols
            matrix = np.random.multivariate_normal(means, covariance, rows)
            return matrix.round(2).tolist()
        np.random.seed(1)
        cols = 5
        rows = 10
        combined = random_matrix([10]*cols, rows) + random_matrix([20]*cols, rows)
        combined_json = json.dumps(combined)
        r = self.app.get('/cluster?matrix=%s' % combined)
        permutation = json.loads(r.data)
        self.assertEqual(permutation, [14, 15, 11, 18, 12, 13, 16, 10, 17, 19, 0, 2, 1, 7, 8, 3, 4, 9, 5, 6])


if __name__ == '__main__':
    unittest.main()
