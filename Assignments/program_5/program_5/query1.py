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
class mongoHelper(object):
    def __init__(self):
        self.client = MongoClient()         



    def airport(self,source,destination,radius,point):
        lon,lat = literal_eval(point)
        i = 0
        j = 0
        earth_radius = 3963.2
        final_result = []
        #lon2,lat2 = literal_eval(point)
        res = self.client['world_data'].airport.find( {'geometry' : { '$geoWithin': { '$centerSphere': [[lon,lat], float(radius)/earth_radius]}}})
        res_list = []
        k =0
        min = 99999
        for r in res:

            
            lon2 = r['geometry']['coordinates'][0]
            lat2 = r['geometry']['coordinates'][1]
            
            if d < min:
                min = d

                closest_ap = r

        return closest_ap
                
            #final_result.append(r['geometry']['coordinates'])
           
    def haversine(point1, point2, miles=True):
        """ Calculate the great-circle distance between two points on the Earth surface.
        :input: two 2-tuples, containing the latitude and longitude of each point
        in decimal degrees.
        Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))
        :output: Returns the distance bewteen the two points.
        The default unit is kilometers. Miles can be returned
        if the ``miles`` parameter is set to True.
        """
        # unpack latitude/longitude
        lat1, lng1 = point1
        lat2, lng2 = point2

        # convert all latitudes/longitudes from decimal degrees to radians
        lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

        # calculate haversine
        lat = lat2 - lat1
        lng = lng2 - lng1
        d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
        h = 2 * RADIUS_KM * asin(sqrt(d))
        if miles:
            return h * 0.621371  # in miles
        else:
            return h  # in kilometers

    
        
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

    result = mh.airport(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
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