import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\program_4\\WorldData\\world_cities_large.json","r")

data = f.read()

data = json.loads(data)
large_cities = []

'''
      "geometry": {
        "type": "Point",
        "coordinates": [
          -120.966003418,
          42.3642997742
        ]
      }
'''


for k,v in data.items():
    
    for i in v:
        gj = collections.OrderedDict()
        gj['type'] = "Feature"
        gj['properties'] = i
        lat = i['lat']
        lon = i['lon']
        del gj['properties']['lat']
        del gj['properties']['lon']
        gj["geometry"] = {}
        gj["geometry"]["type"]="Point"
        try:
            gj["geometry"]["coordinates"] = [
                        float(lon),
                        float(lat)
                    ]
            large_cities.append(gj)
        except ValueError:
                 pass
        del large_cities [999: len(large_cities)-1] 
#airports={}    

#airports['type'] = "FeatureCollection"    
#airports['features'] = all_airports


    #self.adjusted_poly_dict[id].append(poly)   

#pp.pprint(all_airports)

out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\largecities_gj.geojson","w")

out.write(json.dumps(large_cities, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()
