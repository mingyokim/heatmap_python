import json, requests, pprint

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP

#url = 'https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&locale=en-US&currency=USD&_format=for_search_results_with_minimal_pricing&_offset=0&fetch_facets=true&ib=false&ib_add_photo_flow=true&location=Lake%20Tahoe%2C%20CA%2C%20US&min_bathrooms=0&min_bedrooms=0&min_beds=1&min_num_pic_urls=10&price_max=210&price_min=40&sort=1'
url = 'https://api.airbnb.com/v2/search_results?client_id=3092nxybyb0otqw18e8nh5nty&locale=en-US&currency=USD&_format=for_search_results_with_minimal_pricing&_offset=0&location=New%20York%2C%20NY%2C%20US&_limit=15'

resp = requests.get(url=url)
data = json.loads(resp.text)

searchResult = data["search_results"]
print len(searchResult)

class Restaurant: 
	def __init__(self, latitude, longitude, price):
		self.latitude = latitude
		self.longitude = longitude
		self.price = price
	def display(self):
		print "Latitude: ", self.latitude, ", Longitude: ", self.longitude, ", Price: ", self.price

restList = []

for item in searchResult:
	listing = item["listing"]
	#pprint.pprint (listing)
	pricing_quote = item["pricing_quote"]
	restList.append(Restaurant(listing.get("lat"), listing.get("lng"), pricing_quote.get("rate").get("amount")))

latList = []
longList = []
priceList = []
for rest in restList:
	#rest.display()
	latList.append(rest.latitude)
	longList.append(rest.longitude)
	priceList.append(rest.price)

gridsize = 100
#PLT.subplot(111)
PLT.hexbin(latList, longList, C=priceList, gridsize=gridsize, cmap=CM.jet, bins=None)
PLT.axis([min(latList), max(latList), min(longList), max(longList)])

cb = PLT.colorbar()
cb.set_label('price')
PLT.savefig("new_york.png")
