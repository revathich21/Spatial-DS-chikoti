import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\program_4\\WorldData\\state_borders.json","r")

data = f.read()

data = json.loads(data)
all_states = []

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
        #lat = k['Lat']
        #lon = k['Lon']
        borders = k["borders"]
        del gj['properties']['borders']
        #del gj['properties']['Lon']
        gj["geometry"] = {}
        gj["geometry"]["type"]="Polygon"
        try:
            gj["geometry"]["coordinates"] = borders
                  
            all_states.append(gj)
        except ValueError:
                pass
        del all_states [999: len(all_states)-1] 

#airports={}    
#airports['type'] = "FeatureCollection"    
#airports['features'] = all_airports


    #self.adjusted_poly_dict[id].append(poly)   

#pp.pprint(all_airports)

out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\states_gj.geojson","w")

out.write(json.dumps(all_states, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()