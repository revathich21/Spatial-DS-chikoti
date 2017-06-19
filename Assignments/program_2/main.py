"""
Program:
--------
    Program 2 - display points from files based on x-cordinate and y-cordinate.

Description:
------------
    program reads data from five different files based on x and y values and prints 
    points on screen with correspoding colors.Method used here scales values tobest fit on screen.
    
Name: revathi chikoti
Date:19 june 2017
"""
import pygame
import random
from dbscan import *
import sys,os
import pprint as pp
def clean_area(screen,origin,width,height,color):
    """
    Prints a color rectangle (typically white) to "erase" an area on the screen.
    Could be used to erase a small area, or the entire screen.
    """
    ox,oy = origin
    points = [(ox,oy),(ox+width,oy),(ox+width,oy+height),(ox,oy+height),(ox,oy)]
    pygame.draw.polygon(screen, color, points, 0)

background_colour = (255,255,255)
black = (0,0,0)
(width, height) = (1000,1000)

screen = pygame.display.set_mode((width, height))   
pygame.display.set_caption('Simple Line')           #to dispaly title on screen
screen.fill(background_colour)

    #pygame.display.flip()
 
epsilon = 20
min_pts = 5.0
DIRPATH = os.path.dirname(os.path.realpath(__file__))



keys = []

def cordinates(path):
    """Fetches x-cordinates, y-cordinates from given files.
    scales them to best fit on screen
    Args:
        path : path of each file whose points to be displayed on screen
        keys: A sequence of strings representing the key of each table row
            to fetch.

    Returns:
        A list called points, mapping keys to the corresponding file row data
        fetched. Each row is represented as a tuple of intergers.
       
        If a key from the keys argument is missing from the list,
        then that row was not found in the list.

    Raises:
        ValueError : if value is not found
    """
    crimes = []
    points = []
    got_keys = False
    with open(path) as f:  #islandfile
        for line in f:
            line = ''.join(x if i % 2 == 0 else x.replace(',', ':') for i, x in enumerate(line.split('"')))
            line = line.strip().split(',')
            if not got_keys:
                keys = line
                #print(keys)
                got_keys = True
                continue
            crimes.append(line)

        list_x = []
        list_y = []
        list_z = []
        list_w = []
        list_a = []
        for crime in crimes:
            try:
                x = crime[19]
                x1 = int(x)
                list_x.append(x1)
                x2 = 913357
                x3 = 1067226
                y = crime[20]    
                y1 = int(y)
                list_y.append(y1)
                y2 =  121250
                y3 =  271820
            except ValueError:
                pass
        for x1 in list_x:
            x4 = (((x1-x2)/(x3-x2))*1000)
            x5 = int(x4)
            list_z.append(x5)
        for y1 in list_y:
            y4 = 1-((y1-y2)/(y3-y2))
            y5 = y4*1000
            y6 = int(y5)
           # print(y4)
            list_w.append(y6)
    list_a = list(zip(list_z, list_w))
    points.extend(list_a)
    return points
    
    
if __name__ == '__main__':

    points0 = []
    points1 = [] 
    points2 = [] 
    points3 = [] 
    points4 = []
    #paths for each file
    points0 = cordinates(DIRPATH+'/../NYPD_CrimeData/filtered_crimes_bronx.csv')
    points1 = cordinates(DIRPATH+'/../NYPD_CrimeData/filtered_crimes_brooklyn.csv')
    points2 = cordinates(DIRPATH+'/../NYPD_CrimeData/filtered_crimes_manhattan.csv')
    points3 = cordinates(DIRPATH+'/../NYPD_CrimeData/filtered_crimes_queens.csv')
    points4 = cordinates(DIRPATH+'/../NYPD_CrimeData/filtered_crimes_staten_island.csv')

    running = True
    while running:
        for p in points0:
            pygame.draw.circle(screen, (2,120,120), p, 3, 0) #bronx
        for p1 in points1:
            pygame.draw.circle(screen, (128,22,56), p1 ,3, 0) #brooklyn
        for p2 in points2:
            pygame.draw.circle(screen, (194,35,38) ,p2, 3, 0) #manhatan
        for p3 in points3:
            pygame.draw.circle(screen, (243,115,56) ,p3, 3, 0) #queens
        for p4 in points4:
            pygame.draw.circle(screen, (253,182,50), p4, 3, 0) #island
        
        pygame.display.flip()
    
   
