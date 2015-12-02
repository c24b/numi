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

def extract_images(html):
    '''extrait les videos depuis la page html de BBC NEWS SCIENCE'''
    colonne_videos = soup.find("div", {"id": "comp-candy-asset-munger"})    
    img_tags = colonne_videos.findall("img", {"class":"responsive-image__inner-for-label"})
    images = []
    for img in img_tags:
        image_sources = img.get("scr")
        images.append(image_sources)
    return images
    
def extract_titles(html):
    '''extrait les videos depuis la page html de BBC NEWS SCIENCE'''
    soup = BeautifulSoup(html)
    videos_titres = []
    colonne_videos = soup.find("div", {"id": "comp-candy-asset-munger"})    
    videos_items = colonne_videos.findall("div",{"class":"condor-item"})
    for v in videos_items:
        titre = v.h3.span.getText()
        videos_titres.append(titre)
    return data

    
###################################################################"
### c'est ici que l'on execute notre programme
### en appelant les fonctions qu'on a définit plus haut
#**********************************#
#Script2:
#Tester l'extracteur de rapgenious
#**********************************#
print "Exemple2: Extraire simplement une liste d'images"
html = download("http://www.bbc.com/news/science_and_environment")
images = extract_images(html)
print "Il y a %i images sur la page %s" %(len(images), url_de_depart)
write_csv("test2.csv",images)
