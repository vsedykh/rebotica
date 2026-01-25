import bs4
import requests
import tkinter
from tkinter import ttk
class Parser:
    def __init__(self,ssylka = "https://steamspy.com"):
        self.ssylka = ssylka
        parser = requests.get(self.ssylka).text
        self.soup = bs4.BeautifulSoup(parser,"html.parser")
    def get_games_data(self,limit = 53):
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
                                       "players" : mox4}

            return games_data
    def get_games_detail(self,game_link):
        request = requests.get("https://steamspy.com"+game_link).text
        soup = bs4.BeautifulSoup(request, "html.parser")
        detail = {}
        for r in soup.find_all("strong"):
            keys = r.get_text(strip=True).replace(":","")




class App:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.root.title("steem spay")
        self.parser = Parser()
        self.fraim = ttk.Frame(self.root)
        self.fraim.pack(fill=tkinter.BOTH, expand = True)
        self.tree = ttk.Treeview(self.fraim, columns=["name","release_date","price"],show="headings" )
        self.tree.heading("name", text="Название")
        self.tree.heading("release_date", text="Дата выхода")
        self.tree.heading("price", text="Цена")
        self.tree.pack(fill=tkinter.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>",self.get_info())
    def populate_table(self):
        getgamesdata = self.parser.get_games_data()
        for h,l in getgamesdata.items():
            self.tree.insert("",tkinter.END,text=h,values=(l["name"],l["release_date"],l["price"],l["rating"],l["players"]))
    def get_info(self):
        selectitem = self.tree.selection()[0]
        ssylkanaigru = self.tree.item(selectitem,'text')




if __name__ == "__main__":
    app = App()
    app.populate_table()
    app.root.mainloop()