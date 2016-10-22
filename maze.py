# -*- coding: utf-8 -*-
"""
##############################################
acabei o prim, defini as estruturas de dados(ta chatinho de mexer,
buuuut....)
comecei a busca em largura, mas nao deu certo..confundindo criterio de
parada com o algoritmo, tem q ver certinho.

sugestao de teste:
o  o  o
	
o  o  o

o  o  o 	

a primeira coisa q imprime do jeito que tá, são as arestas q tem
já com a arvore gerada por prim, desenha elas no grafico ali, tipo

o--o  o
|	  |
o--o--o
|  |  |
o  o  o 

e vai desenhando o que o algoritmo de visita sugere com algo do tipo
o==o  o
↓	
o==o==o
↓  ↓  ↓
o  o  o 

ah, raw_input() é tipo um scanf, to usanndo pra ir debugando
####################################	


#DONE:
 - gerar matriz "completa"
 - prim - gerar arvore geradora minima
 - DFS
 - BFS

#TODO:
 - Rodar algoritmos n vezes 10 vezes
 - Imprimir bonitinho


- gerar caminho entre vertices de entrada (c) e saida (n)

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
import time
from random import randint
from random import choice
from copy import copy
from igraph import *

# class Stack(object):
# 	def __init__(self, ):
# 		self.stack =[]

# 	def push(self,elem):
# 		self.stack.append(elem)

# 	def pop(self):
# 		return self.stack.pop()

# 	def isEmpty(self):
# 			return len(self.stack) == 0

# class Queue(object):
# 	def __init__(self, ):
# 		self.queue =[]

# 	def push(self,elem):
# 		self.queue.insert(0,elem)

# 	def pop(self):
# 		return self.queue.pop()

# 	def isEmpty(self):
# 		return len(self.queue) == 0


class Maze(object):
	"""docstring for Maze"""
	def __init__(self, n):
		super(Maze, self).__init__()
		self.n = n
		self.start = 0#randint(0,n)
		self.end = 3#randint(n*(n-1) ,(n*n)-1)
		self.vertices = createVertices(n)
		self.edges = createEdges(n)
		self.spt = []
		self.path = []

	####### Imprime labiritno ##############
	def printMaze(self):
		for i in xrange(self.n+2):#*self.n):
			for j in xrange(self.n+2):
				#if
				sys.stdout.write("x")
			print ("")
	
	####### Retorna lista de adjacentes de um vertice ########
	def adjacentVertices(self,vertice):
		#retorna a lista de adjacencias de um vertice do grafo
		adjlist = []
		for e in self.edges:
			if e[0] == vertice:
				adjlist.append(e[1])
			if e[1] == vertice:
				adjlist.append(e[0])
		return set(adjlist)

	######### Retorna lista completa de arestas ##############
	def getAdjList(self,verticesList):
		adjlist = []
		for v in verticesList:
			for e in self.edges:
				if v in e:
					adjlist.append(e)

		return list(set(adjlist))

	################### Algoritmo de Prim ####################	
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
			e = choice(adj)
			if e[0] not in visited :
				visited.append(e[0])
				edges.append(e)
			elif e[1] not in visited:
				visited.append(e[1])
				edges.append(e)

		self.edges = edges

	################### Algoritmo de Busca em Largura ####################	
	def bfs(self):
		visited = []
		q = []
		q.append(self.start)
		visited.append(self.start)
		self.path.append(self.start)

		if self.start != self.end:
			while q:
				v = q.pop(0)
				for adj in self.adjacentVertices(v):
					if adj not in visited:
						visited.append(adj)
						if adj == self.end:
							self.path.append(adj)
							return 
						q.append(adj)
						self.path.append(adj)
					elif adj in q:
						visited.append(adj)
						if adj == self.end:
							self.path.append(adj)
							return
						self.path.append(adj)
		else:
			self.path.append(self.start)

	################### Algoritmo de Busca em Profundidade ####################			
	def profundidade(self, vertice, visitados):
		visitados.append(vertice)
		adjacencias = self.adjacentVertices(vertice)

		if vertice == self.end:
			self.path = copy(visitados)
		
		for adj in adjacencias:
			if adj not in visitados:
				self.profundidade(adj, visitados)

	def dfs(self):
		visitados = []
		v = self.start
		self.path.append(v)

		self.profundidade(v, visitados)
		
		while set(visitados) != set(self.vertices):
			v = set(self.vertices) - set(visitados)
			self.profundidade(v[0], visitados)

	def imprimir(self):
		g = Graph();

		for i in self.vertices:
			g.add_vertices(i)

		g.add_edges(self.edges)

		print g

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

		else:
			edges.append((i,i+1))
			edges.append((i,n+i))
	return edges

def main(args):
	sys.setrecursionlimit(1000000) #sem isso ele fala que o nivel de recursao para o busca em profundidade atingiu o maximo
	#porem quando passa de 500 ele quebra
	n = [10, 50, 100]

	m = Maze(2)
	m.prim()
	m.imprimir()
	m.bfs()
	print m.path

	###### Roda algoritmo de Prim com Busca em Largura
	# for i in n:
	# 	tempo = 0
	# 	for j in range(0, 10):
	# 		m = Maze(i)
	# 		inicio = time.clock()
	# 		m.prim()
	# 		m.bfs()
	# 		fim = time.clock()
	# 	tempo = tempo + (fim - inicio)
	# 	print "Media de tempo gasto (Algoritmo de Prim) para N =", i
	# 	print "t=", tempo

	
	###### Roda algoritmo de Busca em Profundidade
	# for i in n:
	# 	tempo = 0
	# 	for j in range(0, 10):
	# 		m = Maze(50)
	# 		inicio = time.clock()
	# 		m.dfs()
	# 		fim = time.clock()
	# 		tempo = tempo + (fim - inicio)
	# 	print "Media de tempo gasto (Algoritmo de Busca em Profundidade) para N =",i
	# 	print "t=", tempo/i

if __name__ == '__main__':
	main(sys.argv)