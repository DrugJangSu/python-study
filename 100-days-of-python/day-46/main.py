import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date.split("-")[0]


## Due to the Billboard chart is now asking for a pro subscription, gonna change to the wikipedia
 
url = f"https://en.wikipedia.org/wiki/Billboard_Year-End_Hot_100_singles_of_{year}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')

song_names_spans = soup.select("table.wikitable tbody tr td:nth-of-type(2)")
song_names = [song.getText().strip().strip('"') for song in song_names_spans]

print(song_names[:10])