'''
Auther: Sourav
Date of creation: 5/12/2021
Class: 9th
Section: A
'''
#importing importing modules
import pygame
from pygame import mixer
import time, sys, math

#importing the datafile so i can use the functions
import datafile

#initiallise modules
pygame.init()
mixer.init()
pygame.font.init()

#screen variables
screenX = 1000
screenY = 800
screen = pygame.display.set_mode((screenX, screenY))

# loop and other variables
mainMenu = True
mainGame = False

fps =  30
clock = pygame.time.Clock()
sec = 1.7

images = {}
sounds = {}

#font variables
font = pygame.font.Font("Font/morse.ttf", 150)
normalFont = pygame.font.Font(None, 150)
morse = " "
letter = " "

#colour variables
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (19,19,19)

#game images
images['icon'] = pygame.image.load("Images/icon.png").convert_alpha()
images['bg'] = pygame.image.load("Images/bg.png").convert_alpha()
images['bgText'] = pygame.image.load("Images/bgText.png").convert_alpha()

#game sounds
sounds['dot'] = mixer.Sound("Sounds/dot.WAV")
sounds['dash'] = mixer.Sound("Sounds/dash.WAV")

#resizing the images
images['bg'] = pygame.transform.scale(images['bg'],(screenX, screenY))
images['bgText'] = pygame.transform.scale(images['bgText'],(screenX, screenY))

#defining icon and title
pygame.display.set_caption('Solar System')
pygame.display.set_icon(images['icon'])

#defining the MorseText
def showMorse(morse):
  letterImg = font.render(morse, True, white)

  letterImgHeight = letterImg.get_height()
  letterImgWidth = letterImg.get_width()

  var = screenY / 1/4
  screen.blit(letterImg,((screenX /2) - (letterImgWidth / 2), (screenY - var) - (letterImgHeight / 2)))

#defining the Text
def showLetter(letter):
  letterImg = normalFont.render(letter, True, white)

  letterImgHeight = letterImg.get_height()
  letterImgWidth = letterImg.get_width()
  screen.blit(letterImg,((screenX /2) - (letterImgWidth / 2), (screenY /2)/2 - (letterImgHeight / 2)))

def showNote():
  font = pygame.font.Font(None, 25)
  letterImg = font.render("NOTE: Only Press The Key One time and dont Spam!!", True, red)

  letterImgHeight = letterImg.get_height()
  letterImgWidth = letterImg.get_width()
  screen.blit(letterImg,((screenX /2) - (letterImgWidth / 2), (screenY - 50)))

#ifCondition function
def condition():
  
  screen.blit(images['bg'],(0,0))
  showMorse(morse)
  showLetter(letter)
  showNote()
  pygame.display.update()

#mainMeny loop
while mainMenu:
  screen.blit(images['bg'],(0,0))
  screen.blit(images['bgText'], (0,0))

  for event in pygame.event.get():
    
    if event.type == pygame.KEYDOWN:
      mainMenu = False
      mainGame = True

    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()

#game loop
while mainGame:
  screen.blit(images['bg'],(0,0))
  showMorse(morse)
  showLetter(letter)
  showNote()
  
  for event in pygame.event.get():
    
    if event.type == pygame.KEYDOWN :

      if event.key == pygame.K_SPACE:
        time.sleep(2.5)

      #alphabets
      if event.key == pygame.K_a:
        letter, morse = 'A', 'A'
        condition()
        datafile.a()
        time.sleep(sec)
        
      if event.key == pygame.K_b:
        letter, morse = 'B', 'B'
        condition()
        datafile.b()
        time.sleep(sec)

      if event.key == pygame.K_c:
        letter, morse = 'C', 'C'
        condition()
        datafile.c()
        time.sleep(sec)

      if event.key == pygame.K_d:
        letter, morse = 'D', 'D'
        condition()
        datafile.d()
        time.sleep(sec)

      if event.key == pygame.K_e:
        letter, morse = 'E', 'E'
        condition()
        datafile.e()
        time.sleep(sec)

      if event.key == pygame.K_f:
        letter, morse = 'F', 'F'
        condition()
        datafile.f()
        time.sleep(sec)

      if event.key == pygame.K_g:
        letter, morse = 'G', 'G'
        condition()
        datafile.g()
        time.sleep(sec)

      if event.key == pygame.K_h:
        letter, morse = 'H', 'H'
        condition()
        datafile.h()
        time.sleep(sec)

      if event.key == pygame.K_i:
        letter, morse = 'I', 'I'
        condition()
        datafile.i()
        time.sleep(sec)

      if event.key == pygame.K_j:
        letter, morse = 'J', 'J'
        condition()
        datafile.j()
        time.sleep(sec)
        
      if event.key == pygame.K_k:
        letter, morse = 'K', 'K'
        condition()
        datafile.k()
        time.sleep(sec)

      if event.key == pygame.K_l:
        letter, morse = 'L', 'L'
        condition()
        datafile.l()
        time.sleep(sec)

      if event.key == pygame.K_m:
        letter, morse = 'M', 'M'
        condition()
        datafile.m()
        time.sleep(sec)

      if event.key == pygame.K_n:
        letter, morse = 'N', 'N'
        condition()
        datafile.n()
        time.sleep(sec)

      if event.key == pygame.K_o:
        letter, morse = 'O', 'O'
        condition()
        datafile.o()
        time.sleep(sec)

      if event.key == pygame.K_p:
        letter, morse = 'P', 'P'
        condition()
        datafile.p()
        time.sleep(sec)

      if event.key == pygame.K_q:
        letter, morse = 'Q', 'Q'
        condition()
        datafile.q()
        time.sleep(sec)

      if event.key == pygame.K_r:
        letter, morse = 'R', 'R'
        condition()
        datafile.r()
        time.sleep(sec)

      if event.key == pygame.K_s:
        letter, morse = 'S', 'S'
        condition()
        datafile.s()
        time.sleep(sec)

      if event.key == pygame.K_t:
        letter, morse = 'T', 'T'
        condition()
        datafile.t()
        time.sleep(sec)

      if event.key == pygame.K_u:
        letter, morse = 'U', 'U'
        condition()
        datafile.u()
        time.sleep(sec)

      if event.key == pygame.K_v:
        letter, morse = 'V', 'V'
        condition()
        datafile.v()
        time.sleep(sec)

      if event.key == pygame.K_w:
        letter, morse = 'W', 'W'
        condition()
        datafile.w()
        time.sleep(sec)

      if event.key == pygame.K_x:
        letter, morse = 'X', 'X'
        condition()
        datafile.x()
        time.sleep(sec)

      if event.key == pygame.K_y:
        letter, morse = 'Y', 'Y'
        condition()
        datafile.y()
        time.sleep(sec)

      if event.key == pygame.K_z:
        letter, morse = 'Z', 'Z'
        condition()
        datafile.z()
        time.sleep(sec)

      #numbers
        
      if event.key == pygame.K_1:
        letter, morse = '1', '1'
        condition()
        datafile.one()
        time.sleep(sec)

      if event.key == pygame.K_2:
        letter, morse = '2', '2'
        condition()
        datafile.two()
        time.sleep(sec)

      if event.key == pygame.K_3:
        letter, morse = '3', '3'
        condition()
        datafile.three()
        time.sleep(sec)

      if event.key == pygame.K_4:
        letter, morse = '4', '4'
        condition()
        datafile.four()
        time.sleep(sec)

      if event.key == pygame.K_5:
        letter, morse = '5', '5'
        condition()
        datafile.five()
        time.sleep(sec)

      if event.key == pygame.K_6:
        letter, morse = '6', '6'
        condition()
        datafile.six()
        time.sleep(sec)

      if event.key == pygame.K_7:
        letter, morse = '7', '7'
        condition()
        datafile.seven()
        time.sleep(sec)

      if event.key == pygame.K_8:
        letter, morse = '8', '8'
        condition()
        datafile.eight()
        time.sleep(sec)

      if event.key == pygame.K_9:
        letter, morse = '9', '9'
        condition()
        datafile.nine()
        time.sleep(sec)

      if event.key == pygame.K_0:
        letter, morse = '0', '0'
        condition()
        datafile.zero()
        time.sleep(sec)
 
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  clock.tick(fps)
  pygame.display.update()




