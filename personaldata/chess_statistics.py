from bs4 import BeautifulSoup
from personaldata.getwebsite import GetWebsiteMixin


class ChessStatistics(GetWebsiteMixin):
    def __init__(self, nick):
        self.nick = nick
        self.url = f"https://www.chess.com/pl/member/{self.nick}"
        self.table_data = []

    def data_chess(self):
        r = self.get_website_html(self.url)
        soup = BeautifulSoup(r, "html.parser")
        buttons = soup.find_all("button", class_="stat-section-button")

        for button in buttons:
            dic = {}
            dic['name'] = button.find(
                'span', class_="stat-section-section-link-name").text
            dic['score'] = button.find(
                'div', class_="stat-section-user-rating").text
            self.table_data.append(dic)

        print(self.table_data)
