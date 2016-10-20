# -*- coding: utf-8 -*-
"""

- gerar matriz "completa"
- gerar arvore geradora minima
- gerar caminho entre vertices de entrada (c) e saida (n)

Os valores para n são: 10, 50, 100, 500, 1000. Para cada
valor de n um mı́nimo de 10 execuções são necessárias

Os valores para n são: 10, 50, 100, 500, 1000. Para cada
valor de n um mı́nimo de 10 execuções são necessárias e, junto com os resultados
individuais, mostrar a média dos tempos.

------------
classes:
maze(?) completa (ou grafo)

0
i i+1 n-1

	o-o-o
	| | | |
n	o-o-o
	| | | |
	o-o-o

"""

import sys
from igraph import *
#from random import rand

def createVertices(n):
	vertices = []
	for i in xrange(n*n):
		vertices.append(i)
	return vertices

def createEdges(n):
	edges = []
	countColumn = 0
	countLine = 0
	
	for i in xrange(n*n):
		countColumn += 1

		if i == 0:
			print(i,i+1) , "," , (i,n+i)

		elif countLine == n-1:
			if (i+1 < n*n):
				print (i,i+1)

		elif countColumn == n:
			print (i, n+i)
			countColumn = 0
			countLine += 1


		elif i % n != 0:
			print(i,i+1) , "," , (i,n+i)

		else:
			print (i,i+1) , "," , (i, n+i)

		
	#print edges

class Maze(object):
	"""docstring for Maze"""
	def __init__(self, n):
		super(Maze, self).__init__()
		self.n = n
		self.edges = []
		self.vertices = []
		self.path = []
		self.start = 0
		self.end = 0
		


def main(args):
	v = createVertices(10)
	createEdges(3)




if __name__ == '__main__':
	main(sys.argv)