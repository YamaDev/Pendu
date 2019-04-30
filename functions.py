#coding:utf-8

#######################################
###### Déclaration des imports ########
#######################################


from time import sleep
from donnees import *
from random import choice
import pickle


#########################################
# Déclaration des variables pour le jeu #
#########################################

myName = ""

#########################################
# Déclaration des fonctions pour le jeu #
#########################################

def narrationPause(timepause):
    """ une fonction permettant de faire des pauses pendant la narration du jeu """
    sleep(timepause)

def welcome():
    """ une fonction permettant d'annoncer le jeu et souhaiter la bienvenue """
    print("Bienvenue au jeu du Pendu")
    narrationPause(1)

def sayHello(gamer):
    """ une fonction permettant de dire bonjour au joueur """
    print("Bonjour {}, nous allons jouer ensemble".format(gamer))
    narrationPause(1)

def playerName():
    """ une fonction renvoyant  le nom du joueur """
    global myName
    myName = input("Quel est votre nom: ? ")
    if myName == "":
        print("ah bon ?")
        return playerName()
    else:
        try:
            myName = int(myName)
            print('Vous devez rentrer une chaine de caractère')
            return playerName()

        except:
            return myName


def importData():
    wordToFind  = choice(wordList)
    hits        = avaible_hits
    # print("le mot a trouver est {}: ".format(wordToFind))
    # print("Il vous reste {} coups a jouer : ".format(hits))
    return wordToFind, hits
