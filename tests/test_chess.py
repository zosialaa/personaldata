import unittest
from personaldata.chess_statistics import ChessStatistics


class StatisticsTests(unittest.TestCase):
    def test_construktor(self):
        client = ChessStatistics("zosialaa")
        client.data_chess()
