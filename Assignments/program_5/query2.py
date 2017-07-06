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
    
    def earthquakes(self,collection,field,field_value,min_max,max_results,radius,point):
        x,y = literal_eval(point)
        #x,y = point
        i = 0
        j = 0
        earth_radius = 3963.2
        k =0
        final_earthquakes = []

        if  min_max == 'min':
            res = self.client['world_data'][collection].find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}},'properties.mag':{'$gt':float(field_value)}} )
            for r in res:
                if  i < int(max_results):
                    final_earthquakes.append(r['geometry']['coordinates'])
                    i+=1
                elif int(max_results) == 0:
                    final_earthquakes.append(r['geometry']['coordinates'])
                    
        elif min_max == 'max':
            res = self.client['world_data'][collection].find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}},'properties.mag':{'$lt':float(field_value)}} )            
        
            for r in res:
                if i < int(max_results):
                    final_earthquakes.append(r['geometry']['coordinates'])
                    i+=1
        return final_earthquakes
    def volcanos(self,collection,field,field_value,min_max,max_results,radius,point):
        x,y = literal_eval(point)
        i = 0
        j = 0
        earth_radius = 3963.2
        
        k =0
        final_volcanos = []

        if  min_max == 'min':
            res = self.client['world_data'][collection].find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}},'properties.Altitude': {'$gt':str(field_value)}} )
            for r in res:
                if  i < int(max_results):
                    final_volcanos.append(r['geometry']['coordinates'])
                    i+=1
                elif int(max_results) == 0:
                    final_volcanos.append(r['geometry']['coordinates'])
        elif min_max == 'max':
            res = self.client['world_data'][collection].find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}},'properties.Altitude':{'$lt':str(field_value)}} )
            for r in res:
                if i < int(max_results):
                    final_volcanos.append(r['geometry']['coordinates'])
                    i+=1
        return final_volcanos

    def meteorite(self,collection,field,field_value,min_max,max_results,radius,point):
        x,y = literal_eval(point)
        i = 0
        j = 0
        earth_radius = 3963.2
    
        k =0
        final_meteorite = []

        if  min_max == 'min':
            res = self.client['world_data'][collection].find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}},'properties.mass': {'$gt':str(field_value)}} )
            for r in res:
                if  i < int(max_results):
                    final_meteorite.append(r['geometry']['coordinates'])
                    i+=1
                elif int(max_results) == 0:
                    final_meteorite.append(r['geometry']['coordinates'])
        elif min_max == 'max':
            res = self.client['world_data'][collection].find( {'geometry' : { '$geoWithin': { '$centerSphere': [[x,y], float(radius)/earth_radius]}},'properties.mass':{'$lt':str(field_value)}} )
            for r in res:
                if i < int(max_results):
                    final_meteorite.append(r['geometry']['coordinates'])
                    i+=1
        return final_meteorite
        print(final_meteorite)

    def one_radius(self,radius,point):
        x,y = literal_eval(point)
        final = []
        final1 = []
        final2 = []
        earth_radius = 3963.2
        res = self.client['world_data'].volcanos.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [x, y ] ,float(radius)/earth_radius ] } }} )
        for r in res:
        
            final.append(r['geometry']['coordinates'])
            #print(final)
        return final
    def radius1(self,radius,point):
        x,y = literal_eval(point)
        final = []
        final1 = []
        earth_radius = 3963.2
        res = self.client['world_data'].earthquakes.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [x, y ] ,float(radius)/earth_radius ] } }} )
        for r in res:
        
            final1.append(r['geometry']['coordinates'])
            #print(final)
        return final1
    def radius2(self,radius,point):
        x,y = literal_eval(point)
        final = []
        final1 = []
        earth_radius = 3963.2
        res = self.client['world_data'].meteorite.find( { 'geometry': { '$geoWithin': { '$centerSphere': [ [x, y ] ,float(radius)/earth_radius ] } }} )
        for r in res:
        
            final1.append(r['geometry']['coordinates'])
            #print(final)
        return final1
    

        
        
        
    
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
    
def toLLtest(point):
        ans = []
        x,y = point
        for i in range(1,5):
            print(i)
            ans.append(mercToLL((x/i,y/i)))
            ans.append(mercToLL((x/4,y)))
        return ans

def toLL(point):
        ans = []
        x,y = point
        y += 256
        return mercToLL((x/4,y/4))

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
    final_earthquakes = 0
    points1 = []
    final_volcanos = 0
    final_meteorite= 0
    final = 0
    final1 = 0
    final2 = 0
    points2 = []
    screen_width = 1024
    screen_height = 512
    if len(sys.argv) > 3:
        final_earthquakes = mh.earthquakes(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
        #print(final_earthquakes)
        final_meteorite = mh.meteorite(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
        #print(result)
        final_volcanos = mh.volcanos(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7])
        #print(result)
       
        for coord in final_earthquakes:
            
            x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
            y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
            points.append((x,y))
        for coord in final_volcanos:
            
            x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
            y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
            points.append((x,y))
        for coord in final_meteorite:
            
            x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
            y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
            points.append((x,y))
    elif len(sys.argv) > 1:
        final = mh.one_radius(sys.argv[1],sys.argv[2])
        #print(final)
        for coord in final:
            
            x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
            y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
            points.append((x,y))  
       
        final1 = mh.radius1(sys.argv[1],sys.argv[2])  
        for coord in final1:
            
            x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
            y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
            points1.append((x,y))  
        
        final2 = mh.radius2(sys.argv[1],sys.argv[2])  
        for coord in final2:
            
            x = int((mh.mercX(coord[0]) / 1024 * screen_width))        
            y = int((mh.mercY(coord[1]) / 512 * screen_height) - 256)     
            points2.append((x,y))  
       
       
            
            



    background_colour = (255,255,255)
    black = (0,0,0)
    (width, height) = (1024, 512)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Query2')
    screen.fill(background_colour)
    pygame.init()
    bg = pygame.image.load(DIRPATH+'/'+'1024x512.png')
    pygame.display.flip()
        #Json File with all the adjusted coordinates
    running = True
    i = 1
    while running:
        screen.blit(bg, (0, 0))
        if len(sys.argv) > 3:
            for p in points:
                if(sys.argv[1]=='volcanos'):
                    pygame.draw.circle(screen, (194,35,38), p, 2,0)
                elif(sys.argv[1]=='earthquakes'):
                    pygame.draw.circle(screen, (0,255,255), p, 2,0)
                elif(sys.argv[1]=='meteorite'):
                    pygame.draw.circle(screen, (0,255,0), p, 2,0)
        elif(len(sys.argv) > 1):
            for p in points:
                pygame.draw.circle(screen,(194,35,38),p,2,0)
            for p in points1:
                pygame.draw.circle(screen,(0,255,255),p,2,0)
            for p in points2:
                pygame.draw.circle(screen,(0,255,0),p,2,0)


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
