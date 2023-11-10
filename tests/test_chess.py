import unittest
from personaldata.chess_statistics import ChessStatistics


class StatisticsTests(unittest.TestCase):
    def test_construktor(self):
        client = ChessStatistics("zosialaa")
        client.data_chess()
        
    def test_data_chess(self):
        client1= ChessStatistics("zosialaa")
        client1.data_chess()
        self.assertTrue(len(client1.table_data) > 0)
