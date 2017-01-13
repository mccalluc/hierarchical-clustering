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
            covariance = np.diagflat([1] * cols)
            matrix = np.random.multivariate_normal(means, covariance, rows)
            return matrix.round(2).tolist()

        np.random.seed(1)
        cols = 5
        rows = 10
        combined = random_matrix([10] * cols, rows) + random_matrix([20] * cols, rows)
        combined_json = json.dumps(combined)
        r = self.app.get('/cluster?matrix=%s' % combined)
        permutation = json.loads(r.data)
        # The important part is that the two chunks are segregated;
        # precise order will be different with different random seed.
        self.assertTrue(all([x >= 10 for x in permutation[:10]]))
        self.assertTrue(all([x < 10 for x in permutation[-10:]]))
        self.assertEqual(permutation, [13, 14, 15, 11, 12, 16, 17, 19, 10, 18, 0, 2, 1, 6, 3, 5, 7, 8, 4, 9])


if __name__ == '__main__':
    unittest.main()
