import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\world_cities_small_w_pop.json","r")

data = f.read()

data = json.loads(data)
all_cities = []

'''
      "geometry": {
        "type": "Point",
        "coordinates": [
          -120.966003418,
          42.3642997742
        ]
      }
'''


for k in data:


        gj = collections.OrderedDict()
        gj['type'] = "Feature"
        gj['properties'] = k
        lat = k['lat']
        lng = k['lng']
        del gj['properties']['lat']
        del gj['properties']['lng']
        gj["geometry"] = {}
        #gj["geometry"]["type"]="Point"
        try:
            gj["geometry"]["coordinates"] = [
                    float(lng),
                    float(lat)
                ]
            all_cities.append(gj)
        except ValueError:
                pass

#airports={}    
#airports['type'] = "FeatureCollection"    
#airports['features'] = all_airports


    #self.adjusted_poly_dict[id].append(poly)   

#pp.pprint(all_airports)

out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\cities_gj.geojson","w")

out.write(json.dumps(all_cities, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()