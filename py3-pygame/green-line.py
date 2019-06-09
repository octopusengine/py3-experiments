import pygame, random, sys, math

# You have to call this to make it work.
pygame.init()

# Set up some variables containing the screeen size
sizeX=600
sizeY=600

# Set the starting colour
colour = pygame.Color('#009900')

# Create the pygame window
window = pygame.display.set_mode([sizeX,sizeY])

# Create the clock object
clock = pygame.time.Clock()

# Put a name on the window.
pygame.display.set_caption("Spirograph")

# Initialise more variables
# k and l are numbers between 0 and 1.
# k is the ratio of the distance of the small circle from the big circle
l=random.random()

# l is the ratio of the small circles radius (to the hole with the pen in)
# to the distance from the centre of the large circle.
k=random.random()

# Counter - real number - not integer.
i=0.0

# Scaling factor (Radius of big circle)
R=300

x=0
y=0

# This will loop forever.
while True:
    t = math.radians(i)

    newx = R * ((1-k) * math.cos(t) + l*k*math.cos((1-k) * t / k ))
    newy = R * ((1-k) * math.sin(t) - l*k*math.sin((1-k) * t / k ))

    if (x==0 and y==0):
       pass
    else:
       pygame.draw.line(window,colour,(x+R,y+R),(newx+R,newy+R),2)
    x=newx
    y=newy

    i=i+5

    clock.tick(40)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
sys.exit()