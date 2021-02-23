import json
import numpy as np

with open('rio_coord', 'r') as rio:
	coord_rio =json.loads(str(rio.read()))['features'][0]['geometry']['coordinates']


#coord_rio[0][2]=(np.zeros(len(coord_rio[0])))

for i in range(len(coord_rio[0])):
	coord_rio[0][i].append(0)
print(coord_rio)
with open('rio_cod', 'w') as rio:
	rio.write(str(coord_rio[0]))

'''
#print(coord_rio)
#coord_rio = np.array(coord_rio[0])*[-1,-1,0] - [40,9,0]
for i in range(len(coord_rio[0])):
	#for s in range(len(coord[0][i]))
	coord_rio[0][i][0]=coord_rio[0][i][0]*(-1)-40
	coord_rio[0][i][1]=coord_rio[0][i][1]*(-1)-9
#	coord_rio[0][i].append(0)
#coord_rio.append(np.zeros(len(coord_rio)))
#print('coordenadas: ',coord_rio['coordinates'])

print(coord_rio)
import pygmsh
import numpy as np


'''
with open('rio_cod','w') as file:
	file.write(str(coord_rio))

geom = pygmsh.opencascade.Geometry()

# Draw a cross.

print('adicionando poligono')
poly = geom.add_polygon(coord_rio,
    lcar=0.05
)

axis = [1,0]

print('gerando a estrutura geometrica')
#geom.extrude(
   # poly,
   # translation_axis=axis,
   # rotation_axis=axis,
  #  point_on_axis=[0, 0],
 #   angle=0
#)

#geom.add_physical_surface(poly)

print('estrutura feita, meshipando')
mesh = pygmsh.generate_mesh(geom)
import meshio
meshio.write('rio.vtk',mesh)
print('meshipado')
# mesh.points, mesh.cells, ...
'''
import pygmsh
import numpy as np

geom = pygmsh.built_in.Geometry()

# Draw a cross.
poly = geom.add_polygon([
    [ 0.0,  0.5, 0.0],
    [-0.1,  0.1, 0.0],
    [-0.5,  0.0, 0.0],
    [-0.1, -0.1, 0.0],
    [ 0.0, -0.5, 0.0],
    [ 0.1, -0.1, 0.0],
    [ 0.5,  0.0, 0.0],
    [ 0.1,  0.1, 0.0]
    ],
    lcar=0.05
)

axis = [0, 0, 1]

geom.extrude(
    poly,
    translation_axis=axis,
    rotation_axis=axis,
    point_on_axis=[0, 0, 0],
    angle=2.0 / 6.0 * np.pi
)

import meshio
import pymesh



#mesh = pygmsh.generate_mesh(geom)
# mesh.points, mesh.cells, ...
'''
