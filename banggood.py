from urllib.request import urlopen
from bs4 import BeautifulSoup

class BanggoodClient():

    def __init__(self):
        super(BanggoodClient,self).__init__

    def download_page(self,url):
        html = urlopen(url)
        page = html.read()
        html.close()
        return page

    def search_prices(self,page):
        soup = BeautifulSoup(page,'lxml')
        prices_list=[]
        price_old_list=[]
        titles_list=[]
        ul = soup.find("ul","goodlist_1")
        li = ul.find_all("li")

        for product in li:
            title = product.find("span","title")
            price_old = product.find("span","price_old")
            price = product.find("span","price")
            print(title.text + " OLD PRICE: " + price_old['oriprice'] + " DISCOUNT: " + price['oriprice'])
            print('\n')
        return titles_list,price_old_list,prices_list,

    def run(self):
        page = self.download_page("https://www.banggood.com/es/Flashdeals.html")
        data = self.search_prices(page)
        print(data)

if __name__ == "__main__":
    c = BanggoodClient()
    c.run()
