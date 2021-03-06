# coding:utf-8

#ici les modules
import requests
import csv
from bs4 import BeautifulSoup

BeautifulSoup("html.parser")

#ici les fonctions
def download(url):
    '''fonction qui télécharge une page a partir d'une url et retourne le html sous forme de texte'''
    reponse = requests.get(url)
    if reponse.status_code == 200:
        return reponse.text

def write_csv(filename, line):
    '''fonction qui écrit des données sous forme de listes dans un fichier []'''
    with open(filename, 'a') as csvfile: 
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(line)
    return

def extract_links(url):
    '''fonction qui extrait simplement les liens de la page'''
    print url
    html = download(url)
    liens = []
    soup = BeautifulSoup(html)
    tag_link_list = soup.find_all("a", {"class":"song_name"})
    for element in tag_link_list:
        lien = element.get("href")
        liens.append(lien)
    return liens


def extract_chanson(html):
    '''ici la fonction qui permet d'extraire 
    le texte de la chanson 
    le titre
    les tags 
    l'auteur
    en utilisant les fonctions de Beautiful Soup
    '''
    soup = BeautifulSoup(html)    
    texte = soup.find("div", {"class":"lyrics"}).text
    titre = soup.find("span", {"class":"text_title"}).text
    tags = soup.find("p", {"class":"tags song_meta_item"}).text
    auteur = soup.find("span", {"class":"text_artist"}).text
    return [titre.encode("utf-8"), texte.encode("utf-8"), tags.encode("utf-8"), auteur.encode("utf-8")]

def extract_chansons_list(html):
    soup = BeautifulSoup(html)    
    #section = soup.find("section", {"class":"all_songs"})
    liens_bruts = soup.find_all("a", {"class": "song_name"})
    liens = []
    for lien in liens_bruts:
        print lien
        url = lien.get("href")
        liens.append(url)
    return liens

def extract_artistes_list(html):
    ''' parse la page d'index'''
    soup = BeautifulSoup(html)
    liens_bruts = soup.find_all("a",{"class":"artists_index_list-artist_name"})
    liens = []
    for lien in liens_bruts:
        url = lien.get("href")
        liens.append(url)
    return liens
    
###ici on appelle 
print "Exemple4: L artiste de mon choix:"
#html = download("http://genius.com/Ab-soul-terrorist-threats-lyrics")
#url_artist = "http://genius.com/artists/Ab-soul"
url_index = "http://genius.com/artists-index/a"
html = download(url_index)
listes_artist = extract_artistes_list(html)
for artist in listes_artist:    
    html = download(artist)
    liste_chansons = extract_chansons_list(html)
    for chanson in liste_chansons:
        #print chanson
        html = download(chanson)
        chanson = extract_chanson(html)
        print chanson
        write_csv("chansons_A.csv", chanson)
    
