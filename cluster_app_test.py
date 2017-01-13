import cluster_app
import unittest

class ClusterAppTestCase(unittest.TestCase):

    def setUp(self):
        cluster_app.app.config['TESTING'] = True
        self.app = cluster_app.app.test_client()

    def tearDown(self):
        pass

    def test_small_matrix(self):
        r = self.app.get('/cluster?matrix=[[101],[1],[11],[2],[12],[102]]')
        self.assertEqual(r.data, '[0, 5, 2, 4, 1, 3]')

if __name__ == '__main__':
    unittest.main()
