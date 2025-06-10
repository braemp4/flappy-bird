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
          self.rect = self.image.get_rect(topleft=self.position)

     def flap(self, dy):
          self.rect.y -= dy



running = True

while running:
    
    pygame.display.update()

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
pygame.quit()