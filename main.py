import pygame #type: ignore - run in terminal to test
import random

pygame.init()
screen_w = 500
screen_l = 500

win = pygame.display.set_mode((screen_l, screen_w))
pygame.display.set_caption("flappybird")

     
GRAVITY= -10 #subtract this from height to get falling
FLAP_POWER = -13 #add to get upwards motion

test_image = pygame.image.load("flappy-bird-prototype.jpg").convert_alpha() #must go into spawnbird method

test_image = pygame.transform.scale(test_image, (50,50))
running = True

def calculate_pipe_space():
    width = 50
    height = random.randrange(35, 100) #min size for bird and up
    x = 450
    y = random.randrange(100,400) #min-max based on height of rectangle space taking into account window size

    return {"xcoord":x,"ycoord":y,"w":width,"h":height}

def calculate_pipe_spawn(pipe_params):
    #calculate thwere the two pipes will spawn based on calculate_pipe_space() as params
    top_x = pipe_params["xcoord"] 
    bottom_x = pipe_params["xcoord"]

    #top_y should probably be a constant 500
    top_y = pipe_params["ycoord"] - pipe_params["h"] - 100 #might have to be +
    bottom_y = pipe_params["ycoord"] + pipe_params["h"] + 100

    #pipe size should be: (total height - rectangle height)/2 and width is constant 
    #we should also calculate and return that in dict instead of "spacing"

    pipe_width = pipe_params["w"]
    pipe_height = (500 - pipe_params["h"])/2 


    return {"top_pipe":(top_x, top_y, pipe_width, pipe_height), "bottom_pipe":(bottom_x, bottom_y, pipe_width, pipe_height)}
y = 200
key_debounce = False

new_pipes = calculate_pipe_spawn(calculate_pipe_space())



#----DO THIS->> to make everything easier----#
#from the random num we actually only need to calculate space on the y axis - two y values
#the bottom y value can now just the bottom height spawn 
#so steps: random vertical line, top pipe y is constant, bottom y of the random vert line is the top y value for bottom pipe
#x starts at 500 and moves left as a variable 
#everything else is a constant


#everything below is just thought process for above#

#-----spawning pipes-----#
#problem - I only want the random num to be calculated ONCE per pipe spawning event 
#perhaps if we wait for "current pipe" to be at a certain spot on the screen? then run the calculate_pipe_spawn function
#this will work and allow proper spacing 
#to fix this goes alongside making x coord variable
#make the top pipe y value constant - then make its height vary, add "spacing" then place bottom pipe under spacing
#so the first step should be rewording calc_pipe_spawn to be more calc_pipe_height

#-----fixing pipe height/length-------#
#we also need to fix the pipe height(or length) ensuring they always come from the end of the screen

#--------making x coord a varible------#
#moving them across the screen could be a bit tricky too 
#we may have to change how were are return the values - so instead we should return from calc_pipe_spawn:
#(height, width) (bottom y) that way we can manipulate x in the game loop

while running:

    win.fill((0,55, 200))
    
    pygame.draw.rect(win, (255,255,0), (50,y, 25, 25))

    y += 0.1

    

    pygame.draw.rect(win, (0, 255, 0), (new_pipes["top_pipe"]))
    pygame.draw.rect(win, (0, 255, 0), (new_pipes["bottom_pipe"]))

    
     
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
                
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space is being clicked")
                
                y -= 100
    

    

    pygame.display.update()

pygame.quit()