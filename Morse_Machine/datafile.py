'''
this is the data file and contains all the data required for the actual program to run,
do not delete please :3
'''

#importing modules
import pygame
from pygame import mixer
import time

pygame.init()
mixer.init()

#variables
images = {}
sounds = {}
sec = 1.2

keyPressed = False

#game sounds
sounds['dot'] = mixer.Sound("Sounds/dot.WAV")
sounds['dash'] = mixer.Sound("Sounds/dash.WAV")

#functions alphabets
def  a():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    
def  b():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  c():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  d():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  e():
    sounds['dot'].play()

def  f():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  g():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  h():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  i():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  j():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  k():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  l():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def  m():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  n():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play() 

def  o():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  p():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play() 

def  q():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()    

def  r():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play() 

def  s():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()    

def  t():
    sounds['dot'].play()    

def  u():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  v():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  w():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  x():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  y():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def  z():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

#numerical veriables
def one():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def two():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def three():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

def four():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dash'].play()

def five():
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def six():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def seven():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def eight():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()
    time.sleep(sec)
    sounds['dot'].play()

def nine():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dot'].play()

def zero():
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()
    time.sleep(sec)
    sounds['dash'].play()

    







