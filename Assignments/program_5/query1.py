import math
from math import radians,sin,cos
import os
import sys
import pygame
import pprint as pp
from ast import literal_eval
from pymongo import MongoClient
DIRPATH = os.path.dirname(os.path.realpath(__file__))
client = MongoClient()
#class mongoHelper(object):
#    def __init__(self):
#        self.client = MongoClient()         



def get_nearest_neighbor(self,lon,lat,r):
    # air_res = self.db_ap.find( { 'geometry' : { '$geoWithin' : { '$geometry' : poly } } })
    air_res = self.['world_data'].airport.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [lon, lat ] , r / 3963.2 ] } }} )

    min = 999999
        
    for ap in air_res:
        lon2 = ap['geometry']['coordinates'][0]
        lat2 = ap['geometry']['coordinates'][1]
        d = self._haversine(lon,lat,lon2,lat2)
        if d < min:
            min = d

            closest_ap = ap

    return closest_ap
def _haversine(self,lon1, lat1, lon2, lat2):
    """
        Calculate the great circle distance between two points 
        on the earth (specified in decimal degrees)
        """
        # convert decimal degrees to radians 
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 3956 # Radius of earth. Use 6371 for km. Use 3956 for miles
        return c * r

    
        
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

    
def clean_area(screen,origin,width,height,color):
    """
    Prints a color rectangle (typically white) to "erase" an area on the screen.
    Could be used to erase a small area, or the entire screen.
    """
    ox,oy = origin
    points = [(ox,oy),(ox+width,oy),(ox+width,oy+height),(ox,oy+height),(ox,oy)]
    pygame.draw.polygon(screen, color, points, 0)


def run_tests():
    mh = mongoHelper()
    points = []
    result = 0
    screen_width = 1024
    screen_height = 512

    
    for r in result:
        x = int((mh.mercX(r[0]) / 1024 * screen_width))        
        y = int((mh.mercY(r[1]) / 512 * screen_height) - 256)     
        points.append((x,y))

    background_colour = (255,255,255)
    black = (0,0,0)
    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Query_1')
    screen.fill(background_colour)
    pygame.init()
    bg = pygame.image.load(DIRPATH+'/'+'1024x512.png')
    pygame.display.flip()
    #Json File with all the adjusted coordinates
    running = True
        #i = 1
    while running:
        screen.blit(bg, (0, 0))
        for p in points:
                
            pygame.draw.circle(screen, (194,35,38), p, 2,0)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clean_area(screen,(0,0),width,height,(255,255,255))
            if event.type == pygame.QUIT:
                #pygame.image.save(screen,DIRPATH+'/'+'EarthQuake_ScreenShot.png')
                running = False
            

        pygame.display.flip()

			
if __name__=='__main__':
   
    run_tests()