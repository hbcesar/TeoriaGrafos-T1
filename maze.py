# -*- coding: utf-8 -*-
import sys
import time
from random import randint
from random import choice
from copy import copy
from heapq import heappop, heappush
# from igraph import *

class Stack(object):
	def __init__(self):
		self.stack =[]

	def push(self,elem):
		self.stack.append(elem)

	def pop(self):
		return self.stack.pop()

	def isEmpty(self):
			return len(self.stack) == 0

class Queue(object):
	def __init__(self, ):
		self.queue =[]

	def push(self,elem):
		self.queue.insert(0,elem)

	def pop(self):
		return self.queue.pop()

	def isEmpty(self):
		return len(self.queue) == 0

class Vertice(object):
	def __init__(self, i):
		super(Vertice, self).__init__()
		self.i = i
		self.edges = []

class Maze(object):
	"""docstring for Maze"""
	def __init__(self, n):
		super(Maze, self).__init__()
		self.n = n
		self.start = randint(0,n)
		self.end = randint(n*(n-1) ,(n*n)-1)
		self.vertices = self.createVertices()
		self.createEdges()
		self.path = []
		self.edges = []

	############## Funcoes para criacao da malha ############
	def createVertices(self):
		n = self.n
		vertices = []
		for i in xrange(n*n):
			v = Vertice(i)
			vertices.append(v)
		return vertices

	def createEdges(self):
		countColumn = 0
		countLine = 0
		n = self.n

		for i in xrange(n*n):
			countColumn += 1

			if countLine == n-1:
				if (i+1 < n*n):
					self.vertices[i].edges.append((i, i+1))
					self.vertices[i+1].edges.append((i+1, i))

			elif countColumn == n:
				self.vertices[i].edges.append((i, n+i))
				self.vertices[n+i].edges.append((n+i, i))
				countColumn = 0
				countLine += 1

			else:
				self.vertices[i].edges.append((i, i+1))
				self.vertices[i+1].edges.append((i+1, i))
				self.vertices[i].edges.append((i, n+i))
				self.vertices[n+i].edges.append((n+i, i))



	################### Funcoes de manutencao de listas ####################	
	#atualiza lista de adjacencias de cada vertices
	def updateEdges(self, tree):
		self.edges = tree

		for v in self.vertices:
			v.edges = []

		for v, k in tree:
			self.vertices[v].edges.append((v, k))
			self.vertices[k].edges.append((k, v))

	def pathfinder(self, parentMap):
		path = []

		#percorre o mapa de traz pra frente gerando o caminho
		curr = self.end
		while curr != self.start:
			path.insert(0, curr)
			curr = parentMap[curr]
		path.insert(0, self.start)

		#copia o caminho para variavel da classe
		self.path = copy(path)

	#retorna lista de vertices adjacentes a um dado vertice
	def adjacentes(self, vertice):
		adjlist = []
		vertice = self.vertices[vertice]

		for e in vertice.edges:
			if e[0] == vertice.i:
				adjlist.append(e[1])
			if e[1] == vertice.i:
				adjlist.append(e[0])
		return set(adjlist)


	################### Algoritmo de Prim ####################	
	def addToEdge(self, vertice, edges):
		for adj in self.adjacentes(vertice):
			edges.append((vertice, adj))

	def prim(self):
		maze = []
		edges = []
		tree = []
		start = self.vertices[self.start]
		start = start.i
		maze.append(start)

		for adj in self.adjacentes(start):
			edges.append((start, adj))

		while edges:
			e = choice(edges)
			edges.remove(e)

			if e[0] not in maze:
				maze.append(e[0])
				tree.append(e)
				self.addToWall(e[0], edges)
			elif e[1] not in maze:
				maze.append(e[1])
				tree.append(e)
				self.addToWall(e[1], edges)

		self.updateEdges(tree)

	################### Algoritmo de Busca em Largura ####################	
	def bfs(self):
		# listas auxiliares
		queue = Queue()
		visited = []
		parentMap = {}

		# insere o primeiro caminho na lista
		queue.push(self.start)
		visited.append(self.start)

		while not queue.isEmpty():
			# pega o no da fila
			node = queue.pop()

			# pega as adjacencias do nó e insere na fila
			for adj in self.adjacentes(node):
				if adj not in visited:
					queue.push(adj)
					visited.append(adj)
					parentMap[adj] = node

		self.pathfinder(parentMap)

	

	################### Algoritmo de Busca em Profundidade ####################
	def dfs_iterativo(self):
		stack = Stack()

		#lista de visitados
		visited = []

		#adiciona primeiro vertice a pilha
		start = self.vertices[self.start]
		# start = start.i
		stack.push(start)

		#dicionario para manter caminho para o vertice alvo
		parentMap = {}

		#nova lista de adjacencias
		edges = []		

		while not stack.isEmpty():
			#pega primeiro da pilha
			parent = stack.pop()
			parent = parent.i
			
			#se ja tiver sido visitado, nao faz nada
			if parent in visited:
				continue

			#marca que o vertice alvo esta na arvore (evitar erros)
			if parent == self.end:
				found = True

			#marca o vertice como visitado
			visited.append(parent)
			children = self.adjacentes(parent)

			#adiciona na pilha (e no mapa de caminhos)
			for child in children:
				stack.push(self.vertices[child])

				#atualiza lista de pais caso ainda nao houver
				if child not in parentMap:
					parentMap[child] = parent

		#endwhile

		#se o vertice foi encontrado, gera caminho até ele
		if found:
			self.pathfinder(parentMap)

		#deleta a raiz do mapa de pais pois ela nao tem um pai
		del parentMap[self.start]

		#gera e atualiza nova lista de adjacencias
		for parent, child in parentMap.iteritems():
			edges.append((parent, child))
		self.edges = edges

	###### imprime grafico bonitinho ##########
	def imprimir(self):
		g = Graph();

		for v in self.vertices:
			g.add_vertices(v.i)

		g.add_edges(self.edges)

		print g



def main(args):
	# n = [10, 50, 100]#, 500, 1000]
	n = [500, 1000]

	###### Roda algoritmo de Prim com Busca em Largura
	for i in n:
		tempo = 0
		for j in range(0, 10):
			m = Maze(3)
			inicio = time.clock()
			m.prim()
			m.bfs()
			fim = time.clock()
			tempo = tempo + (fim - inicio)
		tempo = tempo/3
		print i, tempo


	###### Roda algoritmo de Busca em Profundidade
	for i in n:
		tempo = 0
		for j in range(0, 10):
			m = Maze(i)
			inicio = time.clock()
			m.dfs_iterativo()
			fim = time.clock()
			tempo = tempo + (fim - inicio)
		print i, tempo

if __name__ == '__main__':
	main(sys.argv)