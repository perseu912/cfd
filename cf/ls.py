import json

with open('rio_cod','r') as file:
  rio_coord = (json.loads(str(file.read())))
  print(rio_coord)
  #file.write(rio_coord)
  
with open('rio.geo','w') as geo:
  n=0
  for i in rio_coord:
    _point = f'Point({n}) ='+'{'+str(i[0])+','+str(i[1])+'};\n'
    print(f'escrevendo o ponto {n}: {_point}')
    geo.write(_point)
    n += 1
  nl=[]
  n = 0
  for i in range(len(rio_coord)-1):
    nl.append(n)
    _line = 'Line('+str(n)+') = {'+str(n)+','+str(n+1)+'};\n'
    print(f'escrevendo a linha {n}: {_line}')
    geo.write(_line)
    n += 1
  
  geo.write('Line loop(200) = {%s};\n'%(nl))
  geo.write(f'Plane surface(16) = {20};\n')  
  
