def get_jobs(ville, money, tech):
    '''for i in range(0, 3):
        if 'c#' in tech[x]:
            tech[x] = 'c%23'
        else if 'c++' in tech[x]:
            tech[x] = 'c%2B%2B'
        else: break'''
    url_test = 'https://stackoverflow.com/jobs/feed?l='+str(ville)+'&u=Km&d=20&s='+str(money)+'&c=EUR&tl='+str(tech)
    print(url_test)
    url = urllib.request.urlopen(url_test)
    return url
                                 
def get_meteo(ville):
    url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + ville +'&mode=json&units=metric&APPID=786b264284a5fd8ff885525aea085ba0')
    data = json.loads(url.read().decode('utf-8'))
    url.close()
    return data

def tree_creation(xml_file):
    parsed_xml = et.parse(xml_file).getroot()
    liste_caterory = []
    liste_link = []
    liste_name = []
    liste_title = []
    desc_list = []
    pubdate_list = []
    location_list = []
    global category, link, name, title, desc, pubdate, location
    
    for node in parsed_xml:
        for x in node.findall('item'):
            namespace = {'a10': 'http://www.w3.org/2005/Atom'}
            link = x.find('link')
            name = x.find('a10:author/a10:name', namespace)
            category = x.findall('category')
            title = x.find('title')
            desc = x.find('description')
            pubdate = x.find('pubDate')
            location = x.find('{http://stackoverflow.com/jobs/}location')
        for i in range(0, len(category)):  
            liste_caterory.append(get_noeud(category[i]))
        liste_link.append(get_noeud(link))
        liste_name.append(get_noeud(name))
        liste_title.append(get_noeud(title))
        desc_list.append(get_noeud(desc))
        pubdate_list.append(get_noeud(pubdate))
        location_list.append(get_noeud(location))
    print('Techs used: '+str(liste_caterory))
    print('Link: '+str(liste_link))
    print('Company'+str(liste_name))
    print('Title'+str(liste_title))
    print('Description'+str(desc_list))
    print('Published date'+str(pubdate_list))
    print('Location'+str(location_list))
    
    
def get_noeud(n):
    if(n is not None):
        return n.text
    
def data_meteo(data):
    n_data = dict(
        ville = data.get('name'),
        pays = data.get('sys').get('pays'),
        main_temp = data.get('main').get('temp'),
        main_press = data.get('main').get('pressure'),
        main_humidity = data.get('main').get('humidity'),
        wind = data.get('wind').get('speed'),
        clouds = data.get('clouds').get('all'),
        desc = data.get('weather')
    )
    return n_data

def get_weather_data(n_data):

    x= format(n_data['main_temp'])
    return x
                
def print_meteo(n_data):
    print('***********************************')
    print('Ville: {}'.format(n_data['ville']))
    print('Pays: {}'.format(n_data['pays']))
    print('Temperature actuelle: {}'.format(n_data['main_temp'])+'\xb0'+'C')
    print('Pression atmospherique: {}'.format(n_data['main_press'])+'hpa')
    print('Humidite: {}'.format(n_data['main_humidity'])+'%')
    print('Vitesse du vent: {}'.format(n_data['wind']))
    print('Nuage: {}'.format(n_data['clouds'])+'%')
    print('Description: {}'.format(n_data['desc']))
    x= format(n_data['main_temp'])
    return x
import urllib.request
import json, requests, xml
import xml.etree.ElementTree as et
import matplotlib.pyplot as plt

tab_techno_favorite = []
tab_ville_favorite = []
cities = ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', 'Strasbourg', 'Montpellier', 'Bordeaux', 'Rennes', 'Reims', 'Lille', 'Toulon', 'Grenoble', 'Angers', 'Dijon', 'Brest']
techno = ['javascript', 'sql', 'java', 'c#', 'python', 'php', 'c++', 'c', 'typescript', 'ruby', 'swift']
for cpt in range(0, 3):
    while True:
        tab_techno_favorite.append(input('Saisir votre language de programmation préféré: '))
        if tab_techno_favorite[cpt] not in techno:
            print("Ce langage de programmation n'est pas disponible, reessayez. ")
            continue
        else: break
            
for cpt2 in range(0, 2):
    while True:
        tab_ville_favorite.append(input('Saisir vos deux grandes ville préférées'))
        if tab_ville_favorite[cpt2] not in cities:
            print("Ville pas trouvé reeassayez")
            continue
        else:break
valeur_temperature=input("Saisir votre température idéal:")        
for cpt3 in cities:
    x= get_weather_data(data_meteo(get_meteo(cpt3)))
    if float(x) >float(valeur_temperature):
        print_meteo(data_meteo(get_meteo(cpt3)))
        plt.hist(x,normed=1)
        plt.show()
        for d in tab_techno_favorite:
            tree_creation(get_jobs(cpt3, 25000, d))