import pygame, glob, math
from pygame import *
from gameSettings import *

#For a better understanding of the code, visit http://www.pygame.org/news.html

pygame.init()

#Importing the images into different lists
objects_gameStage = glob.glob("./Arts/gameStage/*png")
objects_Bullets = glob.glob("./Arts/gameStage/Bullets/*png")
objects_Monster = glob.glob("./Arts/gameStage/Monsters/*png")
objects_colorPen = glob.glob("./Arts/gameStage/colorPen/*png")
objects_mapPart = glob.glob("./Arts/gameStage/MapPart/*png")
objects_brokenPart = glob.glob("./Arts/gameStage/brokenParts/*png")

#all_sprites_List is a list containing all sprites
all_sprites_List = pygame.sprite.RenderPlain()

#background is a Pygame.Surface containing the background image of the game
background = pygame.image.load(objects_gameStage[0]).convert_alpha()

#animationClock is used to help control an animation speed
animationClock = pygame.time.Clock()
animation_milliseconds = animationClock.tick(FPS)
animation_seconds = 1/float(animation_milliseconds)

#colorPenList is a list containing the images for the colorPens objects
colorPenList = pygame.sprite.RenderPlain()
class colorPen(pygame.sprite.Sprite):
    '''colorPen is the object that can change the color of a monster object
       and a mapPart object.
    '''
    def __init__(self, posX, posY, colorNumber):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.color is the color of the colorPen object
        self.color = colorNumber
        #self.image is the Pygame.Surface containing the colorPen object image
        self.image = pygame.image.load(objects_colorPen[colorNumber]).convert_alpha()
        #self.rect is the collision box for the colorPen object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))
        #self.dragged tells if the mouse button is being hold while the mouse is moving
        self.dragged = False
        #self.clicked tells if the colorPen object was clicked by the mouse
        self.clicked = False
        #Variable that will help returning the colorPen to it's initial position
        self.notInitialPosition = False 

    def positionUpdate(self):
        '''Function that enables drag and drop movement to colorPen object
        '''
        self.notInitialPosition = True
        mousePos = pygame.mouse.get_pos()
        self.rect.x = mousePos[0] - 10
        self.rect.y = mousePos[1]

    def resetPosition(self):
        '''Function that takes the colorPen object to it's initial position
        '''
        self.rect.x = self.posX
        self.rect.y = self.posY
        self.notInitialPosition = False

#mapPartList is a list containing the images for the mapParts objects
mapPartList = pygame.sprite.RenderPlain()
class mapPart(pygame.sprite.Sprite):
    '''mapPart is the object that represents a state of the whole map.
       The whole map is made by 25 mapParts(states)
    '''
    def __init__(self, posX, posY, colorNumber, part):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.color is the color of the mapPart object
        self.color = colorNumber
        #self.clicked tells if the mapPart object was clicked by the mouse
        self.clicked = False
        #self.change is used to help changing the mapPart image according to it's color
        self.change = False   
        #self.part tells which part(state) is the mapPart object
        self.part = part 
        #self.image is the Pygame.Surface containing the mapPart object image
        if(self.color == 0):
            self.image = pygame.image.load(objects_mapPart[self.part]).convert_alpha()
        elif(self.color == 1):
            self.image = pygame.image.load(objects_mapPart[self.part+26]).convert_alpha()
        elif(self.color == 2):
            self.image = pygame.image.load(objects_mapPart[self.part+52]).convert_alpha()
        elif(self.color == 3):
            self.image = pygame.image.load(objects_mapPart[self.part+78]).convert_alpha()
        elif(self.color == 4):
            self.image = pygame.image.load(objects_mapPart[self.part+104]).convert_alpha()
        #self.rect is the collision box for the mapPart object image
        self.rect = self.image.get_rect(topleft = (self.posX, self.posY))  
        
    def updateImage(self, color):
        '''updateImage is responsible for changing the sprite of each map part,
           creating the effect of painting
        '''
        self.change = True
        if(self.change):
            self.color = color
            if(self.color == 0):
                self.image = pygame.image.load(objects_mapPart[self.part]).convert_alpha()
            elif(self.color == 1):
                self.image = pygame.image.load(objects_mapPart[self.part+26]).convert_alpha()
            elif(self.color == 2):
                self.image = pygame.image.load(objects_mapPart[self.part+52]).convert_alpha()
            elif(self.color == 3):
                self.image = pygame.image.load(objects_mapPart[self.part+78]).convert_alpha()
            elif(self.color == 4):
                self.image = pygame.image.load(objects_mapPart[self.part+104]).convert_alpha()
        self.rect = self.image.get_rect(topleft = (self.posX, self.posY))
        self.change = False



class EnemyShip(pygame.sprite.Sprite):
    '''Enemy ship is the object that shoots a Bullet object in differents colors and forms
    '''
    def __init__(self, posX, posY, updateAng, side):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.readyToAnimate tells when the shooting animation can be rendered
        self.readyToAnimate = False
        #self.animation is a list containing all sprites used to create the shooting animation
        self.animation = []
        #self.animation_frame represents the current frame of the shooting animation
        self.animation_frame = 0    
        #Speed of the shooting animation in frames per second
        self.fps = 35               
        #self.enemyship_frames is a list containing all the imported frames
        self.enemyship_frames = glob.glob("./Arts/gameStage/EnemyShipAnimation/*png")
        for i in range(0,len(self.enemyship_frames)):
            self.animation.append(pygame.image.load(self.enemyship_frames[i]).convert_alpha())
        #self.image is the Pygame.Surface containing the EnemyShip object image(frame)
        self.image = self.animation[0]
        #self.rect is the collision box for the EnemyShip object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))
        #self.updateAngle is the angle of the Bullet object that is going to be shot
        self.updateAngle = updateAng
        #self.amtToUpdateAngle is the value that increments self.updateAngle
        self.amtToUpdateAngle = side
        
    def animate(self):
        '''Function that runs the shooting animation of the EnemyShip object
        '''
        if(animationClock.get_time()%2 == 0):
            self.animation_frame += 1
        if(self.animation_frame > self.fps):
            self.animation_frame = 0
            self.readyToAnimate = False
        self.image = self.animation[self.animation_frame]        
    
    def angleUpdate(self):
        '''Function that changes the direction in which the next Bullet object will be shot
        '''
        self.updateAngle += self.amtToUpdateAngle
        if(self.posX < 400):    #This part of the code is executed by the enemy ship in the left corner
            if(self.updateAngle > 4):
                self.amtToUpdateAngle *= -1
            elif(self.updateAngle < 0):
                self.amtToUpdateAngle *= -1
        elif(self.posX > 400):  #This part of the code is executed by the enemy ship in the right corner
            if(self.updateAngle < -4):
                self.amtToUpdateAngle *= -1
            elif(self.updateAngle > 0):
                self.amtToUpdateAngle *= -1


class Spaceship(pygame.sprite.Sprite):
    '''SpaceShip carries the claw, which is responsible for recicling.
       Recicling means getting 3 broken parts together to create a monster
    '''
    def __init__(self, posX, posY):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.animation is a list containing all sprites used to create the charging animation
        self.animation = []
        #self.animation_frame represents the current frame of the charging animation
        self.animation_frame = 0
        #self.numberOfFrames is the total number of frames used in the charging animation
        self.numberOfFrames = 4
        #self.jumpFrame tells when the game can change the frame of the charging animation
        self.jumpFrame = False
        #self.spaceship_frames is a list containing all the imported frames
        self.spaceship_frames = glob.glob("./Arts/gameStage/Spaceship/*png")
        for i in range(0,self.numberOfFrames):
            self.animation.append(pygame.image.load(self.spaceship_frames[i]).convert_alpha())
        #self.image is the Pygame.Surface containing the SpaceShip object image(frame)
        self.image = self.animation[0]
        #self.rect is the collision box for the SpaceShip object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))
        #self.moveUp and self.moveDown tell when the Spaceship object will move up or down
        self.moveUp, self.moveDown = False, False
        #self.moveLeft and self.moveRight tell when the Spaceship object will move left or right
        self.moveLeft, self.moveRight = False, False
        #self.speed is the speed of the Spaceship object movement
        self.speed = 2
        
    def animate(self):
        '''Function used to run the charging animation
        '''
        if(self.jumpFrame == True):
            self.animation_frame += 1
            self.jumpFrame = False
        if(self.animation_frame > (self.numberOfFrames-1)):
            self.animation_frame = 0
        self.image = self.animation[self.animation_frame]

    def positionUpdate(self):
        '''Movement of the SpaceShip object in X and Y axis,
           with the borders of the screen being the limits
        '''
        if((self.moveUp == True) and (self.rect.y > 10)):
            self.rect.y -= self.speed
        elif((self.moveDown == True) and (self.rect.y < 550)):
            self.rect.y += self.speed
        if((self.moveLeft == True) and (self.rect.x > 0)):
            self.rect.x -= self.speed
        elif((self.moveRight == True) and (self.rect.x < 700)):
            self.rect.x += self.speed

#clawList contains the image of the Claw object
clawList = pygame.sprite.RenderPlain()
class Claw(pygame.sprite.Sprite):
    '''Claw is responsible for recicling the broken parts into another monster
    '''
    def __init__(self, posX, posY):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.image is the Pygame.Surface containing the Claw object image
        self.image = pygame.image.load(objects_gameStage[5]).convert_alpha()
        #self.rect is the collision box for the Claw object image
        self.rect = self.image.get_rect(topleft = (self.posX, self.posY))
        #self.holding tells when the Claw can grab a brokenPart object
        self.isHolding = False
        #self.piecesCollected is a list containing the parts that build the monster
        self.piecesCollected = []
        #self.formsCollected is a list used to help prevent getting repeated parts
        self.formsCollected = []
        #self.colorsCollected is a list containing the color of the monsters that were destroyed
        self.colorsCollected = []   
        
    def positionUpdate(self,x, y):
        '''Function responsible for maintaining the claw
           attached to the spaceship
        '''
        self.rect.x = (x+50)
        self.rect.y = (y+52)

#bulletList is a list containing the images for the Bullets objects
bulletList = pygame.sprite.RenderPlain()
class Bullet(pygame.sprite.Sprite):
    '''Bullet is the object that can destroy a Monster object or decolorize a MapPart object
    '''
    def __init__(self, posX, posY, colorNumber, form, angle, side):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.color is the color of the Bullet object
        self.color = colorNumber
        #self.form is the form of the Bullet object
        self.form = form
        #self.dx is the speed of the Bullet object movement in the x axis
        self.dx = angle
        #self.dy is the speed of the Bullet object movement in the y axis
        self.dy = 1    
        #self.shot tells when the Bullet object is shot by an EnemyShip object
        self.shot = False      
        #self.created tells when the Bullet object is created
        self.created = False   
        #self.right tells when the Bullet object is created by the right EnemyShip object
        self.right = side
        #self.image is the Pygame.Surface containing the Bullet object image
        if(self.form == 0):
            #print "form 0"
            self.image = pygame.image.load(objects_Bullets[colorNumber]).convert_alpha()
        elif(self.form == 1):
            #print "form 1"
            self.image = pygame.image.load(objects_Bullets[colorNumber+4]).convert_alpha()
        elif(self.form == 2):
            #print "form 2"
            self.image = pygame.image.load(objects_Bullets[colorNumber+8]).convert_alpha()
        #self.rect is the collision box for the Bullet object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def positionUpdate(self):
        '''Function responsible for the Bullet object movement
        '''
        self.rect.x += self.dx
        self.rect.y += self.dy

#MonsterList is a list containing the images for the Monsters objects
MonsterList = pygame.sprite.RenderPlain()
#mouseGetSpeed is used to tell when the player can throw a Monster object
mouseGetSpeed = False
class Monster(pygame.sprite.Sprite):
    '''Monsters are used to destroy Bullet objects
    '''
    def __init__(self, posX, posY, colorNumber, form):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.color is the color of the Monster object
        self.color = colorNumber
        #self.form is the form of the Monster object
        self.form = form
        #self.dragged tells if the mouse button is being hold while the mouse is moving
        self.dragged = False
        #self.clicked tells if the Monster object was clicked by the mouse
        self.clicked = False
        #self.released tells when the mouse button that was dragging was released
        self.released = False
        #self.mouseVel tells when the mouse is not moving
        self.mouseVel = (0,0)
        #self.image is the Pygame.Surface containing the Monster object image
        if(self.form == 0):
            #print "form 0"
            self.image = pygame.image.load(objects_Monster[colorNumber]).convert_alpha()
        elif(self.form == 1):
            #print "form 1"
            self.image = pygame.image.load(objects_Monster[colorNumber+4]).convert_alpha()
        elif(self.form == 2):
            #print "form 2"
            self.image = pygame.image.load(objects_Monster[colorNumber+8]).convert_alpha()
        #self.rect is the collision box for the Monster object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def positionUpdate(self):
        '''Function that enables drag and drop movement to Monster object
        '''
        mousePos = pygame.mouse.get_pos()
        self.rect.x = mousePos[0] - 10
        self.rect.y = mousePos[1] - 10

    def throw(self, v):
        '''Function used to throw a Monster object
        '''
        speedX = v[0]
        speedY = v[1]
        self.rect.x += speedX
        self.rect.y += speedY

#brokenPartList is a list containing the images for the brokenParts objects
brokenPartList = pygame.sprite.RenderPlain()
class brokenPart(pygame.sprite.Sprite):
    '''Broken Parts are the things that the monsters drop
       when they are destroyed
    '''
    def __init__(self, posX, posY, colorNumber, form, piece):
        '''Constructor of this class
        '''
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.dragged tells if the mouse button is being hold while the mouse is moving
        self.dragged = False
        #self.clicked tells if the brokenPart object was clicked by the mouse
        self.clicked = False
        #Floating movement
        self.maxY = 4
        self.minY = -4
        self.vy = 5
        self.ay = 1
        self.timer = 0
        self.orbiting = False
        #self.angle and self.pi are used to rotate the brokenPart objects around the planet
        self.angle, self.pi = 0 , 3.14
        #self.piece is used make 3 different circular movements
        self.piece = piece
        #self.centerX and self.centerY represent the center of the ring's rect
        self.centerX, self.centerY = 380, 500 
        #self.grabbed tells when the brokenPart object is grabbed by the Claw object
        self.grabbed = False
        #self.color is the color of the brokenPart object
        self.color = colorNumber
        #self.color is the form of the brokenPart object
        self.form = form
        #self.image is the Pygame.Surface containing the brokenPart object image
        if(self.form == 0):
            #print "form 0"
            self.image = pygame.image.load(objects_brokenPart[piece]).convert_alpha()
        elif(self.form == 1):
            #print "form 1"
            self.image = pygame.image.load(objects_brokenPart[piece+3]).convert_alpha()
        elif(self.form == 2):
            #print "form 2"
            self.image = pygame.image.load(objects_brokenPart[piece+6]).convert_alpha()
        #self.rect is the collision box for the brokenPart object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))

    def mouseUpdate(self):
        '''Function used for the drag and drop logic to take the floating pieces
           to orbit around the planet
        '''
        mousePos = pygame.mouse.get_pos()
        self.rect.x = mousePos[0] - 10
        self.rect.y = mousePos[1] - 10
    
    def floatingUpdate(self):
        '''Function used to make the broken parts float
           when they aren't orbiting
        '''
        if((self.orbiting == False) and (self.grabbed == False)):
            self.rect.y += self.vy
            self.vy += self.ay
            if(self.vy > self.maxY):        #When the piece goes down too much, starts going up
                self.ay = -1
            elif(self.vy < self.minY):      #When the piece goes up too much, starts going down
                self.ay = 1
            #print self.vy
            
    def orbitUpdate(self):
        '''Function used to make the broken parts orbit around the planet
        '''
        if((self.grabbed == False) and (self.orbiting == True)):
            self.angle += .03
            if(self.angle > 2*self.pi):
                self.angle = self.angle - 2*self.pi
            if((self.orbiting == True) and (self.piece == 0)):          #Head movement
                self.rect.x = self.centerX + 220*math.cos(self.angle)
                self.rect.y = self.centerY + 30*math.sin(self.angle)
            elif((self.orbiting == True) and (self.piece == 1)):        #Body movement
                self.rect.x = self.centerX + 280*math.cos(self.angle)
                self.rect.y = self.centerY + 40*math.sin(self.angle)
            elif((self.orbiting == True) and (self.piece == 2)):        #Foot movement
                self.rect.x = self.centerX + 340*math.cos(self.angle)
                self.rect.y = self.centerY + 50*math.sin(self.angle)

#These next objects are used to create a "3D perspective" around the planet
#downPlanet
downPlanet = pygame.image.load(objects_gameStage[1]).convert_alpha()
downPlanetX, downPlanetY = 220, 513

#upPlanet
upPlanet = pygame.image.load(objects_gameStage[2]).convert_alpha()
upPlanetX, upPlanetY = 220, 354

#downRing
downRing = pygame.image.load(objects_gameStage[3]).convert_alpha()
downRingX, downRingY = 41, 505

#upRing
upRing = pygame.image.load(objects_gameStage[4]).convert_alpha()
upRingX, upRingY = 40, 440


#Sun appears when the game is finished
sunList = pygame.sprite.RenderPlain()
class Sun(pygame.sprite.Sprite):
    '''Sun is just an animation of the game ending
    '''
    def __init__(self, posX, posY):
        #Constructor of this class
        pygame.sprite.Sprite.__init__(self)
        #self.posX and self.posY represents the position of the object in X and Y axis
        self.posX, self.posY = posX, posY
        #self.readyToAnimate tells when the shooting animation can be rendered
        self.readyToAnimate = False
        #self.animationTimer will help creater a smoother animation
        self.animationTimer = 0
        #self.animation is a list containing all sprites used to create the charging animation
        self.animation = []
        #self.animation_frame represents the current frame of the charging animation
        self.animation_frame = 0
        #self.numberOfFrames is the total number of frames used in the charging animation
        self.numberOfFrames = 40
        #self.spaceship_frames is a list containing all the imported frames
        self.sun_frames = glob.glob(".\Arts\gameStage\Sun\*png")
        for i in range(0,self.numberOfFrames):
            self.animation.append(pygame.image.load(self.sun_frames[i]).convert_alpha())
        #self.image is the Pygame.Surface containing the SpaceShip object image(frame)
        self.image = self.animation[0]
        #self.rect is the collision box for the SpaceShip object image
        self.rect = self.image.get_rect(center = (self.posX, self.posY))
        
    def animate(self):
        #Function used to run the charging animation
        self.animationTimer += 1
        if(self.animationTimer > 5):
            self.animation_frame += 1
            self.animationTimer = 0
        if(self.animation_frame > (self.numberOfFrames-1)):
            self.animation_frame = self.numberOfFrames-1
            self.readyToAnimate = False
        if(self.animation_frame > (self.numberOfFrames-10)):
            self.rect.x -= 2
            self.rect.y -= 1
        self.image = self.animation[self.animation_frame]

    def positionUpdate(self):
        if(self.rect.y > 100):
            self.rect.y += -5

        

