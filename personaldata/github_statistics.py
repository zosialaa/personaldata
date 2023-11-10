import requests
from bs4 import BeautifulSoup

from personaldata.getwebsite import GetWebsiteMixin


class GithubStatistics(GetWebsiteMixin):
    def __init__(self, nick):
        self.nick = nick
        self.url = f"https://github.com/{self.nick}"
        self.data_dict = {}

    def data_github(self):
        r = self.get_website_html(self.url)
        soup = BeautifulSoup(r, "html.parser")
        tab = soup.find_all("span", class_="Counter")

        self.data_dict = {}

        if len(tab) >= 4:
            self.data_dict['repositories'] = tab[0].get_text()
            self.data_dict['projects'] = tab[1].get_text()
            self.data_dict['packages'] = tab[2].get_text()
            self.data_dict['stars'] = tab[3].get("title").replace(",", "")
        print(self.data_dict)
        return self.data_dict
