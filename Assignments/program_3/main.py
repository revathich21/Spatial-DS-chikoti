import pygame
import sys,os
import json

DIRPATH = os.path.dirname(os.path.realpath(__file__))
def clean_area(screen,origin,width,height,color):
    """
    Prints a color rectangle (typically white) to "erase" an area on the screen.
    Could be used to erase a small area, or the entire screen.
    """
    ox,oy = origin
    points = [(ox,oy),(ox+width,oy),(ox+width,oy+height),(ox,oy+height),(ox,oy)]
    pygame.draw.polygon(screen, color, points, 0)

if __name__=='__main__':

    background_colour = (255,255,255)
    black = (0,0,0)
    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('MBRs')
    screen.fill(background_colour)
    pygame.init()
    bg = pygame.image.load(DIRPATH+'/'+'1024x512.png')
    pygame.display.flip()
    f = open('C:\\4553-Spatial-DS\\Resources\\Program_3_Starter\\EarthQuakeExample\\earthquake-adjusted.json','r')
    points = json.loads(f.read())
    
    running = True
    i = 5
    while running:
        screen.blit(bg, (0, 0))
        for p in points[:i]:
            pygame.draw.circle(screen, (255,255,255), p, 1,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clean_area(screen,(0,0),width,height,(255,255,255))
        i += 5
        if i > len(points):
            i = 5
        pygame.image.save(screen , "output.png")
        pygame.display.flip()
        
        pygame.time.wait(10)
