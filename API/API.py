from igdb.wrapper import IGDBWrapper
wrapper = IGDBWrapper("18tfq728xi2b0cxvsnhs69znuzrelk", "ohuyxp4ws2kyof9mzq9i24odno25u0")

import requests
import json
import pandas as pd
from datetime import datetime

url = 'https://id.twitch.tv/oauth2/token'
myobj = {'client_id': '18tfq728xi2b0cxvsnhs69znuzrelk',
          'client_secret': 'ohuyxp4ws2kyof9mzq9i24odno25u0',
          'grant_type':'client_credentials'}

x = requests.post(url, data = myobj)

print(x.text)
i = x.json()

wrapper = IGDBWrapper("18tfq728xi2b0cxvsnhs69znuzrelk", i['access_token'])

# Obtencion de los juegos

print("Obtencion de los juegos")

num = [500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,7500,8000,8500]

for n in num:
    
    print(n)
    
    from igdb.igdbapi_pb2 import GameResult
    byte_array = wrapper.api_request(
                'games', 
                f'f name, cover.url, involved_companies.company.name, genres.name, screenshots.url, platforms.name, summary, first_release_date, aggregated_rating_count, aggregated_rating, rating, websites.url, category, similar_games.name; l 500; offset {n}; where websites.category = 1 & (category = 0 | category = 8) & first_release_date > 1199142000 & cover.url != null & involved_companies.company.name != null & screenshots.url != null & name !~ *"Hentai"* & name !~ *"Sex"* & summary !~ *"Hentai"* & summary !~ *"sex"*; sort first_release_date desc;'
              )
    games_message = GameResult()
    
    # Funcion para decodificar los bytes obtenidos en GameResult(), cargarlo como json y pasarlo a un DataFrame
    
    data = pd.json_normalize(json.loads(byte_array.decode('utf-8')))
    
    data = data.set_index('id')
    
    data = data.rename(columns={'cover.url' : 'cover', 'cover.id' : 'image'})
    
    # Obtencion de los generos
    
    print("Obtencion de los generos")
    
    genres = data["genres"]
    gen = []
    for g in genres:
       if str(g) != 'nan':
            aux = []
            for ge in g:
                aux.append(ge["name"])
            gen.append(aux)
       else:
           gen.append(g)
    data["genres"] = gen
    
    # Obtencion de los websites
    
    print("Obtencion de las Websites")
    
    websites = data["websites"]
    website = []
    for web in websites:
       if str(web) != 'nan':
            aux = []
            for w in web:
                aux.append(w["url"])
            website.append(aux)
       else:
           website.append(g)
    data["websites"] = website
    
    # Obtencion de las plataformas
    
    print("Obtencion de las plataformas")
    
    platforms = data["platforms"]
    plat = []
    for pla in platforms:
       if str(pla) != 'nan':
            aux = []
            for p in pla:
                aux.append(p["name"])
            plat.append(aux)
       else:
           plat.append(pla)
    data["platforms"] = plat
    
    # Obtencion de las compañias
    
    print("Obtencion de las compañias")
    
    companies = data["involved_companies"]
    compa = []
    for com in companies:
       if str(com) != 'nan':
            aux = []
            for c in com:
                aux.append(c["company"]["name"])
            compa.append(aux)
       else:
           compa.append(com)
    data["involved_companies"] = compa
    
    # Obtencion de los juegos similares
    
    print("Obtencion de los juegos similares")
    
    similar_games = data["similar_games"]
    similarG = []
    for simil in similar_games:
       if str(simil) != 'nan':
            aux = []
            for s in simil:
                aux.append(s["name"])
            similarG.append(aux)
       else:
           similarG.append(simil)
    data["similar_games"] = similarG
    
    # Obtencion de las screenshots
    
    print("Obtencion de las screenshots")
    
    screenshot = data["screenshots"]
    screen = []
    for scre in screenshot:
       if str(scre) != 'nan':
            aux = []
            for sc in scre:
                a = sc["url"].replace('t_thumb', 't_screenshot_big_2x')
                aux.append(a)
            screen.append(aux)
       else:
           screen.append(scre)
    data["screenshots"] = screen
    
    # Obtencion de las portadas
    
    print("Obtencion de las portadas")
    
    covers = data["cover"]
    cov = []
    for co in covers:
        if str(co) != 'nan':
            a = co.replace('t_thumb', 't_cover_big')
            cov.append(a)
        else:
            cov.append(co)
    data["image"] = cov
    
    # Obtencion de las fechas
    
    #print("Obtencion de las fechas")
    
    #date = data["first_release_date"]
    #date2 = []
    #for d in date:
    #    if str(d) != 'nan':
    #        dt = datetime.fromtimestamp(d).date()
    #        dat = datetime.strftime(dt, "%d/%m/%Y")
    #        date2.append(dat)
    #    else:
    #        date2.append(d)
    
    #data["first_release_date"] = date2
    
    if n == 500:
        data1 = data
    elif n == 1000:
        data2 = data
    elif n == 1500:
        data3 = data
    elif n == 2000:
        data4 = data
    elif n == 2500:
        data5 = data
    elif n == 3000:
        data6 = data
    elif n == 3500:
        data7 = data
    elif n == 4000:
        data8 = data
    elif n == 4500:
        data9 = data
    elif n == 5000:
        data10 = data
    elif n == 5500:
        data11 = data
    elif n == 6000:
        data12 = data
    elif n == 6500:
        data13 = data
    elif n == 7000:
        data14 = data
    elif n == 7500:
        data15 = data
    elif n == 8000:
        data16 = data
    else: data17 = data
    
dataBase = pd.concat([data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13, data14, data15, data16, data17])

dataBase.to_json("games.json", orient='index')

