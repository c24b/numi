#!/usr/bin/python 
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
    tag_link_list = soup.find_all("a")
    for element in tag_link_list:
        lien = element.get("href")
        liens.append(lien)
    return liens

###################################################################"
### c'est ici que l'on execute notre programme
### en appelant les fonctions qu'on a définit plus haut
#**********************************#
#Exemple 0:
#Extraire simplement les urls de la page
#**********************************#
print "Exemple0: Extraire simplement les urls de la page"

url_de_depart='http://www.bbc.com/news/science_and_environment'
liens0 = extract_links(url_de_depart)
print "Il y a %i urls sur la page %s" %(len(liens0), url_de_depart)
write_csv("test0.csv",liens0)
#Exemple1:
#Extraire simplement les urls d'une page de votre choix
#**********************************#
print "Exemple1: Extraire simplement les urls de la page de mon choix"
url_au_choix="#entrez ici l'url de votre choix"
liens0 = extract_links(url_au_choix)
write_csv("test1.csv",liens0)
print "Il y a %i urls sur la page %s" %(len(liens0), url_de_depart)


#Exemple 3:
#Extraire toutes les images des videos de la page BBC news
#**********************************#
print "Exemple2: Extraire simplement les urls de la page de mon choix"
html = download(url_de_depart)
images = extract_images(html)
print "Il y a %i images sur la page %s" %(len(images), url_de_depart)
write_csv("test2.csv",liens)

#Exemple 3
#Extraire les informations de la page http://genius.com/Ab-soul-terrorist-threats-lyrics
print "Exemple3: Extraire simplement les urls de la page de mon choix"
html = download("http://genius.com/Ab-soul-terrorist-threats-lyrics")
line = extract_data(html)
write_csv("test3.csv", line)


