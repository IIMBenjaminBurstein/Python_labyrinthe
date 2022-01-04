# Import de pygame et du modules sys permetant d'interagir avec l'interpreter
import sys
import pygame
from pygame import key
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP

class Player(object):
    #initilisation d'un rectangle représentant le joueur
    def __init__(self):
        self.player = pygame.Rect(16, 16, 16, 16)
 
    #focntion de mouvement du joueur
    def move(self,murs, directionX, directionY):
        #si l'axe x est modifié on modifie sa position avec la valeur recu 
        if directionX != 0:
            self.player.x += directionX
        #si l'axe y est modifié on modifie sa position avec la valeur recu 
        if directionY != 0:
            self.player.y += directionY
       
       #Pour chaque mur dans le tableau murs on regarde s'il ya une colission entre le mur et le joueur grace à la fonction colliderect
       #En fonction de la direction du joueur on définit la valeur de l'axe du joueur égale à l'opposé du mur
        for mur in murs:
            if self.player.colliderect(mur.walls):
                if directionX > 0:
                    self.player.right = mur.walls.left
                if directionX < 0: 
                    self.player.left = mur.walls.right
                if directionY > 0: 
                    self.player.bottom = mur.walls.top
                if directionY < 0: 
                    self.player.top = mur.walls.bottom