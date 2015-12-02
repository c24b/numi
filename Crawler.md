
# # Cours 5

## Introductions au techniques de crawl en Python

### Principes du crawl

Le crawl est une technique qui consiste à naviguer sur ou plusieurs site pour en récupérer les information 

C'est la technique qu'emploient les moteurs de recherche 
pour créer une base de données qui contient: 
les références au site 
et les mots clés qui correspondent à la recherche.

La base du crawl est de stocker les liens présents dans une page, de les télécharger au fur et à mesure et de stocker les informations intéressantes.

Le crawl permet donc de reconstituer une base de données en collectant les informations html et en les formattant pour les insérer dans une base.

### Les différents types de crawl
Il existe autant de crawler que de besoins spécifiques parfois et même souvent 
une même extraction peut procéder de différentes manières 
et donc avoir différentes implémentations.

Pour la collecte de données, on développe des crawlers spécifiques:  

* qui suit le parcours identifié sur le site
* a une profondeur fixée
* se concentre uniquement sur le site en question
* extrait les informations préalablement identifiées
* représente souvent les données sous forme tabulaire 

Par opposition le crawler web que développent les moteurs de recherche
et qu'on appelle ici *Spider*:

* suit toujours le même parcours 
* ne se concentre sur aucun site en particuler
* n'extrait que les informations qui sont communes à tous les sites web
* représente souvent les données sous forme de réseau ou de graphes

#### Le Spider web
##### Algorithme et implémentation
L'algorithme d'un spider simplifié fonctionne de la manière suivante:

A partir d'une url de départ:
        
        * télécharger la page
        * parser le contenu
        * extraire toutes les urls
        
Pour chaque url de la liste de départ:
    
    * refaire le travail
    * et ainsi de suite jusqu'à ce qu'il n'y ait plus d'url à traiter

Si on simule le fonctionnement d'un spider on écrirait un pseudo code comme celui ci
(Le pseudo code est une manière de définir les instructions simplifiées envoyées à la machine)


    tocrawl = []
    def crawl(url):
        html = download(url)
        page = parse(html)
        urls = extract_links(page)
        tocrawl.append(urls)
        return tocrawl
    
    starter_url = "www.example.com"
    tocrawl = crawl(starter_url)
    while len(tocrawl) != 0:
        for url in tocrawl:
            crawl(url)


Evidemment c'est un tout petit peu plus compliqué que ça...
Quelques exemples à la fin de ce cours

* Fonctionnement du Spider de Google
* Fonctionnement de Hyphe
* Fonctionnement de Crawtext
* Reprendre le fonctionnement des crawlers en ligne: détailer leur algorithme

##### Représentation des données

Les données du spider permettent de constituer des réseaux et des graphes en fonctions des informations collectées.
Les réseaux constitués les plus simple constistent en graphes de co-citations
une url source etant reliée a plusieurs urls par le fait quelle les mentionnent sur la page 
on peut cartographier les sites qui se citent les uns les autres.


####   Le crawler de site
##### Algorithme et implémentation

L'algorithme d'un crawler de site simplifié fonctionne de la manière suivante:
Une fois le parcours sur le site et les informations identifiées, le robot aggrège les données 
cibles qu'il stocke dans une base de données ou un fichier final à plat.
La parcours varie en fonction de l'information auquel on souhaite accéder et la manière dont on veut interroger les données.

* Un exemple d'implémentation de crawl pour le site 
https://www.republique-numerique.fr/consultations/projet-de-loi-numerique/consultation/consultation

L'objectif étant de récupérer l'ensemble des arguments pour chaque article de loi
* Lister les urls de tous les participants
    Pour chaque participants:
    * extraire les arguments qui lui appartiennent

##### Représentation des données
Le crawl produit une base de données d'arguments reliés à un article de loi
Dans le cas d'un crawl sur un site particulier, il est capital de définir avant le crawl 
les données à extraire et les différentes étapes pour appliquer l'extraction à plusieurs pages

### TP: construction d'un crawler de site web

#### Extracteur d'une page web

Reprenons toutes les étapes d'extraction pour la page d'un site.
On va reprendre les bases à travers plusieurs exercices


##### Exercice 0: Extraire les liens d'une page web

Vous pouvez télécharger le [script complet d'exemple par ici](./script0.py)
ou copier coller dans votre éditeur le code à la suite
Il s'agit d'un script très simple dont il faut bien lire les instructions


La liste de toutes les urls de cette page de départ est stockées dans liens1
pour savoir combien d'url on a récupéré on peut appeler une fonction standard dans python
len(uneliste) qui a partir d'une liste en parametres donne le nombre d'élements présents dans la liste


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
    #Exemple 0:
    #Extraire simplement les urls de la page
    #**********************************#
    print "Exemple0: Extraire simplement les urls de la page"
    
    url_de_depart='http://www.bbc.com/news/science_and_environment'
    html = download(url_de_depart)
    liens0 = extract_links(html)
    print "Il y a %i urls sur la page %s" %(len(liens0), url_de_depart)
    write_csv("test0.csv",liens0)

    Exemple0: Extraire simplement les urls de la page
    Il y a 247 urls sur la page http://www.bbc.com/news/science_and_environment


###### Exercice 1: Choississez une page
reprenez le script0.py et enregistrez le sous script1.py

Changez maintenant la partie ou l'on fat tourner le code
en changeant l'url_de_depart par l'url de votre choix
en suivant l'exemple ci dessous on en téléchargeant le [code par ici](./script1.py)
et en le modifiant un peu


    ###################################################################"
    ### c'est ici que l'on execute notre programme
    ### en appelant les fonctions qu'on a définit plus haut
    #**********************************#
    #Exemple 1:
    #Extraire simplement les urls de la page de mon choix
    #**********************************#
    print "Exemple1: Extraire simplement les urls de la page de mon choix"
    
    url= "http://www.opentechschool.org/"
    html = download(url)
    liens0 = extract_links(html)
    print "Il y a %i urls sur la page %s" %(len(liens0), url)
    write_csv("test1.csv",liens0)


Bon jusque là c'était facile, 
on vérifie juste que vous suivez!


On va maintenant remontrer quelques methodes pour extraire des contenus




###### Exercice 2: Extraire les données d'une seule page de chanson
Normalement vous avez déjà réussi à faire ce travail la semaine dernière ,
il s'agit simplement ici de completer la fonction extract_chanson
en ajoutant les méthodes pour extraire le titre, l'auteur, le texte et les tags d'une page de chanson
a partir de BeautifulSoup.

Pour avoir le détail du fonctionnement de BeautifulSoup, 
je vous donne deux exemples détaillés
des methodes find et find_all et de co
mment récupérer des données internes à la balise 
(par exemple href ou scr):
* [exemple1: script1.py](../script1.py)
* [exemple2: script2.py](../script2.py)

Maintenant que vous savez et avez réussi à extraire ce dont nous avions besoin
vous pouvez ajouter votre extraction dans la fonction extract_chanson()/
Le code complet à completer est téléchargeable aussi par [ici](../script3.py)
Sinon vous pouvez copiez coller la cellule suivante:




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
    
    
    def extract_chanson(html):
        '''ici la fonction qui permet d'extraire 
        le texte de la chanson 
        le titre
        les tags 
        l'auteur
        en utilisant les fonctions de Beautiful Soup
        '''
        soup = BeautifulSoup(html)    
        texte = ""
        titre = ""
        tags = ""
        auteur = ""
        return [titre, texte, tags, auteur]

Si vous le testez là tel quel en ayant copié collé 
et juste en ayant ajouter les information: il ne se passera rien 
Nous avons juste importé des modules et défini des fonctions il faut maintenant les appeler comme suit dans l'exemple



    print "Exemple3: La chanson de mon choix:"
    html = download("http://genius.com/Ab-soul-terrorist-threats-lyrics")
    line = extract_chanson(html)
    print line
    write_csv("test3.csv", line)

    Exemple3: La chanson de mon choix:
    ['', '', '***', '']


### Crawler de site: implémentation
Maintenant que vous avez un extracteur pour une chanson il est très facile de coder un extracteur pour toutes les chansons.
Il faut avant tout définir le parcours du crawl.

Vous allez fermer vos ordinateurs pour un moment et je vous montrer l'exemple

Vous allez détailler les étapes à la main en suivant mon exemple mais seulement APRES que j'ai fait le travail sur ce site.

Je cherche à extraire tous les arguments du site https://www.republique-numerique.fr/consultations/projet-de-loi-numerique/consultation/consultation pour chaque article

Etant donné qu'il est très difficile de récupérer les articles et les arguments
j'ai choisi d'attaquer par le profil des participants ceci constitue mon choix.
Et voici mon détail des étapes

1. J'ai défini une fonction qui a partir d'une page de profil

qui extrait les informations suivantes
[auteur, date, argument, lien_article]

2. J'ai defini une fonction qui a partir de la page des participants
qui extrait les url d'un profil

3. J'ai defini une fonction qui crée la liste de chaque page où sont listé les participants
qui génére une liste de page à extraire

4. J'ai maintenant les élements pour présenter mon algorithme en pseudo code


    liste_pages_profiles = lister_pages_participants()
    for page in liste_pages_profiles:
        liste_profil = extract_url_profile(page)
        for profile_url in liste_profil:
            for arguments in extract_profile(profile_url):
                csv_writer("arguments.csv", arguments)

Maintenant le détail de l'implémentation sans les véritables valeurs de BeautifulSoup (pour aller plus vite)


    
    def extract_profile(url):
        infos = []
        html = download(url)
        soup = BeautifulSoup(html)
        auteur = soup.find("div", {"class":auteur})
        auteur_url = url
        arguments = soup.findall("div", {"class": "arguments"})
        for argument in arguments:
            date = argument.find("div", {"class":"date"})
            article = argument.find("a")
            lien_article = article.get("href")
            text = argument.find("p").text
            infos.append([auteur, date, texte, lien_article])

Je suis donc déjà capable d'extraire une liste d'argument pour un utilisateur
en prenant exemple sur le profile suivant: https://www.republique-numerique.fr/profile/jeannevarasco



    url = "https://www.republique-numerique.fr/profile/jeannevarasco"
    arguments = extract_profile(url)
    for a in arguments:
        write_csv("arguments.csv", a)

Mais comment récupérer tous les pages de profile?

Tous les participants sont listés à une meme adresse de la page 1 à la page 1334

Je vais donc définir une fonction qui extrait l'url du profile du participants depuis une page d'exemple
https://www.republique-numerique.fr/projects/projet-de-loi-numerique/participants/2

et qui me donne les urls de profile présents sur cette page



    def extract_participants_url(url):
        participants = []
        html = download(url)
        soup = BeautifulSoup(html)
        for p in soup.find_all("div"):
            url = ""
            participants.append(url)
        return participants

J'ai récupéré maintenant pour une page d'exemple les 16 urls de profils

Je peux donc déjà extraire de ces 16 urls chaque profil.


    url = "https://www.republique-numerique.fr/projects/projet-de-loi-numerique/participants/2"
    list_participants = extract_participants_url(url)
    for profile in list_participants:
        arguments = extract_profile(profile)
        for a in arguments:
            write_csv("arguments.csv", a)

Il me faut donc maintenant tourner virtuellement les pages du site

Rien de plus simple les pages sont numérotées!


Je vais donc générer une liste de page
structurées comme suit:
`url = "https://www.republique-numerique.fr/projects/projet-de-loi-numerique/participants/"+"1"`

etc... 

jusqu'à 1334
dans une petite fonction qui s'appelle liste_pages_profiles()



    def liste_pages_profiles():
        pages = []
        url = "https://www.republique-numerique.fr/projects/projet-de-loi-numerique/participants/"
        for page_nb in range(1, 1335):
            page_url = url+str(page_nb)
            pages.append(url)
        return pages

A vous de jouer avec genius....

Lister le parcours et les extractions à chaque étape

Puis on le codera ensemble...

C'est parti!!!!

