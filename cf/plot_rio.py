import matplotlib.pyplot as plt
import json
import yarah

with open('rio_cod','r') as file:
	rio_coord = (json.loads(str(file.read())))

rio_ = []
for point in rio_coord[0]:
	rio_.append([point[0],point[1]])

print(rio_)

x = [x[0] for x in rio_]
print(x)
y = [y[1] for y in rio_]
print(y)

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

lons = np.array(y)
lats = np.array(x)


#When you need specific data features on the map and the map's database does not provide them, you need to get them from somewhere and put to use. Here I get the data (long, lat) from plotting on GG My Maps. Once a line along the river path is plotted on the map, I can export the line data as KML. From that KML file, I grab only the list of (long,lat,h) and do some editing to get the data for lons and lats in the following code.

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
'''
lons = np.array([-74.8739737, -74.8633163, -74.8585042, -74.8564394, -74.8524035,
       -74.8459655, -74.830347 , -74.7874564, -74.7661703, -74.7593039,
       -74.7531241, -74.7345847, -74.7235983, -74.724285 , -74.7380179,
       -74.7469443, -74.7641104, -74.7826498, -74.8005026, -74.8142355,
       -74.8259085, -74.832775 , -74.8355215, -74.852001 , -74.8623007,
       -74.8698538, -74.9014395, -74.9158591, -74.9302786, -74.9453848,
       -74.9701041, -74.9982565, -75.0140494, -75.0270956, -75.047695 ,
       -75.0552481, -75.0655478, -75.0731009, -75.0916403, -75.111553 ,
       -75.1294058, -75.1369589, -75.1383322, -75.1300925, -75.1300925,
       -75.1355856, -75.1403921, -75.1695615, -75.1971884, -75.2130589,
       -75.2385357, -75.2697054, -75.3127467, -75.3521119, -75.3813978,
       -75.3987804, -75.4230237, -75.4458246])

lats = np.array([40.3023524, 40.2900427, 40.2829709, 40.2758991, 40.2654202,
       40.2567749, 40.2447233, 40.2248056, 40.2127464, 40.1959649,
       40.1828514, 40.1739328, 40.1597655, 40.1471699, 40.1392965,
       40.1356219, 40.134047 , 40.1219717, 40.1219717, 40.1282721,
       40.1277471, 40.1203965, 40.0988651, 40.0941378, 40.0878342,
       40.0825808, 40.0725981, 40.0704963, 40.0715472, 40.062614 ,
       40.050526 , 40.0310756, 40.0221371, 40.0179303, 40.0079382,
       40.0005746, 39.9884756, 39.9795315, 39.9742697, 39.9711125,
       39.9616398, 39.9542712, 39.9321608, 39.9179432, 39.9031959,
       39.8937139, 39.8847574, 39.8809411, 39.8785011, 39.8662113,
       39.8560259, 39.8505758, 39.8494219, 39.8388161, 39.8197959,
       39.8092274, 39.8007649, 39.7931383])
'''
#fig = plt.figure(figsize=[8,8])
#ax = plt.gca()

lat0 = -9.405649
#438528
lon0 = -40.504482
#537006

#m = Basemap(width=100_000, height=100_000 ,projection='stere', resolution='c',lon_0=lon0,lat_0=lat0,lat_ts=-2)

#m.drawmapboundary(fill_color='aqua')
# fill continents, set lake color same as ocean color.
#m.fillcontinents(color='coral',lake_color='aqua')


#lat,lon = m(lat0,lon0)
#lat,lon = m(lat,lon,inverse=True)
#m.plot(lat,lon,'b')
#m.drawmapboundary(fill_color='aqua')
#m.fillcontinents(color='coral', lake_color='aqua')
#m.drawcoastlines()




m = Basemap(width=1200_000, height=900_000, projection='stere', resolution='f', \
            lat_1=-9.390012, lat_2=-9.394808, lat_0=-9.43, lon_0=-40.520325)
#m.drawcoastlines()

m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral',lake_color='aqua')

m.drawrivers()  # no needed now

# plot Delaware river using arrays of data
#m.plot( *m(lat0,lon0), color='blue', zorder=18)

#m.drawcoastlines()
# m.drawrivers()  # no needed now

# plot Delaware river using arrays of data
m.plot( *m(lons, lats), linewidth=2.5, color='blue', zorder=18)

#m.bluemarble()

plt.savefig(f'rio[{lat0}].png',dpi=850)

#plt.plot(rio_)
#plt.savefig(f'rio.png',dpi=850)
