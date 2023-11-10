import unittest
from personaldata.chess import ChessStatistics


class StatisticsTests(unittest.TestCase):
    def test_construktor(self):
        client = ChessStatistics("zosialaa")
        client.data()
        
    def test_show_data(self):
        client1= ChessStatistics("zosialaa")
        client1.data()
        self.assertTrue(len(client1.table_data) > 0)