# -*- coding: utf-8 -*-
"""

- gerar matriz "completa"
- gerar arvore geradora minima
- gerar caminho entre vertices de entrada (c) e saida (n)

Os valores para n são: 10, 50, 100, 500, 1000. Para cada
valor de n um mínimo de 10 execuções são necessárias

Os valores para n são: 10, 50, 100, 500, 1000. Para cada
valor de n um mínimo de 10 execuções são necessárias e, junto com os resultados
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

Prim:
prim(G) # G é grafo
    # Escolhe qualquer vértice do grafo como vértice inicial/de partida
    s ← seleciona-um-elemento(vertices(G))

    para todo v ∈ vertices(G)
        π[v] ← nulo
    Q ← {(0, s)}
    S ← ø

    enquanto Q ≠ ø
        v ← extrair-mín(Q)
        S ← S ∪ {v}

        para cada u adjacente a v
            se u ∉ S e pesoDaAresta(π[u]→u) > pesoDaAresta(v→u)
                Q ← Q \ {(pesoDaAresta(π[u]→u), u)}
                Q ← Q ∪ {(pesoDaAresta(v→u), u)}
                π[u] ← v

    retorna {(π[v], v) | v ∈ vertices(G) e π[v] ≠ nulo}


profundidade :
1  procedure DFS(G,v):
2      label v as discovered
3      for all edges from v to w in G.adjacentEdges(v) do
4          if vertex w is not labeled as discovered then
5              recursively call DFS(G,w)
"""

import sys
from igraph import *
#from random import rand

class Stack(object):
	def __init__(self, ):
		super(Stack, self).__init__()
		self.stack =[]

		def push(elem):
			self.stack.append(elem)

		def pop(self):
			return self.stack.pop()

class Queue(object):
	def __init__(self, ):
		super(Stack, self).__init__()
		self.queue =[]

		def push(elem):
			self.queue.insert(0,elem)

		def pop(self):
			return self.queue.pop()



def createVertices(n):
	vertices = []
	for i in xrange(n*n):
		v = Vertice(i)
		vertices.append(v)
	return vertices

def createEdges(n, vertices):
	edges = []
	countColumn = 0
	countLine = 0
	
	for i in xrange(n*n):
		countColumn += 1

		if i == 0:
			print(i,i+1) , "," , (i,n+i)
			v = vertices[i];
			v.adj.append(i+1)
			v.adj.append(n+i)

		elif countLine == n-1:
			if (i+1 < n*n):
				print (i,i+1)
				v.adj.append(i+1)

		elif countColumn == n:
			print (i, n+i)
			countColumn = 0
			countLine += 1
			v.adj.append(n+i)

		elif i % n != 0:
			print(i,i+1) , "," , (i,n+i)
			v.adj.append(i+1)
			v.adj.append(n+i)

		else:
			print (i,i+1) , "," , (i, n+i)
			v.adj.append(i+1)
			v.adj.append(n+i)

		
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
		
class Vertice(object):
	def __init__(self, label):
		super(Vertice, self).__init__()
		self.label = label
		self.indice = 0
		self.adj = []
		self.distance = sys.maxsize


def main(args):
	v = createVertices(10)
	createEdges(10, v)
	print 


if __name__ == '__main__':
	main(sys.argv)