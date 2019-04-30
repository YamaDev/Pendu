#coding:utf-8

#######################################
###### Déclaration des imports ########
#######################################

from functions import *


#########################################
# Déclaration des variables pour le jeu #
#########################################
game_on = True


#########################################
######### Déroulement du jeu ############
#########################################

while game_on:
    word_to_find, hits = importData()
    print("{},{}".format(word_to_find, hits))
    welcome()
    player_name = playerName()
    sayHello(player_name)