import bs4
import requests
class Parser:
    def __init__(self,ssylka = "https://steamspy.com"):
        self.ssylka = ssylka
        parser = requests.get(self.ssylka).text
        self.soup = bs4.BeautifulSoup(parser,"html.parser")
    def get_games_data(self,limit = 12):
            games_data = {}
            box = self.soup.find("table")
            boxtr = box.find_all("tr")
            for d in boxtr[1:limit]:
                    vox = d.find_all("td")
                    voxa = vox[1].find("a")
                    voxhref = voxa["href"].strip()
                    game_name = voxa.get_text(strip=True)
                    mox1 = vox[2].get_text(strip=True)
                    mox2 = vox[3].get_text(strip=True)
                    mox3 = vox[4].get_text(strip=True)
                    mox4 = vox[5].get_text(strip=True)
                    games_data[voxhref] = {"name":  game_name,
                                       "release_date" : mox1,
                                       "price" : mox2,
                                       "rating" : mox3,
                                       "players" : mox4
                                       }
            return games_data
if __name__ == "__main__":
    parser = Parser()
    agu = parser.get_games_data()
    for k,v in agu.items():
        #prises = mox2
        #def filter_prises(price):
            #filtered_prices = []
            #for price in prises:
                #if prises.startswith("$") and not (prises == "$0"):
                    #filtered_prices.append(prises)
                    #return filtered_prices
        print(k, v["name"])
        print(v["release_date"])
        print(v["price"])
        print(v["rating"])
        print(v["players"])

        #filtered_games = filter_prises(v)

        #print("Фильтрованные цены:", filtered_games)