# coding:utf-8

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

my_name = ""
letter_already_used = []
good_letter = []
testLetter = ""

secretWord = []
word = []
discovered_letter_in_word = []


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
    global my_name
    my_name = input("Quel est votre nom: ? ")
    if my_name == "":
        print("ah bon ?")
        return playerName()
    else:
        try:
            my_name = int(my_name)
            print('Vous devez rentrer une chaine de caractère')
            return playerName()

        except:
            return my_name


def importData():
    """ une fonction renvoyant toutes le données necessaire au jeu """
    wordToFind = choice(wordList)
    hits = avaible_hits
    return wordToFind, hits


def userLetter():
    """ une fonction renvoyant la lettre essayée par le joueur """
    my_letter = input("Veuillez saisir une lettre : ")
    if my_letter == "":
        print("Soyez serieux, vous voulez jouer ?")
        return userLetter()
    elif len(my_letter) > 1:
        print("Enfiiiin !! Une seule lettre à la fois, svp ?")
        return userLetter()
    try:
        my_letter = int(my_letter)
        print('Vous devez rentrer une chaine de caractère')
        return userLetter()
    except:
        return my_letter


def isLetterAlreayUsed(letter_to_test, hits, wdtotest):
    """ une fonction stockant les lettres essayées par le joueur """
    global letter_already_used

    if len(letter_already_used) == 0:
        if letter_to_test not in wdtotest:
            letter_already_used.append(letter_to_test)
            print("Désolé, la lettre ne se trouve pas dans le mot.")
            hits -= 1
            return hits, True
        else:
            letter_already_used.append(letter_to_test)
            print("Bravo. Une lettre de trouvée")
            return hits, True
    else:
        if letter_to_test in letter_already_used:
            print("Lettre déja recherchée")
            print("Voici votre liste de lettre : ", letter_already_used)
            hits -= 1
            return hits, False
        else:
            if letter_to_test not in wdtotest:
                letter_already_used.append(letter_to_test)
                hits -= 1
                print("Désolé, la lettre ne se trouve toujours pas dans le mot.")
                print("lettre déjà enregistrées : ", letter_already_used)
                return hits, True
            else:
                letter_already_used.append(letter_to_test)
                print("Bien. Une lettre de trouvée")
                print("lettre déjà enregistrées : ", letter_already_used)
                return hits, True


def isGoodLetter(wtfd, user_letter):
    global good_letter
    for letter in wtfd:
        if user_letter == letter:
            good_letter += user_letter
    return good_letter


def doIwin(sw, wtf):
    print("secret word: {}, mot a tester: {}".format(sw, wtf))
    if sw == wtf:
        print("gagne")
        return True



def word_to_display(finding_word, good_letter):
    word_to_display = ""
    for letter in finding_word:
        if letter in good_letter:
            word_to_display += letter
        else:
            word_to_display += "*"
    return word_to_display
