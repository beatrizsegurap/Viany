import requests
import json
from bs4 import BeautifulSoup

def Web_scrapping_sky(origen,fi,destino,ff):
    Ciudades=dict(ANF='ANTOFAGASTA',
                  ARI='ARICA',
                  BBA='BALMACEDA',
                  CJC='CALAMA',
                  MGHC='CASTRO CHILOE',
                  CCP='CONCEPCION',
                  CPO='COPIAPO',
                  IQQ='IQUIQUE',
                  LSC='LA SERENA',
                  ZOS='OSORNO',
                  ZPC='PUCON',
                  PMC='PUERTO MONTT',
                  PNT='PUERTO NATALES',
                  PUQ='PUNTA ARENAS',
                  IPC='RAPA NUI',
                  SCL='SANTIAGO DE CHILE'
                  )

    ciudad_origen=origen.upper()
    ciudad_destino=destino.upper()

    for ciudad in Ciudades:
        if(Ciudades[ciudad]==ciudad_origen):
            origen=ciudad
        if(Ciudades[ciudad]==ciudad_destino):
            destino=ciudad
    obtener_script = requests.get("https://www.skyairline.com/").text

    script = obtener_script.split("/js/app")[1]
    script = "app" + script.split('"')[0]
    #print(script)

    codigo_unico = requests.get("https://www.skyairline.com/js/" + script).text

    codigo_unico = codigo_unico.split('VUE_APP_PRICING_FARES_SUBSCRIPTION_KEY:"')[1]

    codigo_unico = codigo_unico.split('"')[0]


    burp0_url = "https://api.skyairline.com:443/shopping-fares/v2/fares-shop"
    burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Market": "cl", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36", "Ocp-Apim-Subscription-Key": codigo_unico, "Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://www.skyairline.com", "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://www.skyairline.com/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}

    burp0_json={"currency": "CLP", "filters": None, "passengers": {"adults": 1, "babies": 0, "children": 0, "pets": 0}, "segments": [{"departureDate": fi, "destination": destino, "origin": origen}, {"departureDate": ff, "destination": destino, "origin": origen}]}
    peticion_final = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)


    jsonSky = json.loads(peticion_final.text)
    listsegments = jsonSky['segments']



    print("-----------------")
    print("\n")
    for name_place in listsegments:
        ciudad_origen=name_place["origin"]
        ciudad_destino=name_place["destination"]
        numero_vuelo=name_place['flightNumber']
        fecha_y_hora_origen=name_place['departureDate']
        fecha_origen=fecha_y_hora_origen.split("T")[0]
        hora_origen=fecha_y_hora_origen.split("T")[1]
        fecha_y_hora_destino=name_place['arrivalDate']
        fecha_destino=fecha_y_hora_destino.split("T")[0]
        hora_destino=fecha_y_hora_destino.split("T")[1]
        tarifa=name_place["fares"][0]["fareAmount"]


#----------------#
#main"

fi = "2022-12-17"
ff = "2022-12-26"
origen = 'Arica'
destino = "Santiago de chile"
Web_scrapping_sky(origen,fi,destino,ff)
