# -*- coding: utf-8 -*-
"""
#DONE:
- busca em largura OK
- busca em profundidade OK (so nao atualiza lista)
- codigo que executa cada valor 10 vezes OK

#TO DO:
- atualizar lista de adjacencias na busca em profundidade
- mudar prim pra ficar mais eficiente
- ver se há uma forma melhor de imprimir
- lembrar de voltar inicio e fim pra aleatorio

Obs:
- eu sou rolezeira


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

class Stack(object):
	def __init__(self, ):
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


class Maze(object):
	"""docstring for Maze"""
	def __init__(self, n):
		super(Maze, self).__init__()
		self.n = n
		self.start = 0#randint(0,n)
		self.end = 8#randint(n*(n-1) ,(n*n)-1)
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
	def mountmap(self):
		graph = {}

		for v in self.vertices:
			graph[v] = list(self.adjacentVertices(v))

		return graph

	def bfs(self):
		visited = []
		q = Queue()
		q.push(self.start)
		visited.append(self.start)
		self.path.append(self.start)
		found = False

		if self.start != self.end:
			while not q.isEmpty():
				v = q.pop()
				for adj in self.adjacentVertices(v):
					if adj == self.end and not found:
						self.path.extend(q.queue)
						self.path.append(adj)
						found = True

					if adj not in visited:
						visited.append(adj)
						q.push(adj)

				# raw_input()
		else:
			self.path.append(self.start)

	def bfs2(self):
		# cria um dicionario com uma lista de caminhos
		graph = self.mountmap()

		# lista de caminhos
		queue = []

		# insere o primeiro caminho na lista
		queue.append([self.start])

		while queue:
			# pega o primeiro caminho da lista
			path = queue.pop(0)

			# pega o ultimo vertice da lista de caminhos
			node = path[-1]

			# se caminho for encontrado, retorna
			if node == self.end:
				self.path = copy(path)
				return

			# pega todos os caminhos adjacentes ao nó, controi novo caminho e adiciona a fila
			for adjacent in graph.get(node, []):
				new_path = list(path)
				new_path.append(adjacent)
				queue.append(new_path)



	################### Algoritmo de Busca em Profundidade (recursivo) ####################			
	def profundidade(self, vertice, visitados, pilha):
		visitados.append(vertice)
		adjacencias = self.adjacentVertices(vertice)

		pilha.push(vertice)

		if vertice == self.end:
			self.path = copy(pilha.stack)
		
		for adj in adjacencias:
			if adj not in visitados:
				self.profundidade(adj, visitados, pilha)

		pilha.pop()

	def dfs_recursivo(self):
		visitados = []
		pilha = Stack()

		v = self.start
		self.path.append(v)

		self.profundidade(v, visitados, pilha)
		
		while set(visitados) != set(self.vertices):
			v = set(self.vertices) - set(visitados)
			self.profundidade(v[0], visitados, pilha)

	################### Algoritmo de Busca em Profundidade (recursivo) ####################	
	def dfs_iterativo(self):
		stack = Stack()

		#lista de visitados
		visited = []

		#adiciona primeiro vertice a pilha
		stack.push(self.start)

		#dicionario para manter caminho para o vertice alvo
		parentMap = {}
		
		while not stack.isEmpty():
			#pega primeiro da pilha
			parent = stack.pop()
			
			#se ja tiver sido visitado, nao faz nada
			if parent in visited: 
				continue

			#marca que o vertice alvo esta na arvore (evitar erros)
			if parent == self.end:
				found = True

			#marca o vertice como visitado
			visited.append(parent)
			children = self.adjacentVertices(parent)

			#adiciona na pilha (e no mapa de caminhos)
			for child in children:
				stack.push(child)
				parentMap.setdefault(child, []).append(parent)

		#se o vertice foi encontrado, gera caminho até ele
		if found:
			path = []

			#percorre o mapa de traz pra frente gerando o caminho
			curr = self.end
			while curr:
				path.insert(0, curr)
			 	curr = parentMap[curr][0]
			path.insert(0, self.start)

			#copia o caminho para variavel da classe
			self.path = copy(path)

	################### Imprime o labirinto ####################	
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
	n = [10, 50, 100, 500, 1000]

	m = Maze(3)
	m.prim()
	m.dfs_iterativo()
	m.imprimir()
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