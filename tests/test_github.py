import unittest
from personaldata.github_statistics import GithubStatistics


class GithubStatisticsTest(unittest.TestCase):
    def test_construktor(self):
        client3 = GithubStatistics("zosialaa")
        self.assertTrue(client3 is not None)


    def test_data_github(self):
        api_client2 = GithubStatistics('zosialaa')
        api_client2.data_github()
        self.assertTrue(api_client2 is not None )