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
    
    
###################################################################"
### c'est ici que l'on execute notre programme
### en appelant les fonctions qu'on a définit plus haut
#**********************************#
#Script3:
#Tester l'extracteur de chanson de genius
#**********************************#
print "Exemple3: Extraire une chanson"
url_d_example = "http://genius.com/Ab-soul-terrorist-threats-lyrics"
html = download(url_d_example)
chanson = extract_chanson(html)
print chanson
write_csv("chansons.csv",chanson)
