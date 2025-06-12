import pygame #type: ignore - run in terminal to test
import random

pygame.init()
screen_w = 500
screen_l = 500

win = pygame.display.set_mode((screen_l, screen_w))
pygame.display.set_caption("flappybird")

class pipe(pygame.sprite.Sprite):
     def __init__(self, image, x, y, height):
          self.WIDTH = 100
          self.height = height
          self.x = x
          self.y = y
          self.position = (x,y)
          self.image = image
          self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.height)
     def spawn_pipes(x,y):
          pass #use pygame.draw.rect at pos 
          #also use random height 
          #this will spawn a set of two pipes
    

class bird(pygame.sprite.Sprite):
     def __init__(self, img, position):
          super().__init__()
          self.position = position
          self.image = img
          self.rect = self.image.get_rect(topleft=self.position),
          self.score = 0
          self.alive = False
     def spawn_bird(self):
          pass #draw bird at start pos
          
     def flap(self, dy):
          self.rect.y += dy

     def apply_gravity(self, grav):
          self.rect.y -= grav #goes at top of loop
          
     def get_score(self):
          return self.score

     def add_score(self):
          self.score += 1
          
     def game_over(self):
          self.alive = False

     def new_game(self):
          if not self.alive:
               self.alive = True
          #spawn_bird gets called here
     
GRAVITY= -10 #subtract this from height to get falling
FLAP_POWER = -13 #add to get upwards motion

running = True

while running:
    
    pygame.display.update()

     #we get menu with high score and strart game (first as cli then as gui)

     
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
pygame.quit()