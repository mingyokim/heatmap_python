import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP
import csv

#restList = []

latList = []
longList = []
priceList = []

LAT_INDEX = 6
LONG_INDEX = 7
PRICE_INDEX = 9
MAX_PRICE = 1000
with open("listings.csv", "r") as f:
	#next(f)
	reader = csv.DictReader(f)
	for row in reader:
		if float(row['price']) > MAX_PRICE:
			continue

		latList.append(float(row['latitude']))
		longList.append(float(row['longitude']))
		priceList.append(float(row['price']))

	'''
	for line in f:
		linesplit = line.split(',')
		#print linesplit
		if len(linesplit) <= LAT_INDEX:
			continue
		
		latList.append(linesplit[LAT_INDEX])
		longList.append(linesplit[LONG_INDEX])
		priceList.append(linesplit[PRICE_INDEX])
	'''
f.close		



'''
class Restaurant: 
	def __init__(self, latitude, longitude, price):
		self.latitude = latitude
		self.longitude = longitude
		self.price = price
	def display(self):
		print "Latitude: ", self.latitude, ", Longitude: ", self.longitude, ", Price: ", self.price
for item in searchResult:
	listing = item["listing"]
	#pprint.pprint (listing)
	pricing_quote = item["pricing_quote"]
	#restList.append(Restaurant(listing.get("lat"), listing.get("lng"), pricing_quote.get("rate").get("amount")))
	latList.append(listing.get("lat"))
	longList.append(listing.get("lng"))
	priceList.append(pricing_quote.get("rate").get("amount"))
for rest in restList:
	#rest.display()
	latList.append(rest.latitude)
	longList.append(rest.longitude)
	priceList.append(rest.price)
'''

gridsize = 100
#PLT.subplot(111)
PLT.hexbin(latList, longList, C=priceList, gridsize=gridsize, cmap=CM.jet, bins=None)
PLT.axis([min(latList), max(latList), min(longList), max(longList)])

cb = PLT.colorbar()
cb.set_label('price')

'''
map = Basemap(projection='merc', llcrnrlat=min(latList), urcrnrlat=max(latList), llcrnrlon=min(longList), urcrnrlon=max(longList), resolution='h')
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='grey')
map.drawmapboundary()
'''

#PLT.show();
PLT.savefig("new_york_file.png")
