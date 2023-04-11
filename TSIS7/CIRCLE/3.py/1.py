

# import pygame module in this program 
import pygame
  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()
  
# create the display surface object  
# of specific dimension..e(500, 500).  
game_window = pygame.display.set_mode((550, 550))
  
# set the pygame game_windowdow name 
pygame.display.set_caption("Moving rectangle")
  
  
# dimensions of the object 
width = 50
height = 50
  
# object current co-ordinates 
x = 200
y = 200
# Vocity / speed of movement
V = 20
  
# Indicates pygame is running
run = True
  
# infinite loop 
while run:
    # creates time delay of 10ms 
    pygame.time.delay(10)
      
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  
    for event in pygame.event.get():
          
        # if event object type is QUIT  
        # then quitting the pygame  
        # and program both.  
        if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False
    # stores keys pressed 
    keys = pygame.key.get_pressed()
      
    # if left arrow key is pressed
    if keys[pygame.K_LEFT] and x>0:
          
        # decrement in x co-ordinate
        x -= V
          
    # if left arrow key is pressed
    if keys[pygame.K_RIGHT] and x<500-width:
          
        # increment in x co-ordinate
        x += V
         
    # if left arrow key is pressed   
    if keys[pygame.K_UP] and y>0:
          
        # decrement in y co-ordinate
        y -= V
          
    # if left arrow key is pressed   
    if keys[pygame.K_DOWN] and y<500-height:
        # increment in y co-ordinate
        y += V
         
              
    # completely fill the surface object  
    # with black colour  
    game_window.fill((0, 255, 0))
      
    # dragame_windowg object on screen which is rectangle here 
    pygame.draw.circle(game_window, (255, 0, 0), (x, y), 20)
      
    # it refreshes the game_windowdow
    pygame.display.flip() 
  
# closes the pygame game_windowdow 
pygame.quit()
