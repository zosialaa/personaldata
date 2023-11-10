import unittest
from personaldata.github_statistics import GithubStatistics


class GithubStatisticsTest(unittest.TestCase):
    def test_construktor(self):
        client = GithubStatistics("zosialaa")
        self.assertTrue(client is not None)


    def test_data(self):
        api_client2 = GithubStatistics('zosialaa')
        api_client2.data_github()
        self.assertTrue(api_client2 is not None )