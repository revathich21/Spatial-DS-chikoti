import pprint as pp
import os,sys
import json
import collections


f = open("C:\\4553-Spatial-DS\\Resources\\Data\\program_4\\WorldData\\countries.geo.json","r")

data = f.read()

data = json.loads(data)
all_country = []

'''
      "geometry": {
        "type": "Point",
        "coordinates": [
          -120.966003418,
          42.3642997742
        ]
      }
'''
del data [999: len(data)-1]


out = open("C:\\4553-Spatial-DS\\Resources\\Data\\WorldData\\country_gj.geojson","w")

out.write(json.dumps(data, sort_keys=False,indent=4, separators=(',', ': ')))

out.close()