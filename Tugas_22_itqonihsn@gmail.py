from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
import pandas as pd

#--------------------------------------------------------------------------------

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
headers = {'User-Agent': user_agent, 'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'}

alamat = 'https://www.kompas.com/'

#--------------------------------------------------------------------------------

data_request = Request(alamat, headers=headers)
response = urlopen(data_request)
soup = bs(response, "html.parser")

#--------------------------------------------------------------------------------

berita_populers = soup.find_all("h4",{"class":"most__title"})

judul_berita_populer = [berita_populer.get_text() for berita_populer in berita_populers]

df_judul_berita_populer = pd.DataFrame(judul_berita_populer, columns=['Judul Berita Populer'])
print(df_judul_berita_populer)