MONGO Database name : world_data
Collections:
	
	cities
	countries
	earthquakes
	globalterrorism
	meteorite
	state
	volcanos
Bash file:
	in geojson folder
Query1: Find Interesting Features along some path

	python query1.py DFW BOM 500
	python query1.py MNL YYT 500

Query2 :  Nearest Neighbor

	 python query2.py 1000 [140.8,39.76]
	 python query2.py volcanos Altitude 1000 max 10 2000 [140.8,39.76]
	 python query2.py meteorite mass 1000 min 20 2000 [140.8,39.76]
	
Query3 :  Clustering

	 python query3.py earthquakes 5 20
	 python query3.py volcanos 5 30
	 python query3.py meteorite 5 30


