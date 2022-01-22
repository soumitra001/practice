import requests
from bs4 import BeautifulSoup

URL="http://www.imdb.com/chart/top"
response = requests.get(URL)


src_content=response.content
soup=BeautifulSoup(response.text,"html.parser")

movietags=soup.select('td.titleColumn')
#print(movietags)
inner_movietags = soup.select('td.titleColumn a')
#print(inner_movietags)

titles=[tag.text for tag in inner_movietags]
print("\n****************\n")
length=len(titles)
for idx in range(length) :
 print(titles[idx])


