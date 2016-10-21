import sys
from igraph import *

def getWeight(currentV, nextV):
	for adj in currentV.adjacencias:
		if nextV.label == adj:
			return currentV.distance + nextV.distance #esse negocio ta errado, rever

	return sys.maxsize

def min(vertices, v):
	distance = sys.maxsize

	for adj in v:
		u = vertices[adj]

		if u.distance < distance:
			distance = u.distance
			best = u

	return best #se for tudo igual tem que retornar random



def Prim(vertices, inicial):
	u = list(vertices)
	t = []
	
	v = u.pop(inicial)
	v.distance = 0

	for ver in u:
		ver.distance = getWeight(v, ver)

	while not u.isEmpty():
		# ache um vértice w tal que L(w) = min {L(v)| v  V-V´}; <--- fazer essa parte
		for adj in v.adjacencias:
			nextVertice = vertices[adj]
			newCost = getWeight(v, nextVertice)

			if newCost < 

