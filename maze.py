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
    o-o-o
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




def createVertices(n):
	vertices = []
	for i in xrange(n*n):
		v = Vertice(i)
		vertices.append(v)
	return vertices
"""

import sys
from random import randint
from random import choice
from copy import copy

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
		vertices.append(i)
	return vertices

def createEdges(n):
	edges = []
	countColumn = 0
	countLine = 0
	
	for i in xrange(n*n):
		countColumn += 1

		if i == 0:
			edges.append((i,i+1))
			edges.append((i,n))

		elif countLine == n-1:
			if (i+1 < n*n):
				edges.append((i,i+1))

		elif countColumn == n:
			edges.append((i,n+i))
			countColumn = 0
			countLine += 1


		elif i % n != 0:
			edges.append((i,i+1))
			edges.append((i,n+i))

		else:
			edges.append((i,i+1))
			edges.append((i,n+i))
	return edges
	

class Maze(object):
	"""docstring for Maze"""
	def __init__(self, n):
		super(Maze, self).__init__()
		self.n = n
		self.start = 0#randint(0,n)
		self.end = 8#randint( n*(n-1) ,(n*n)-1)
		self.vertices = createVertices(n)
		self.edges = createEdges(n)
		self.spt = []
		self.path = []
		
		
	
	def adjacentVertices(self,vertice):
		#retorna a lista de adjacencias de um vertice do grafo
		adjlist = []
		for e in self.edges:
			if e[0] == vertice:
				adjlist.append(e[1])
			if e[1] == vertice:
				adjlist.append(e[0])
		return adjlist
	

	#provavelmente n vai precisar, mas taí 
	def getCompleteAdjList(self):
		adjlist = []
		for i in xrange(self.n*self.n):
			a = self.adjacent(self.vertices[i])
			adjlist.append(a)
		return adjlist

	def getAdjList(self,verticesList):
		adjlist = []
		for v in verticesList:
			for e in self.edges:
				if v in e:
					adjlist.append(e)

		#print adjlist
		#print list(set(adjlist))
		#raw_input()
		return list(set(adjlist))


	def prim(self):
		edges = []
		visited = []
		toVisit = copy(self.vertices)

		v = self.start
		visited.append(v)
		while set(self.vertices) != set(visited):
			adj = self.getAdjList(visited)
			for a in adj:
				if a[0] in visited and a[1] in visited:
					adj.remove(a)
			print adj
			e = choice(adj)
			print e
			w = e[1]
			if w not in visited:
				visited.append(w)
				edges.append(e)
		print edges
		

			
###################################################			
	def profundidade(vertice, visitados):
		adjacencias =  adjacent(vertice)
		visitados.append(vertice)
		
		for adj in adjacencias:
			if adj not in visitados:
				profundidade(adj)
			
	def DFS(self):
		visitados = []
		
		visitados.append(self.start)
		
		while len(visitados) < self.n:
			profundidade(self.start, visitados)
		

#v é o vertice, i é o indice do vertice e visitados é a lista de vertices visitados

			

def main(args):
	n = 3
	v = createVertices(n)
	e = createEdges(n)
	m = Maze(n)
	m.prim()

	
	
	#print v
	#print e


if __name__ == '__main__':
	main(sys.argv)