
import math
import os
import sys
import pygame
import pprint as pp
import json
from ast import literal_eval
from pygame.locals import *
from pymongo import MongoClient
DIRPATH = os.path.dirname(os.path.realpath(__file__))
client = MongoClient()
class mongoHelper(object):
    def __init__(self):
        self.client = MongoClient() 

    def airports(self,source,radius,point):
        x,y = literal_eval(point)
        earth_radius = 3963.2
        
        airport = []

       
        res = self.client['world_data'].airport.find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}}} )
        for r in res:
                
            airport.append(r['geometry']['coordinates'])
        return airport
    def mercX(self,lon):
        """
        Mercator projection from longitude to X coord
        """
        zoom = 1.0
        lon = math.radians(lon)
        a = (256.0 / math.pi) * pow(2.0, zoom)
        b = lon + math.pi
        return int(a * b)


    def mercY(self,lat):
        """
        Mercator projection from latitude to Y coord
        """
        zoom = 1.0
        lat = math.radians(lat)
        a = (256.0 / math.pi) * pow(2.0, zoom)
        b = math.tan(math.pi / 4 + lat / 2)
        c = math.pi - math.log(b)
        return int(a * c)      
def mercToLL(point):
        lng,lat = point
        lng = lng / 256.0 * 360.0 - 180.0
        n = math.pi - 2.0 * math.pi * lat / 256.0
        lat = (180.0 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n))))
        return (lng, lat)       
def run_tests():
    
    mh = mongoHelper()
    points = []

    
    screen_width = 1024
    screen_height = 512
    
    final = mh.airports(sys.argv[1],sys.argv[2],sys.argv[3])
        
       
    for coord in final:
            
        x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
        y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
        points.append((x,y))
    background_colour = (255,255,255)
    black = (0,0,0)
    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Query1')
    screen.fill(background_colour)
    pygame.init()
    bg = pygame.image.load(DIRPATH+'/'+'1024x512.png')
    pygame.display.flip()
        #Json File with all the adjusted coordinates
    running = True
    i = 1
    while running:
        screen.blit(bg, (0, 0))
        
        for p in points:
                pygame.draw.circle(screen, (194,35,38), p, 2,0)
                

                    #print(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clean_area(screen,(0,0),width,height,(255,255,255))
            if event.type == MOUSEBUTTONUP:
                
                x,y = event.pos
                print(event.pos)
                
            if event.type == pygame.QUIT:
                    
                running = False
    

        pygame.display.flip()
if __name__=='__main__':

    run_tests()
