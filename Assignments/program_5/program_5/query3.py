import math
import os
import pygame
import pprint as pp
from ast import literal_eval
from map_helper import *
from pymongo import MongoClient
from dbscan import *

DIRPATH = os.path.dirname(os.path.realpath(__file__))
client = MongoClient()
class mongoHelper(object):
    def __init__(self):
        self.client = MongoClient()         
    def run(self):
        background_colour = (255,255,255)
        black = (0,0,0)
        (width, height) = (1024, 512)
        color_list = {'volcanos':(255,0,0),'earthquakes':(70,173,212),'meteorite':(76,187,23)}
        box_color = (255,255,0)

        pygame.init()
        bg = pygame.image.load('C:\\program_5\\1024x512.png')
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Query3')
        screen.fill(background_colour)
        pygame.display.flip()

        #separate sys.argv
        feature = sys.argv[1]
        min_pts = float(sys.argv[2])
        eps = float(sys.argv[3])

        drawn = False

        res = []
       
        points = []
        extremes = {}
        screen.blit(bg, (0, 0))
        pygame.display.flip()

        if feature == 'volcanos':
            res = client['world_data'][feature].find()
            extremes, points = find_extremes(res, width, height)
        elif feature == 'earthquakes':
            res1 = client['world_data'][feature].find({'properties.mag':{'$gt':(7)}})
            extremes, points = find_extremes(res1, width, height)
        elif feature == 'meteorite':
            res2 = client['world_data'][feature].find({'properties.mass':{'$gt':('80000')}})
            extremes, points = find_extremes(res2, width, height)

        points = adjust_location_coords(extremes,points,width,height)

        mbrs = calculate_mbrs(points, eps, min_pts)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
    
        while drawn ==  False:
            for pt in points:
                pygame.draw.circle(screen, color_list[feature], pt, 2,0)
                pygame.display.flip()
            for i in range(5):
                pygame.draw.polygon(screen, box_color, mbrs[i], 2)
                pygame.display.flip()
            
                
if __name__=='__main__':
    mh = mongoHelper()
    mh.run()



