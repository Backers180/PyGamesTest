import pygame
import random


pygame.init()



screen = pygame.display.set_mode((800, 600))



#title and icon

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load('ship2.png')

pygame.display.set_icon(icon)



#Player
playerImg = pygame.image.load('ship2.png')

playerX = 380				#initial positions

playerY = 500

playerX_change = 0

playerY_change = 0


#enemy
enemyImg = pygame.image.load('alien.png')

enemyX = random.randint(64,736)

enemyY = random.randint(64,150)



def player(x,y):

    screen.blit(playerImg,(x,y))

def enemy(x,y):

    screen.blit(enemyImg,(x,y))

    

running = True

while running:			#Main Code



  screen.fill((0,0,0))

     

  for event in pygame.event.get():

    if event.type== pygame.QUIT:

      running = False

  

    if event.type == pygame.KEYDOWN:		#left and right controls

        if event.key == pygame.K_LEFT:

            playerX_change = -0.1



        if event.key == pygame.K_RIGHT:

            playerX_change = 0.1





    if event.type == pygame.KEYUP:

        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:

            playerX_change = 0



  playerX += playerX_change
  player(playerX,playerY)
  

  if playerX <0:		#total xlength = 800 pixels spaceship is 64x64 pix

      playerX = 0

  elif playerX >736:	#800 - 64 = 736

      playerX = 736

      

  pygame.display.update()
