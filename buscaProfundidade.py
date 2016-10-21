import sys
from igraph import *
#from ceso import beleza

def nextZero(vertices):
	for v in vertices:
		if v.indice == 0:
			return v

	return None

def PBP(vertices, v, i, f, final, caminho):
	v.indice = i
	i = i + 1
	adjacencias = v.adj

	for u in adjacencias:
		v = vertices(u)
		
		if v.indice == 0:
			if v.label == final:
				caminho = list(f)

			f.append(v)
			PBP(vertices, v, i, f)

def buscaProfundidade(vertices, inicial, final):
	i = 1
	f = []
	caminho = []

	for v in vertices:
		v.indice = 0

	v = vertices[inicial]

	while v != None:
		PBP(vertices, v, i, f, final, caminho)
		v = nextZero(vertices);

	return caminho