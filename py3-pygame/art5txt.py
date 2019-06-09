import pygame, random, sys

# random art
# http://huffton.wordpress.com/2012/05/13/raspberry-pi-python-introduction-part-2/

# You have to call this to make it work.
pygame.init()

# Set up some variables containing the screeen size
sizeX=600
sizeY=600


# Start drawing from the middle of the window.
x=sizeX/2
y=sizeY/2

# Set the starting colour
colour = pygame.Color('#333333')

# Create the pygame window
window = pygame.display.set_mode([sizeX,sizeY])

# Put a name on the window.
pygame.display.set_caption("Random art")

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

# render text
label = myfont.render("Some text!", 1, (255,255,0))
window.blit(label, (100, 100))

# This will loop forever.
while True:
    colour.r = (colour.r+random.randint(-3,3)) % 255
    colour.g = (colour.g+random.randint(-3,3)) % 255
    colour.b = (colour.b+random.randint(-3,3)) % 255

    newx=x+random.randint(-3,3)
    newy=y+random.randint(-3,3)

    label = myfont.render(str(x), 1,colour)
    window.blit(label, (100, x*2))

   # Make sure the new point is visible
    if newx > sizeX:
       newx = sizeX
    if newy > sizeY:
       newy = sizeY
    if newx < 0:
       newx = 0
    if newy < 0:
       newy = 0

   
    pygame.draw.line(window,colour,(x,y),(newx,newy),2)
    x=newx
    y=newy
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()