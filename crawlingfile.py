import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.billboard.com/charts/hot-100')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
rank = soup.select(
   'li > button > span.chart-element__rank.flex--column.flex--xy-center.flex--no-shrink > span.chart-element__trend > i > span'
)
song = soup.select(
   'li > button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary'
)
singer = soup.select(
   'li > button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary'
)
music_chart = []
for items in zip(rank, song, singer):
    music_chart.append(
        {
            'rank'  : items[0].text,
            'song'  : items[1].text,
            'singer': items[2].text,
        }
    )

for row in music_chart:
    print(row['rank'],'/.' , row['song'],'/.' ,row['singer'])