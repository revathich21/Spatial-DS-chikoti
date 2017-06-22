import math
import json
import sys
import os
DIRPATH = os.path.dirname(os.path.realpath(__file__))
def mercX(lon):
    """
    Mercator projection from longitude to X coord
    """
    zoom = 1.0
    lon = math.radians(lon)
    a = (256.0 / math.pi) * pow(2.0, zoom)
    b = lon + math.pi
    return int(a * b)


def mercY(lat):
    """
    Mercator projection from latitude to Y coord
    """
    zoom = 1.0
    lat = math.radians(lat)
    a = (256.0 / math.pi) * pow(2.0, zoom)
    b = math.tan(math.pi / 4 + lat / 2)
    c = math.pi - math.log(b)
    return int(a * c)

def adjust_location_coords(extremes,points,width,height):
    """
    Adjust your point data to fit in the screen. 
    Input:
        extremes: dictionary with all maxes and mins
        points: list of points
        width: width of screen to plot to
        height: height of screen to plot to
    """
    maxx = float(extremes['max_x']) # The max coords from bounding rectangles
    minx = float(extremes['min_x'])
    maxy = float(extremes['max_y'])
    miny = float(extremes['min_y'])
    deltax = float(maxx) - float(minx)
    deltay = float(maxy) - float(miny)

    adjusted = []

    for p in points:
        x,y = p
        x = float(x)
        y = float(y)
        xprime = (x - minx) / deltax         # val (0,1)
        yprime = ((y - miny) / deltay) # val (0,1)
        adjx = int(xprime*width)
        adjy = int(yprime*height)
        adjusted.append((adjx,adjy))
    return adjusted

def earth_quake(path):
   
    cords = []
    # Open our condensed json file to extract points
    f = open(path,'r')
    data = json.loads(f.read())
        


    # Loop through converting lat/lon to x/y and saving extreme values. 
    for quake in data:
        #st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        lon = quake['geometry']['coordinates'][0]
        lat = quake['geometry']['coordinates'][1]
        x,y = (mercX(lon),mercY(lat))
        cords.append((x,y))
  
    return cords

if __name__=='__main__':
    # Create dictionary to send to adjust method
    years = [x for x in range(1960,2017)]
    final_points = []
    allx = []
    ally = []
    list_p=[]
    for k in years:
        #print(k)
        final_points.append(earth_quake(DIRPATH+'/'+'./quake-'+str(k)+'-condensed.json'))
        #print(k)
        #print(final_points)
        for j in final_points:
            for i in j:
                #print(i[0],i[1])
                allx.append(i[0])
                ally.append(i[1])
        #final_points.append((x,y))
        #print(final_points)
        for i in final_points:
            for c in i:
                list_p.append((c[0],c[1]))
        extremes = {}
        extremes['max_x'] = max(allx)
        extremes['min_x'] = min(allx)
        extremes['max_y'] = max(ally)
        extremes['min_y'] = min(ally)
    
    
    # Get adjusted points
        screen_width = 1024
        screen_height = 512
        
        adj = adjust_location_coords(extremes,list_p,screen_width,screen_height)

        # Save adjusted points
        f = open(DIRPATH+'/'+'earthquake-adjusted.json','w')
        f.write(json.dumps(adj, sort_keys=True,indent=4, separators=(',', ': ')))
        f.close()
