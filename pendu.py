#coding:utf-8

#######################################
###### Déclaration des imports ########
#######################################

from functions import *


#########################################
# Déclaration des variables pour le jeu #
#########################################
game_on = True
is_secret_word_discovered = False
testedLetter = []
secret_word = ""
word_to_find = ""


#########################################
######### Déroulement du jeu ############
#########################################

while game_on:
    secret_word, hits = importData()
    print("{},{}".format(secret_word, hits))
    welcome()
    player_name = playerName()
    sayHello(player_name)
    print("Voici le mot a trouver : ", word_to_display(secret_word, ""))
    # word_to_find = secret_word
    while not is_secret_word_discovered and word_to_find != secret_word:
        # word_to_find = secret_word
        my_letter = userLetter().lower()
        my_good_letter = isGoodLetter(secret_word, my_letter)
        letterOk = isLetterAlreayUsed(my_letter)
        if letterOk:
            word_to_find = word_to_display(secret_word, my_good_letter)
            # word_to_find = displaySecretWord(secret_word)
            print("pendu mot a trouver: ", word_to_find)