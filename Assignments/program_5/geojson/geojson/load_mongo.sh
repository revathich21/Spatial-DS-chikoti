mongo world_data --eval "db.dropDatabase()"
mongoimport --db world_data --collection airport       --type json --file airport.geojson        --jsonArray
mongoimport --db world_data --collection countries      --type json --file countries.geojson       --jsonArray
mongoimport --db world_data --collection meteorite     --type json --file meteorite.geojson       --jsonArray
mongoimport --db world_data --collection volcanos       --type json --file volcanos.geojson        --jsonArray
mongoimport --db world_data --collection earthquakes    --type json --file earthquakes.geojson     --jsonArray
mongoimport --db world_data --collection cities         --type json --file world_cities.geojson    --jsonArray
mongoimport --db world_data --collection states         --type json --file state_borders.geojson   --jsonArray
mongoimport --db world_data --collection globalterrorism      --type json --file globalterrorism.geojson --jsonArray