'''This application was made using python 2.7 with pygame 1.9.1'''

import sys, pygame, random, os
from pygame.locals import *

'''Importing the graph module to help create random maps'''
import networkx as nx

'''Importing other .py files'''
from Menu import *
from gameStage import *             #gameStage contains all classes used in this game
from gameSettings import *

black = (0,0,0)
white = (255,255,255)
screen.fill(black)

stage = 0 #This works like a game state

mouseMove = False  #Detects when the user moves the mouse


#Colecting data of the players actions
pygame.font.init()
font = pygame.font.SysFont("Times New Roman",20)
pygame.key.set_repeat(400,25)

#Score system
score_zero = 0   #did an action without knowing what to do next
score_one = 1    #did an action and after did another action that was not correct
score_two = 2    #did an action and after did another action correctly
score_total = 0  #the sum of all scores obtained while playing the game

global dataArchive
celPadding = 20 #used when formatting the file
name = ""
nameCollector = "Digite o seu nome completo, idade e sexo "
def getName():
    global dataArchive
    save_path = ".\Data Archive"
    completeName = os.path.join(save_path, name+".txt")
    dataArchive = open(completeName, "w")
    dataArchive.write('{0} {1} {2} {3} {4}'.format("Objeto".ljust(celPadding), \
                                              "Posição do Objeto (X,Y)".ljust(celPadding+2), \
                                              "Tempo (s)".ljust(celPadding), \
                                              "Comando".ljust(celPadding), \
                                              "Pontuacao".rjust(celPadding)+'\n'+'\n'))

#This text appears before the game begins
def drawText():
    surface_name = font.render(name,True,white)
    surface_nameCollector = font.render(nameCollector,True,white)
    screen.blit(surface_name,(100,100))
    screen.blit(surface_nameCollector,(100,70))

'''Instantiating the objects'''
    #EnemyShips
enemyShipX, enemyShipY = 100, 50
bulletsX, bulletsY = enemyShipX, (enemyShipY+60)           #bullets shot by the left enemy ship
bullets2X, bullets2Y = enemyShipX+600, (enemyShipY+60)     #bullets shot by the right enemy ship
enemyShip = EnemyShip(enemyShipX,enemyShipY, 4, -1)        #left enemy ship
enemyShip2 = EnemyShip(enemyShipX+600,enemyShipY, -4, 1)   #right enemy ship
all_sprites_List.add(enemyShip, enemyShip2)             


    #Monsters
'''Monsters are used to protect the map painting from the bullets of enemyships'''
monsterX, monsterY = 700, 300                    
monster = Monster(100, monsterY, 0, 0)           
monster1 = Monster(200, monsterY, 1, 1)
monster2 = Monster(300, monsterY, 2, 2)
monster3 = Monster(400, monsterY, 3, 0)
monster4 = Monster(500, monsterY, 0, 1)
monster5 = Monster(600, monsterY, 1, 2)
monster6 = Monster(700, monsterY, 2, 0)
monster7 = Monster(100, monsterY-100, 3, 1)
monster8 = Monster(200, monsterY-100, 0, 2)
monster9 = Monster(300, monsterY-100, 1, 0)
monster10 = Monster(400, monsterY-100, 2, 1)
monster11 = Monster(500, monsterY-100, 3, 2)
monster12 = Monster(600, monsterY-100, 0, 0)
monster13 = Monster(700, monsterY-100, 1, 1)
monster14 = Monster(300, monsterY-200, 2, 2)
monster15 = Monster(400, monsterY-200, 3, 0)
monster16 = Monster(500, monsterY-200, 0, 1)

MonsterList.add(monster, monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9, \
                monster10, monster11, monster12, monster13, monster14, monster15, monster16)

all_sprites_List.add(monster, monster1, monster2, monster3, monster4, monster5, monster6, monster7, monster8, monster9, \
                     monster10, monster11, monster12, monster13, monster14, monster15, monster16)

    #MapParts
'''MapParts altogether represents the map that is going to be painted with colorPens.
   The best solution is painting with 4 colors
'''
map1X, map1Y = 270, 475                     
map1 = mapPart(map1X, map1Y, 4, 0)              
map2 = mapPart(map1X+23, map1Y-14, 4, 1)          
map3 = mapPart(map1X+31, map1Y+10, 4, 2)
map4 = mapPart(map1X+52, map1Y+18, 4, 3)
map5 = mapPart(map1X+48, map1Y-13, 4, 4)
map6 = mapPart(map1X+22, map1Y-54, 4, 5)
map7 = mapPart(map1X+80, map1Y+2, 4, 6)
map8 = mapPart(map1X+110, map1Y+6, 4, 7)
map9 = mapPart(map1X+44, map1Y-42, 4, 8)
map10 = mapPart(map1X+72, map1Y-27, 4, 9)
map11 = mapPart(map1X+74, map1Y-47, 4, 10)
map12 = mapPart(map1X+17, map1Y-74, 4, 11)
map13 = mapPart(map1X+55, map1Y-72, 4, 12)
map14 = mapPart(map1X+55, map1Y-92, 4, 13)
map15 = mapPart(map1X+87, map1Y-90, 4, 14)
map16 = mapPart(map1X+107, map1Y-75, 4, 15)
map17 = mapPart(map1X+105, map1Y-22, 4, 16)
map18 = mapPart(map1X+108, map1Y-40, 4, 17)
map19 = mapPart(map1X+140, map1Y-72, 4, 18)
map20 = mapPart(map1X+135, map1Y-20, 4, 19)
map21 = mapPart(map1X+125, map1Y-92, 4, 20)
map22 = mapPart(map1X+136, map1Y-47, 4, 21)
map23 = mapPart(map1X+163, map1Y-19, 4, 22)
map24 = mapPart(map1X+175, map1Y, 4, 23)
map25 = mapPart(map1X+205, map1Y, 4, 24)
map26 = mapPart(map1X+199, map1Y-25, 4, 25)

'''These lists are used to draw the mapParts to the screen'''
mapPartList.add(map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11, map12, map13, map14, map15, \
                map16, map17, map18, map19, map20, map21, map22, map23, map24, map25, map26)
all_sprites_List.add(map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11, map12, map13, map14, map15, \
                     map16, map17, map18, map19, map20, map21, map22, map23, map24, map25, map26)

'''We use a graph library to help detecting neighbors colors'''
states = [map1, map2, map3, map4, map5, map6, map7, map8, map9, map10, map11, map12, map13, map14, map15, map16, \
          map17, map18, map19, map20, map21, map22, map23, map24, map25, map26]
edges = [(map1,map2),(map1,map3), \
         (map2,map3),(map2,map5), \
         (map3,map4),(map3,map5), \
         (map7,map5),(map7,map4), \
         (map8,map7), \
         (map9,map6),(map9,map5),(map9,map7), \
         (map10,map9),(map10,map5),(map10,map7), \
         (map11,map9),(map11,map10), \
         (map12,map6), \
         (map13, map12),(map13,map6),(map13,map11), \
         (map14,map12),(map14,map13), \
         (map15,map14),(map15,map13), \
         (map16,map11),(map16,map15), \
         (map17,map10),(map17,map8), \
         (map18,map10),(map18,map17), \
         (map19,map16), \
         (map20, map17), \
         (map21, map15),(map21,map16),(map21,map19), \
         (map22,map18),(map22,map20), \
         (map23,map20),(map24,map23),(map25,map24),(map26,map25)]
mapGraph = nx.Graph()
mapGraph.add_nodes_from(states, name='', color=4, nNeighbors=0, nDifNeighbors=0, neighborsList=[])
mapGraph.add_edges_from(edges)

'''Giving name to the edges'''
mapGraph.node[map1]['name'] = 'map1'
mapGraph.node[map2]['name'] = 'map2'
mapGraph.node[map3]['name'] = 'map3'
mapGraph.node[map4]['name'] = 'map4'
mapGraph.node[map5]['name'] = 'map5'
mapGraph.node[map6]['name'] = 'map6'
mapGraph.node[map7]['name'] = 'map7'
mapGraph.node[map8]['name'] = 'map8'
mapGraph.node[map9]['name'] = 'map9'
mapGraph.node[map10]['name'] = 'map10'
mapGraph.node[map11]['name'] = 'map11'
mapGraph.node[map12]['name'] = 'map12'


totalNeighbors = 0    #totalNeighbors is responsible for telling if the player painted the map totally correct
                      #totally correct means that totalNeighbors equal the sum of all neighbors of all nodes
correctPainting = 0   #correctPainting is the sum of all neighbors of all nodes

'''Getting the number of neighbors for all nodes of the graph'''
for node in nx.nodes(mapGraph):
    mapGraph.node[node]['nNeighbors'] = len(mapGraph.neighbors(node))
    correctPainting += len(mapGraph.neighbors(node))
    mapGraph.node[node]['neighborsList'] = mapGraph.neighbors(node)
    #print mapGraph.node[node]['name'] , "number of neighbors: %d" %mapGraph.node[node]['nNeighbors']
    #print correctPainting

    #Spaceship
'''Spaceship collects the broken parts to recicle into monsters'''
spaceshipX, spaceshipY = 120, 400
spaceship = Spaceship(spaceshipX,spaceshipY)  
all_sprites_List.add(spaceship)

    #Claw
'''Claw is attached to the spaceship. Used to get get the broken parts that are orbiting'''
claw = Claw(spaceshipX, spaceshipY)           
clawList.add(claw)                            
all_sprites_List.add(claw)

    #ColorPens
clPenX, clPenY = 600, 515                   
clPen = colorPen(clPenX,clPenY, 0)
clPen2 = colorPen(clPenX+50,clPenY, 1)
clPen3 = colorPen(clPenX+100,clPenY, 2)
clPen4 = colorPen(clPenX+150,clPenY, 3)
colorPenList.add(clPen, clPen2, clPen3, clPen4)
all_sprites_List.add(clPen, clPen2, clPen3, clPen4)

    #Sun
sunX, sunY = 400,500
sun = Sun(sunX, sunY)
sunList.add(sun)
    #gameEnding timer
endTimer = 0


bulletHitMonsterList = []       #List containing the monsters that collides with bullets
penHitMapList = []              #List containing pens that collides with mapParts
penHitMonsterList = []          #List containing pens that collides with monsters
upRing_Hit_bkPartList = []      #List containing bkParts that collides with upRing
claw_Hit_bkPartList = []        #List containing bkParts that collides with claw

'''Time delay for shooting'''
clock = pygame.time.Clock()
tInitial, tFinal = 0, 0     #Time counter for the shoots of enemyShip
t2Initial, t2Final = 0, 0   #Time counter for the shoots of enemyShip2
delay = 1000                 #This sets the time delay for enemyShip
delay2 = 1500               #This sets the time delay for enemyShip2

running = True
while running:
    #Total time the game has been running
    gameTime = pygame.time.get_ticks()/1000
    
    game_milliseconds = clock.tick(FPS)         #milliseconds passed since last frame
    game_seconds = 1/float(game_milliseconds)   #seconds passsed since last frame
    
    for event in pygame.event.get():
        #Exit of the game----------------
        if event.type == pygame.QUIT:
            dataArchive.write("{0} {1} {2} {3}".format('Pontuação Total: ', \
                               "%d"%score_total+"pontos |", \
                               "Tempo Total: ", \
                               "%d"%gameTime+"segundos"+'\n'+'\n'))
            dataArchive.close()
            pygame.mixer.quit()
            running = False
        #--------------------------------
        
        '''Menu buttons logic'''
        if(event.type == KEYDOWN and stage == 0):
            if(event.key == K_ESCAPE):
                pygame.mixer.quit()
                running = False
            elif(event.key == K_BACKSPACE):
                if(len(name) > 0):
                    name = name[:-1]
            else:
                try: name += str(event.unicode)
                except: pass
        
        if (event.type == MOUSEBUTTONUP and stage == 0 and event.button == 1 and len(name)>3):
            if(quitButtonrect.collidepoint(pygame.mouse.get_pos())):
                pygame.mixer.quit()
                running = False
            elif(playButtonrect.collidepoint(pygame.mouse.get_pos())):
                getName()
                dataArchive.write("{0} {1} {2} {3} {4}".format('Botão Jogar'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(playButtonrect.x,playButtonrect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Clique".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_two+'\n'+'\n'))
                score_total += score_two
                stage = 1
                screen.fill(white)

        '''gameStage logic starts here'''
        if(event.type == MOUSEMOTION):
            mouseMove = True
        
        '''Drag and Drop logic for the pens part (1/2)'''
        if (event.type == MOUSEBUTTONUP and stage == 1 and event.button == 1):
            for clPen in colorPenList:
                if clPen.rect.collidepoint(pygame.mouse.get_pos()):
                    #print clPen.dragged
                    if(not(clPen.dragged)):
                        clPen.dragged = True
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Caneta Colorida'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(clPen.rect.x,clPen.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Arraste".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
                    elif(clPen.dragged):
                        clPen.dragged = False
                    if(not(clPen.clicked)):
                        clPen.clicked = True
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Caneta Colorida'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(clPen.rect.x,clPen.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Clique".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
                    elif(clPen.clicked):
                        clPen.clicked = False
                    #print clPen.clicked
        
        '''Drag and Drop logic for the monsters part (1/2)'''
        for monster in MonsterList:                    
            if (event.type == MOUSEBUTTONDOWN and event.button == 1 and stage == 1):
                if monster.rect.collidepoint(pygame.mouse.get_pos()):
                    monster.dragged = True
                    monster.released = False
                    dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Arraste".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
            
            elif(event.type == MOUSEBUTTONUP and event.button == 1 and stage == 1):
                monster.dragged = False
            if(event.type == MOUSEBUTTONUP and (mouseMove) and monster.rect.collidepoint(pygame.mouse.get_pos())):
                monster.dragged = False
                monster.released = True
                mouseGetSpeed = True
                if (mouseGetSpeed):
                    monster.mouseVel = pygame.mouse.get_rel()
                    mouseGetSpeed = False
                dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Lançado".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
                #print monster.released

        '''Drag and Drop logic for the broken parts part (1/2)'''
        for bkPart in brokenPartList:                    
            if (event.type == MOUSEBUTTONDOWN and event.button == 1 and stage == 1):
                if bkPart.rect.collidepoint(pygame.mouse.get_pos()):
                    bkPart.dragged = True
                    bkPart.released = False
                    dataArchive.write("{0} {1} {2} {3} {4}".format('Peça Quebrada'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(bkPart.rect.x,bkPart.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Arraste".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
                    
            elif(event.type == MOUSEBUTTONUP and event.button == 1 and stage == 1):
                bkPart.dragged = False
        
        '''Keyboard input to control the spaceship'''
        keys = pygame.key.get_pressed()

        '''claw grabbing'''
        if(keys[K_g] and stage == 1):
            claw.isHolding = True
            dataArchive.write("{0} {1} {2} {3} {4}".format('Garra da Nave'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(claw.rect.x,claw.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Coletar/Reciclar".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
        '''Spaceship movement'''
        if(keys[K_w] and stage == 1):
            spaceship.moveUp = True
            spaceship.moveDown = False
            dataArchive.write("{0} {1} {2} {3} {4}".format('Nave'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(spaceship.rect.x,spaceship.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Movimento Cima".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
        elif(keys[K_s] and stage == 1):
            spaceship.moveDown = True
            spaceship.moveUp = False
            dataArchive.write("{0} {1} {2} {3} {4}".format('Nave'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(spaceship.rect.x,spaceship.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Movimento Baixo".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
        elif(keys[K_a] and stage == 1):
            spaceship.moveLeft = True
            spaceship.moveRight = False
            dataArchive.write("{0} {1} {2} {3} {4}".format('Nave'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(spaceship.rect.x,spaceship.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Movimento Esquerda".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
        elif(keys[K_d] and stage == 1):
            spaceship.moveRight = True
            spaceship.moveLeft = False
            dataArchive.write("{0} {1} {2} {3} {4}".format('Nave'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(spaceship.rect.x,spaceship.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Movimento Direita".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
        else:
            spaceship.moveUp = False
            spaceship.moveDown = False
            spaceship.moveLeft = False
            spaceship.moveRight = False

    
    '''Drawings'''
    if(stage == 0):  #Menu
        screen.blit(background, (0,0))
        if(len(name) > 3):
            draw_quitButton()
            draw_playButton()
        drawText()
    if(stage == 1):  #gameStage
        screen.blit(background, (0,0))
        #print pygame.mouse.get_rel()

        '''Delay logic for the enemy ship shooting'''
        if(clock.get_time()%2 == 0):
            tInitial+=1
            tFinal+=1
            t2Initial+=1
            t2Final+=1

        '''Spaceship with it's claw movement'''
        spaceship.positionUpdate()
        claw.positionUpdate(spaceship.rect.x, spaceship.rect.y)
        
        '''Recicling logic'''
        if(len(claw.piecesCollected) > 2):
            monster = Monster(spaceship.rect.x+50, spaceship.rect.y-50, claw.colorsCollected[0], claw.formsCollected[0])
            MonsterList.add(monster)
            all_sprites_List.add(monster)
            spaceship.jumpFrame = True
            spaceship.animate()
            claw.piecesCollected = []
            claw.formsCollected = []
            claw.colorsCollected.pop(0)
            dataArchive.write("{0} {1} {2} {3} {4}".format('Nave'.ljust(celPadding), \
                                                       "%d, %d".ljust(celPadding)%(spaceship.rect.x,spaceship.rect.y), \
                                                       "%d".ljust(celPadding)%gameTime, \
                                                       "Monstro Reciclado".ljust(celPadding), \
                                                       "%d".rjust(celPadding)%score_zero+'\n'+'\n'))
            #print "full"
        
        '''Timer to instantiate a bullet'''
        if(tInitial > (delay/2)):
            '''Left enemyShip'''
            global colorNumber
            global formNumber
            colorNumber = random.randint(0,nColorMax)
            formNumber = random.randint(0,nFormMax) 
            bullet = Bullet(bulletsX,bulletsY-85, colorNumber, formNumber, enemyShip.updateAngle, False)
            bulletList.add(bullet)
            all_sprites_List.add(bullet)
            bullet.created = True
            bullet.right = False
            enemyShip.angleUpdate()
            tInitial = (delay-(delay+100))
            #print "created left bullet"
            #print bullet.form

        '''Timer to shoot the bullet'''
        if(tFinal > delay):
            for bullet in bulletList:
                if(not(bullet.right)):
                    if(bullet.created):
                        bullet.shot = True
                        tFinal = 0
                        #print "Left Bullet Shot:",bullet.shot

        '''Enable enemyShip animation'''
        if(tFinal > (delay - 30)):
            enemyShip.readyToAnimate = True
            for bullet in bulletList:
                if(not(bullet.right) and not(bullet.shot)):
                    bulletList.remove(bullet)
                    all_sprites_List.remove(bullet)
                    bullet = Bullet(bulletsX,bulletsY, colorNumber, formNumber, enemyShip.updateAngle, False)
                    bulletList.add(bullet)
                    all_sprites_List.add(bullet)
                    bullet.created = True
        
        '''Enable enemyShip2 animation'''
        if(t2Final > (delay2 - 30)):
            enemyShip2.readyToAnimate = True
            for bullet2 in bulletList:
                if((bullet2.right) and not(bullet2.shot)):
                    bulletList.remove(bullet2)
                    all_sprites_List.remove(bullet2)
                    bullet2 = Bullet(bullets2X,bullets2Y, colorNumber2, formNumber2, enemyShip2.updateAngle, True)
                    bulletList.add(bullet2)
                    all_sprites_List.add(bullet2)
                    bullet2.created = True

        if(enemyShip.readyToAnimate):
            enemyShip.animate()
        #print enemyShip.readyToAnimate
        
        if(enemyShip2.readyToAnimate):
            enemyShip2.animate()
        #print enemyShip2.readyToAnimate

        
        '''Timer to instantiate a bullet for enemyShip2'''
        if (t2Initial > (delay2/2)):
            '''Right enemyShip'''
            global colorNumber2
            global formNumber2
            colorNumber2 = random.randint(0,nColorMax)
            formNumber2 = random.randint(0,nFormMax) 
            bullet2 = Bullet(bullets2X,bullets2Y-85, colorNumber2, formNumber2, enemyShip2.updateAngle, True)
            bulletList.add(bullet2)
            all_sprites_List.add(bullet2) 
            bullet2.created = True
            enemyShip2.angleUpdate()
            t2Initial = (delay2-(delay2+150))
            #print "created right bullet"
            
        '''Timer to shoot the bullet for enemyShip2'''
        if(t2Final > delay2):
            for bullet2 in bulletList:
                if(bullet2.right):
                    if(bullet2.created):
                        bullet2.shot = True
                        t2Final = 0
                        #print "Right Bullet Shot:",bullet.shot
        
        '''Drag and Drop logic for the monsters part (2/2)'''
        for monster in MonsterList:
            if(monster.dragged):
                monster.positionUpdate()
            if(monster.released):
                monster.throw(monster.mouseVel)
            if((monster.rect.x < 0) and (monster.released)):
                monster.rect.x += 50
                monster.mouseVel = (0,0)
            elif((monster.rect.x > window_Width-40) and (monster.released)):
                monster.rect.x -= 50
                monster.mouseVel = (0,0)
            elif((monster.rect.y < 0) and (monster.released)):
                monster.rect.y += 50
                monster.mouseVel = (0,0)
            elif((monster.rect.y >(window_Height-40)) and (monster.released)):
                monster.rect.y -= 50
                monster.mouseVel = (0,0)

        '''Broken Parts movement'''
        for bkPart in brokenPartList:
            bkPart.orbitUpdate()
            bkPart.timer += 1
            if(bkPart.timer > 4):
                bkPart.floatingUpdate()
                bkPart.timer = 0
            if(bkPart.rect.y > (window_Height-200)):
                bkPart.orbiting = True
            '''Drag and Drop logic for the broken parts part (2/2)'''
            if((bkPart.dragged) and (not(bkPart.orbiting))):
                bkPart.mouseUpdate()
                
            
        '''Detects if the mouse is not moving'''
        if(pygame.mouse.get_rel()[0] == 0 and pygame.mouse.get_rel()[1] == 0):
            mouseMove = False
        
        
#All collisions-------------------------------------------------------------------------------     
        '''Drag and Drop logic for the pens part (2/2)'''
        for clPen in colorPenList:
            if(clPen.dragged):
                clPen.positionUpdate()
                #stage = 2
            if(not(clPen.dragged)):
                penHitMapList = pygame.sprite.spritecollide(clPen, mapPartList, False)
                penHitMonsterList = pygame.sprite.spritecollide(clPen, MonsterList, clPen.notInitialPosition)
                '''Coloring mapParts with pen'''
                for mapPart in penHitMapList:
                    if(mapPart.rect.collidepoint(pygame.mouse.get_pos())):
                        mapPart.updateImage(clPen.color)
                        mapGraph.node[mapPart]['color'] = clPen.color
                        addToList = True
                        for neighbor in mapGraph.node[mapPart]['neighborsList']:
                            if(mapGraph.node[neighbor]['color'] != mapGraph.node[mapPart]['color'] and addToList and \
                               mapGraph.node[neighbor]['nDifNeighbors'] < len(mapGraph.node[neighbor]['neighborsList'])):
                                #print mapGraph.node[neighbor]['name']
                                mapGraph.node[neighbor]['nDifNeighbors'] += 1
                                totalNeighbors += 1
                                dataArchive.write("{0} {1} {2} {3} {4}".format('Estado do mapa'.ljust(celPadding), \
                                           "%d, %d".ljust(celPadding)%(mapPart.rect.x,mapPart.rect.y), \
                                           "%d".ljust(celPadding)%gameTime, \
                                           "Estado Pintado".ljust(celPadding), \
                                           "%d".rjust(celPadding)%score_two+'\n'+'\n'))
                                score_total += score_two
                '''Coloring monsters with pen'''
                for monster in penHitMonsterList:
                    if(not(monster.dragged)):
                        MonsterList.remove(monster)
                        all_sprites_List.remove(monster)
                        monster = Monster(monster.rect.x, monster.rect.y, clPen.color, monster.form)
                        MonsterList.add(monster)
                        all_sprites_List.add(monster)
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                           "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                           "%d".ljust(celPadding)%gameTime, \
                                           "Monstro Pintado".ljust(celPadding), \
                                           "%d".rjust(celPadding)%score_two+'\n'+'\n'))
                        score_total += score_two
                clPen.resetPosition()
                

                                
        '''Bullet collision with monsters'''
        for bullet in bulletList:
            if(bullet.shot):
                bullet.positionUpdate()
            bulletHitMonsterList = pygame.sprite.spritecollide(bullet, MonsterList, bullet.shot)
            '''Destroying monsters and creating the broken parts'''
            for monster in bulletHitMonsterList:
                if (((monster.color == bullet.color) and (bullet.shot)) or \
                    ((monster.form == bullet.form) and (bullet.shot))):
                    bulletList.remove(bullet)
                    all_sprites_List.remove(bullet)
                    bkPart = brokenPart(monster.rect.x, monster.rect.y, monster.color, monster.form, 0)
                    bkPart2 = brokenPart(monster.rect.x-40, monster.rect.y, monster.color, monster.form, 1)
                    bkPart3 = brokenPart(monster.rect.x+40, monster.rect.y, monster.color, monster.form, 2)
                    brokenPartList.add(bkPart, bkPart2, bkPart3)
                    if(monster.dragged):
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                                   "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                                    "%d".ljust(celPadding)%gameTime, \
                                                   "Monstro Destruido Corretamente".ljust(celPadding), \
                                                   "%d".rjust(celPadding)%score_two+'\n'+'\n'))
                        score_total += score_two
                    if(monster.released):
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                                   "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                                    "%d".ljust(celPadding)%gameTime, \
                                                   "Monstro Lançado Corretamente".ljust(celPadding), \
                                                   "%d".rjust(celPadding)%score_two+'\n'+'\n'))
                        score_total += score_two
                        
                elif(((monster.color != bullet.color) and (bullet.shot)) or \
                     ((monster.form != bullet.form) and (bullet.shot))):
                    MonsterList.remove(monster)
                    all_sprites_List.remove(monster)
                    bkPart = brokenPart(monster.rect.x, monster.rect.y, monster.color, monster.form, 0)
                    bkPart2 = brokenPart(monster.rect.x-40, monster.rect.y, monster.color, monster.form, 1)
                    bkPart3 = brokenPart(monster.rect.x+40, monster.rect.y, monster.color, monster.form, 2)
                    brokenPartList.add(bkPart, bkPart2, bkPart3)
                    if(monster.dragged):
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                                   "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                                    "%d".ljust(celPadding)%gameTime, \
                                                   "Monstro Destruido Incorretamente".ljust(celPadding), \
                                                   "%d".rjust(celPadding)%score_one+'\n'+'\n'))
                        score_total += score_one
                    if(monster.released):
                        dataArchive.write("{0} {1} {2} {3} {4}".format('Monstro Defesa'.ljust(celPadding), \
                                                   "%d, %d".ljust(celPadding)%(monster.rect.x,monster.rect.y), \
                                                    "%d".ljust(celPadding)%gameTime, \
                                                   "Monstro Lançado Incorretamente".ljust(celPadding), \
                                                   "%d".rjust(celPadding)%score_one+'\n'+'\n'))
                        score_total += score_one
            '''Bullet collision with walls'''
            if( (bullet.rect.x < 0) or (bullet.rect.x > window_Width) or (bullet.rect.y < 0) \
                or (bullet.rect.y > (window_Height-50)) ):
                bulletList.remove(bullet)
                all_sprites_List.remove(bullet)
                '''Taking away the map painting'''
                totalNeighbors = 0
                for mapPart in mapPartList:
                    mapPart.updateImage(4)
                    for node in nx.nodes(mapGraph):
                        mapGraph.node[node]['nDifNeighbors'] = 0
        '''Claw collision with broken parts'''
        for claw in clawList:
            claw_Hit_bkPartList = pygame.sprite.spritecollide(claw, brokenPartList, False)
            for bkPart in claw_Hit_bkPartList:
                if((claw.isHolding) and (bkPart.piece not in claw.piecesCollected) and (bkPart.orbiting)):
                    spaceship.jumpFrame = True
                    spaceship.animate()
                    claw.isHolding = False
                    claw.piecesCollected.append(bkPart.piece)
                    if((len(claw.formsCollected)<1) or (bkPart.form in claw.formsCollected)):
                        claw.formsCollected.append(bkPart.form)
                    if((len(claw.colorsCollected)<1) or (bkPart.color not in claw.colorsCollected)):
                        claw.colorsCollected.append(bkPart.color)
                    brokenPartList.remove(bkPart)
                    dataArchive.write("{0} {1} {2} {3} {4}".format('Peça Quebrada'.ljust(celPadding), \
                                                   "%d, %d".ljust(celPadding)%(bkPart.rect.x,bkPart.rect.y), \
                                                    "%d".ljust(celPadding)%gameTime, \
                                                   "Peça Quebrada Coletada".ljust(celPadding), \
                                                   "%d".rjust(celPadding)%score_two+'\n'+'\n'))
                    score_total += score_two

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

        #print mouseMove
        #print updateAngle
        #print clPen.dragged
        #print tFinal
        #print "t2Initial:",t2Initial, "t2Final:",t2Final
        #print spaceship.moveUp
        #print game_seconds
        #print claw.piecesCollected
        #print mapGraph.node[neigh[0]]['color']        

        #print mapGraph.node[map2]['nDifNeighbors']

        print score_total
        
        '''Checking the painting of the map'''
        if(totalNeighbors == correctPainting):
            print "PAINTING CORRECT!"
            stage = 2
            dataArchive.write("{0} {1} {2} {3} {4}".format('Mapa'.ljust(celPadding), \
                               "%d, %d".ljust(celPadding)%(370,500), \
                                "%d".ljust(celPadding)%gameTime, \
                               "Mapa Colorido Corretamente".ljust(celPadding), \
                               "%d".rjust(celPadding)%score_two+'\n'+'\n'))
            score_total += score_two
        #else:
            #print totalNeighbors
        
        '''Drawing all objects'''
        screen.blit(upRing, (upRingX, upRingY))
        screen.blit(downPlanet, (downPlanetX, downPlanetY))
        screen.blit(downRing, (downRingX, downRingY))
        brokenPartList.draw(screen)
        screen.blit(upPlanet, (upPlanetX, upPlanetY))
        
        all_sprites_List.draw(screen)  

    if(stage == 2):
        #closing the archive file we created
        dataArchive.write("{0} {1} {2} {3}".format('Pontuação Total: ', \
                               "%d"%score_total+"pontos |", \
                               "Tempo Total: ", \
                               "%d"%gameTime+"segundos"+'\n'+'\n'))
        dataArchive.close()
        #getting the background color from black to white
        if(colorFading < 255):
            colorFading += 1
        screen.fill((colorFading, colorFading, colorFading))

        sun.positionUpdate()
        if(colorFading < 2):
            sun.readyToAnimate = True
            #print sun.readyToAnimate
        if(sun.readyToAnimate):
            sun.animate()

        sunList.draw(screen)
        
    pygame.display.flip()

pygame.display.quit()
