import sys, pygame                                          #1
pygame.init()                                               #2
                                                            #3
velikost = sirka, vyska = 800, 600                          #4
rychlost = [2, 2]                                           #5
cerna = 0, 0, 0                                             #6
                                                            #7
screen =  pygame.display.set_mode(velikost)                 #8
                                                            #9
micek = pygame.image.load("mic.gif")                      #10
micekRect = micek.get_rect()  

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)
                           
                                                            #12
while 1:                                                    #13
     for udalost in  pygame.event.get():                    #14
         if udalost.type == pygame.QUIT:      sys.exit()    #15
                                                            #16
     micekRect =  micekRect.move(rychlost)                  #17
     if micekRect.left < 0 or micekRect.right > sirka:      #18
         rychlost[0] = -rychlost[0]                         #19 
     if micekRect.top < 0 or micekRect.bottom > vyska:      #20 
         rychlost[1] = -rychlost[1]                         #21
                                                            #22
     screen.fill(cerna)  
     # render text
     label1 = myfont.render("x:"+str(micekRect.top), 1, (255,255,0))
     screen.blit(label1, (50, 20))
     label2 = myfont.render("y:"+str(micekRect.left), 1, (255,255,0))
     screen.blit(label2, (50, 50))
                                   
     screen.blit(micek, micekRect)                          #24
     pygame.display.flip()