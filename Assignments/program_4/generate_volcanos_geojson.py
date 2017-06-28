import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\program_4\\WorldData\\world_volcanos.json","r")

data = f.read()

data = json.loads(data)
all_volcanos = []

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
        lat = k['Lat']
        lon = k['Lon']
        del gj['properties']['Lat']
        del gj['properties']['Lon']
        gj["geometry"] = {}
        gj["geometry"]["type"]="Point"
        try:
            gj["geometry"]["coordinates"] = [
                    float(lon),
                    float(lat)
                ]
            all_volcanos.append(gj)
        except ValueError:
                pass
        del all_volcanos [999: len(all_volcanos)-1] 

#airports={}    
#airports['type'] = "FeatureCollection"    
#airports['features'] = all_airports


    #self.adjusted_poly_dict[id].append(poly)   

#pp.pprint(all_airports)

out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\volcanos1_gj.geojson","w")

out.write(json.dumps(all_volcanos, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()