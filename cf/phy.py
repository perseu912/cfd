import matplotlib.pyplot as plt
import numpy as np


class Particle:
	def __init__(self,size,color,pos,m=.5,alpha=.5):
		self.pos = np.array(pos)
		#plt.scatter(x,y,s=size,c=color,alpha=alpha)
		self.vel = np.array([0,0])
		self.acc = np.array([0,0])
		self.size = size
		self.alpha = alpha
		self.color = color
		self.m = m

	def add_force(self,force):
		force = np.array(force)
		self.acc = force/self.m
		print(self.vel)
		self.vel = self.vel + self.acc
		self.acc *= 0
		self.pos = self.pos + self.vel
		
	def show(self,clear=True,show=False,filename=False):
		if(clear): plt.cla(); plt.cfg()
		x,y = self.pos[0],self.pos[1]
		plt.scatter(x,y,s=self.size,c=self.color,alpha=self.alpha)
		if(filename): plt.savefig(filename)
		if(show): plt.show()
		return plt




x,y = np.linspace(0,2,10),np.linspace(0,2,10)
plt.plot(x,y)
pos = [0,2]
e = Particle(size=.5,color='r',pos=pos)
e.show(clear=False,filename='move.jpg')

t = np.linspace(0,10,100)
g = [0,10]
filenames = []
for i in range(len(t)):
	plt.plot(x,y,c='white')
	e.add_force(g)
	filename = f'gif/plot{i}.jpg'
	filenames.append(filename)
	e.show(clear=False,filename=filename)
	print(f'[{i}/{len(t)} {round(i/len(t)*100,2)}%]')
	
