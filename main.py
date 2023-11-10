from personaldata.chess_statistics import ChessStatistics
from personaldata.github_statistics import GithubStatistics
from personaldata.getwebsite import GetWebsiteMixin

#client1 = GetWebsiteMixin()
#html = client1.get_website_html("https://www.chess.com/pl/member/zosialaa")
#print(html)

if __name__ == '__main__':
    
        client = ChessStatistics("zosialaa")
        client.data_chess()
        
        client1 = GithubStatistics("zosialaa")
        client1.data_github()