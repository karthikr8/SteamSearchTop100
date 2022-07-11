# Program to search the most played top 100 games on Steam

import requests
import bs4

req = requests.get("https://store.steampowered.com/stats/")
soup = bs4.BeautifulSoup(req.text,'lxml')

top_100 = soup.select('.gameLink')
game_links = [game['href'] for game in top_100]

# SEARCH CRITERIA
tag = input('What tag do you need in top 100?:')

# LOGIC

games_requested = []
for game in game_links:
    req = requests.get(game)
    soup = bs4.BeautifulSoup(req.text,'lxml')
    tagclass = soup.select('.app_tag')
    if tag in str(tagclass):
        games_requested.append(soup.select('.apphub_AppName')[0].text)

# OUTPUT WITH THE USER REQUEST TAG

print(games_requested)