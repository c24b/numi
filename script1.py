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

def extract_links(html):
    '''fonction qui extrait simplement les liens de la page'''
    
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
#Exemple 1:
#Extraire simplement les urls de la page de mon choix
#**********************************#
print "Exemple1: Extraire simplement les urls de la page de mon choix"
#a vous d'ajouter l'url de votre choix
url_de_depart= ""
html = download(url_de_depart)
liens0 = extract_links(html)
print "Il y a %i urls sur la page %s" %(len(liens0), url_de_depart)
write_csv("test1.csv",liens0)
