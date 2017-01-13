import cluster_app
import unittest

class ClusterAppTestCase(unittest.TestCase):

    def setUp(self):
        cluster_app.app.config['TESTING'] = True
        self.app = cluster_app.app.test_client()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
