import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\program_4\\WorldData\\earthquakes-1960-2017.json","r")

data = f.read()

data = json.loads(data)
# earth ={}
earthquakes = []

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
          gj['geometry'] = i['geometry']
          gj['properties'] = i
          del gj['properties']['geometry']
          earthquakes.append(gj)
        
          del earthquakes [999: len(earthquakes)-1]
    
        


out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\earthquakes_gj.geojson","w")

   

         
    
out.write(json.dumps(earthquakes, sort_keys=False,indent=4, separators=(',', ': ')))
    

out.close()
