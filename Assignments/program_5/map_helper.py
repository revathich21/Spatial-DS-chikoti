import os,sys
import math



def get_extremes(points):
    maxX = -999
    minX = 999
    maxY = -999
    minY = 999


# http://wiki.openstreetmap.org/wiki/Mercator
def merc_xy(lon,lat):
    #x portion
    r_major=6378137.000
    x = r_major*math.radians(lon)

    #y portion
    if lat>89.5:lat=89.5
    if lat<-89.5:lat=-89.5
    r_major=6378137.000
    r_minor=6356752.3142
    temp=r_minor/r_major
    eccent=math.sqrt(1-temp**2)
    phi=math.radians(lat)
    sinphi=math.sin(phi)
    con=eccent*sinphi
    com=eccent/2
    con=((1.0-con)/(1.0+con))**com
    ts=math.tan((math.pi/2-phi)/2)/con
    y=0-r_major*math.log(ts)
    return (x,y)


def mercXY(lon,lat):
    r = 6378137
    scale = math.cos(lat * math.pi / 180.0)
    x = scale * lon * math.pi * r / 180.0
    y = scale * r * math.log( math.tan((90.0+lat) * math.pi / 360.0) )
    return (x,y)

def mercX(lon,zoom = 1):
    lon = math.radians(lon)
    a = (256 / math.pi) * pow(2, zoom)
    b = lon + math.pi
    return a * b

def mercY(lat,zoom = 1):
    lat = math.radians(lat)
    a = (256.0 / math.pi) * pow(2, zoom)
    b = math.tan(math.pi / 4 + lat / 2)
    c = math.pi - math.log(b)
    return (a * c)

def adjust_location_coords(extremes,points,width,height):
    """
    Adjust your point data to fit in the screen. 
    Input:
        extremes: dictionary with all maxes and mins
        points: list of points
        width: width of screen to plot to
        height: height of screen to plot to
    """
    max_x = float(extremes['max_x']) 
    min_x = float(extremes['min_x'])
    max_y = float(extremes['max_y'])
    min_y = float(extremes['min_y'])
    deltax = float(max_x) - float(min_x)
    deltay = float(max_y) - float(min_y)

    adjusted = []

    for p in points:
        x,y = p
        x = float(x)
        y = float(y)
        xprime = (x - min_x) / deltax    # val (0,1)
        yprime = ((y - min_y) / deltay)  # val (0,1)
        adjx = int(xprime*width)
        adjy = int(yprime*height)-256
        adjusted.append((adjx,adjy))
    return adjusted

def find_extremes(res,width,height):
    '''
    find the extremes in a set of points.
    input:
        result_list: a list geojson entries
    '''
    extremes={}
    allx = []
    ally = []
    points = []
    for r in res:
        lon = r['geometry']['coordinates'][0]
        lat = r['geometry']['coordinates'][1]
        x,y = (mercX(lon),mercY(lat))
        allx.append(x)
        ally.append(y)
        points.append((x,y))
    extremes['max_x'] = width
    extremes['min_x'] = 0
    extremes['max_y'] = height
    extremes['min_y'] = 0
    extremes['max_x'] = width
    extremes['min_x'] = 0
    extremes['max_y'] = height
    extremes['min_y'] = 0
        
    return extremes,points

def flatten_country_polygons(geometry):
    adjusted_polys = []
    if geometry['type'] == 'Polygon':
        pass
    else:
        for polygons in geometry['coordinates']:
            for polygon in polygons:
                newp = []
                for p in polygon:
                    newp.append([mercX(p[0]),mercY(p[1])])
                adjusted_polys.append(newp)
        return adjusted_polys