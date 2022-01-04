# Import de pygame et du modules sys permetant d'interagir avec l'interpreter
import sys
import random
import pygame
from Player import Player
from walls import Mur
#init de l'écran et de sa taille
pygame.init()
pygame.display.set_caption('Help rabit to find his carott')
ecran = pygame.display.set_mode((1205, 365))

#création d'un objet clock pour gérer la vitesse de déplacement du joueur
clock = pygame.time.Clock()
murs = []

Player = Player()
 #Layout du labyrinthe # = murs, F = finish
lab = [
    "############################################################",
    "#              ##                 ##                       #",
    "#              ##                 ##           ### ###  # ##",
    "#   ###        #############  ##  ## #  ##### #######  #####",
    "#   #           #                  #               ###     #",
    "# ###      ###  ################## ##########  #### #      #",
    "#   #     # #                        #   #          ###    #",
    "#      ############################### ############  # ## ##",
    "#   ## ##    ##############            #             ###  ##",
    "#     #         #            #  ###################    #####",
    "###   ## ##### ##     #  #   #               #     #      ##",
    "# #         #  #             #    #      #   #    ##  ##   #",
    "# #   ###   #      ####### #### ########### ########     ###",
    "#     #        #   #    ##     ##   ##      ##### ####    ##",
    "#     #        #        ## ##       ##           ###    # ##",
    "#     #        #   #       #  #      ##    ### ###    ### ##",
    "#     #        #   #   ##  ##       ###             ###   ##",
    "############################################################",
]
randRow = random.randrange(0, len(lab)-1, 1);
randFinish = random.randrange(0, len(lab[randRow])-1, 1);
finishRow = lab[randRow][:randFinish] + 'F' + lab[randRow][randFinish+1:]
lab[randRow] = finishRow
#init de la position à 0
x = y = 0
#On parse le layout
#Pour chaque ligne
for row in lab: 
    #Pour chaque colone (case de la ligne en cour)
    for col in row:
        # S'il y a un # on créer un mur à sa position
        if col == "#":
            Mur(murs,(x, y))
        # SI c'ets un f on créer un rectangle dans la variable de fin
        if col == "F":
            finish = pygame.Rect(x, y, 20, 20)
        # On incrémente la position de l'axe x de 16 (soit la largeur d'un possible mur)   
        x += 20
    y += 20
    x = 0
loop = True
while loop: 
    #Vitesse du joueur
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            #Si on appuie sur echap on ferme le jeu
            if event.key == pygame.K_ESCAPE:
                loop = False
        #Si on appuie sur la croix on ferme le jeu
        if event.type == pygame.QUIT:
            loop= False
            
    #Si on presse (reste appuyé) sur une des flèches on bouge le rectangle       
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        Player.move(murs, -1.5, 0)
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        Player.move(murs,1.5, 0)
    if  pygame.key.get_pressed()[pygame.K_UP]:
        Player.move(murs,0, -1.5)
    if  pygame.key.get_pressed()[pygame.K_DOWN]:
        Player.move(murs,0, 1.5)
 
    #Si le joueur rentre en colision avec le rectangle gagnant on ferme le jeu
    if Player.player.colliderect(finish):
        pygame.quit()
        sys.exit()
    ecran.fill((0, 0, 0))
    #Pour chaque mur on rend le rectangle de couleur blanche
    for mur in murs:
        pygame.draw.rect(ecran, (255, 255, 255), mur.walls)
    #Le rectangle de finish prend la couleur green
    pygame.draw.rect(ecran, (0, 255, 0), finish)
    #Le rectangle du joueur prend la couleur jaune
    pygame.draw.rect(ecran, (255, 200, 0), Player.player)
    pygame.display.flip()
pygame.display.update() 
pygame.quit()
