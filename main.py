from personaldata.chess_statistics import ChessStatistics
from personaldata.github_statistics import GithubStatistics
from personaldata.getwebsite import GetWebsiteMixin


if __name__ == '__main__':

    client = ChessStatistics("zosialaa")
    client.data_chess()

    client1 = GithubStatistics("zosialaa")
    client1.data_github()
