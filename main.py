from personaldata.chess import ChessStatistics
from personaldata.getwebsite import GetWebsiteMixin

#client1 = GetWebsiteMixin()
#html = client1.get_website_html("https://www.chess.com/pl/member/zosialaa")
#print(html)

if __name__ == '__main__':
    
        client = ChessStatistics("ELMimiaczek")
        client.data()