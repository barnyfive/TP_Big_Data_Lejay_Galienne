def get_noeud(n):
    if(n is not None):
        return n.text
    
def weather_data(data):
    tab_data = dict(
        city = data.get('name'),
        country = data.get('sys').get('country'),
        main_temp = data.get('main').get('temp'),
        main_press = data.get('main').get('pressure'),
        main_humidity = data.get('main').get('humidity'),
        wind = data.get('wind').get('speed'),
        clouds = data.get('clouds').get('all'),
        desc = data.get('weather')
    )
    return tab_data

                
def print_weather_data(tab_data):
    print('***********************************')
    print('Ville: {}'.format(tab_data['city']))
    print('Pays: {}'.format(tab_data['country']))
    print('Temperature actuelle: {}'.format(tab_data['main_temp'])+'\xb0'+'C')
    print('Pression atmospherique: {}'.format(tab_data['main_press'])+'hpa')
    print('Humidite: {}'.format(tab_data['main_humidity'])+'%')
    print('Vitesse du vent: {}'.format(tab_data['wind']))
    print('Nuage: {}'.format(tab_data['clouds'])+'%')
    print('Description: {}'.format(tab_data['desc']))
    
def tree_creation(xml_file):
    parsed_xml = et.parse(xml_file).getroot()
    desc_list = []
    pubdate_list = []
    liste_location= []
    liste_category = []
    liste_link = []
    liste_name = []
    liste_title = []
    global category, link, name, title, desc, pubdate, location
    
    for noeud in parsed_xml:
        for cpt in noeud.findall('item'):
            namespace = {'a10': 'http://www.w3.org/2005/Atom'}
            link = cpt.find('link')
            name = cpt.find('a10:author/a10:name', namespace)
            category = cpt.findall('category')
            title = cpt.find('title')
            desc = cpt.find('description')
            pubdate = cpt.find('pubDate')
            location = cpt.find('{http://stackoverflow.com/jobs/}location')
        for i in range(0, len(category)):  
            liste_category.append(get_noeud(category[i]))
        liste_link.append(get_noeud(link))
        liste_name.append(get_noeud(name))
        liste_title.append(get_noeud(title))
        desc_list.append(get_noeud(desc))
        pubdate_list.append(get_noeud(pubdate))
        liste_location.append(get_noeud(location))
    print('Techs used: '+str(liste_category))
    print('Link: '+str(liste_link))
    print('Company'+str(liste_name))
    print('Title'+str(liste_title))
    print('Description'+str(desc_list))
    print('Published date'+str(pubdate_list))
    print('Location'+str(liste_location))

def get_jobs(city, money, tech):
    
    url_test = 'https://stackoverflow.com/jobs/feed?l='+str(city)+'&u=Km&d=20&s='+str(money)+'&c=EUR&tl='+str(tech)
    print(url_test)
    url = urllib.request.urlopen(url_test)
    return url
                                 
def get_meteo(city):
    url = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&mode=json&units=metric&APPID=786b264284a5fd8ff885525aea085ba0')
    data = json.loads(url.read().decode('utf-8'))
    url.close()
    return data

    
import urllib.request
import json, requests, xml
import xml.etree.ElementTree as et


ville = 'Marseille', 'Lyon',['Paris', 'Nice', 'Toulouse', 'Nantes', 'Strasbourg', 'Montpellier', 'Brest', 'Reims', 'Lille', 'Toulon', 'Dijon', 'Angers', 'Grenoble', 'Bordeaux']
tab_technologie = ['javascript', 'sql', 'java', 'c#', 'python', 'php', 'c++', 'c', 'typescript', 'ruby', 'swift']
tab_techno_favorite = []
for cpt in range(0, 3):
    while True:
        tab_techno_favorite.append(input('Saisir votre language prefere parmi ceux listes: '))
        if tab_techno_favorite[cpt] not in tab_technologie:
            print("Ce langage de programmation n'est pas disponible, reessayez. ")
            continue
        else: break
for c in ville:
    print_weather_data(weather_data(get_meteo(c)))
    for d in tab_techno_favorite:
        tree_creation(get_jobs(c, 25000, d))