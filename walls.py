import pygame
#Classe du Mur
class Mur(object):
    #On définit la position à partir du quel on vas affiché nos murs et on ajoute chaque mur à notre liste de murs
    def __init__(self,murs, pos):
        murs.append(self)
        self.walls = pygame.Rect(pos[0], pos[1], 16, 16)