import geopy
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Safari/537.36")
location = geolocator.geocode("petrolina Pernambuco")
print(location.address)
print(location.latitude,location.longitude)



from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#map = Basemap(resolution='i', projection='tmerc', lat_0 = location.latitude, lon_0 = location.longitude,lat_ts=2)

#map.drawmapboundary(fill_color='aqua')
#map.fillcontinents(color='#cc9955',lake_color='aqua')
#map.drawcoastlines()


map = Basemap(width=10000000,height=6000000,projection='lcc',
            resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
plt.figure(figsize=(19,20))
map.bluemarble()



#map.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')

#map.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize = 14)

plt.savefig('rio.png',dpi=800)
