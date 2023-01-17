import igraph as ig
import matplotlib.pyplot as plt

from igraph import *

class GraphRepresentation():

    def __init__(self, numVertices, isDirected=False) -> None:
        self.isDirected = isDirected
        self.numVertices = numVertices
        self.graph = Graph(n=numVertices,directed=isDirected)
        self.AddVerticesProperties()
        self.AddEdgesProperties()



    def ShowAdjacencyMatrix(self) -> None:
        adjacencyMatrix = self.graph.get_adjacency()
        vertices = self.graph.vs['name']
        verticesList = [vertices[vertice] for vertice in range(self.GetAmountVertices())]
        verticesList = '  '.join(map(str,verticesList))

        print('   {0}'.format(verticesList))
        for index in range(self.GetAmountVertices()):
            print('{0} {1}'.format(vertices[index],adjacencyMatrix[index]))



    def ShowAdjacencyList(self) -> None:
        adjacencyLists = self.graph.get_adjlist()
        vertices = self.graph.vs['name']

        for index in range(self.GetAmountVertices()):
            print('{0} -> {1}'.format(vertices[index],adjacencyLists[index]))

    

    def AddEdge(self,source, target) -> None:
        self.graph.add_edge(source, target)
        id = self.graph.get_eid(source, target, error=False)
        self.graph.es[id]['weight'] = 1
        

    

    def CheckEdge(self,source, target) -> bool:
        if self.graph.get_eid(source, target, error=False) != -1:
            return True
        return False

    

    def CheckVertex(self,vertex) -> bool:
        if vertex in self.graph.vs['name']:
            return True
        return False

    

    def RemoveEdge(self,source, target) -> None:
        edgeIndex = self.graph.get_eid(source, target, error=False)
        if  edgeIndex != -1:
            self.graph.delete_edges([edgeIndex])
        else:
            print('NAO EXISTE TAL ARESTA')

    

    def AddVerticesProperties(self) -> None:
        self.graph.vs['name'] = range(self.graph.vcount())
        self.graph.vs['weight'] = 0

    

    def AddEdgesProperties(self) -> None:
        self.graph.es['name'] = range(self.graph.ecount())
        self.graph.vs['weight'] = 0



    def SetVerticesName(self) -> None:
        for index in range(self.GetAmountVertices()):
            self.graph.vs[index]['name'] = input('Digite o nome do vertice {0}: '.format(index))
    


    def SetVerticesWeight(self) -> None:
        for index in range(self.GetAmountVertices()):
            self.graph.vs[index]['weight'] = int(input('Digite o peso do vertice {0}: '.format(index)))



    def SetEdgesName(self) -> None:
        for index in range(self.GetAmountEdges()):
            edge = self.graph.es[index]
            edge['name'] = input('Digite o nome da aresta ({0},{1}): '.format(edge.source,edge.target))



    def SetEdgesWeight(self) -> None:
        for index in range(self.GetAmountEdges()):
            edge = self.graph.es[index]
            edge['weight'] = int(input('Digite o peso da aresta ({0},{1}): '.format(edge.source,edge.target)))



    def ShowVertices(self) -> None:
        vertices = self.graph.vs['name']
        vertices = [vertices[vertice] for vertice in range(self.GetAmountVertices())]
        print('Vertices = {0}'.format(vertices))
    


    def GetVertices(self) -> list:
        vertices = self.graph.vs['name']
        vertices = [vertices[vertice] for vertice in range(self.GetAmountVertices())]
        return vertices



    def ShowEdges(self) -> None:
        edges = self.graph.es['name']
        edges = [edges[edge] for edge in range(self.GetAmountEdges())]
        print('Arestas = {0}'.format(edges))
    


    def GetEdges(self) -> list:
        edges = self.graph.es['name']
        edges = [edges[edge] for edge in range(self.GetAmountEdges())]
        return edges



    def SetVertexName(self, vertex, name) -> None:
        self.graph.vs[vertex]['name'] = name



    def SetVertexWeight(self, vertex, weight) -> None:
        self.graph.vs[vertex]['weight'] = weight
    


    def SetEdgeName(self, edge, name) -> None:
        self.graph.vs[edge]['name'] = name
    


    def SetEdgeWeight(self, edge, weight) -> None:
        self.graph.vs[edge]['weight'] = weight
    


    def GetAmountVertices(self) -> int:
        return self.graph.vcount()

    

    def GetAmountEdges(self) -> int:
        return self.graph.ecount()

    

    def IsEmpty(self) -> bool:
        if self.GetAmountEdges() == 0:
            return True
        return False 

    

    def IsFull(self) -> bool:
        vertices = self.GetAmountVertices()
        degree = vertices*(vertices-1)
        kedges = degree/2
        if self.GetAmountEdges() == kedges and self.graph.is_simple():
            return True
        return False

    

    def IsAdjacentVertices(self, v1,v2) -> bool:
        return self.graph.are_connected(v1, v2)

    

    def IsAdjacentEdges(self, source1, target1, source2, target2) -> bool:
        edge1 = self.graph.get_eid(source1, target1)
        edge2 = self.graph.get_eid(source2, target2)
        edge1 = self.graph.es[edge1]
        edge2 = self.graph.es[edge2]
        if self.isDirected:
            if edge1.target == edge2.target:
                return True
        else:
            if edge1.target == edge2.target or edge1.source == edge2.source:
                return True
            if edge1.target == edge2.source or edge1.source == edge2.target:
                return True
        return False

    

    def ExportGraphGML(self,name='graph') -> None:
        self.graph.save('{0}.gml'.format(name))

    

    def ImportGraphGML(self, path) -> None:
        self.graph = Graph.Load(path, format='gml')

    

    def CreateFullGraph(self,numVertices,isDirected=False) -> None:
        self.graph = Graph.Full(numVertices,isDirected)
        self.AddVerticesProperties()
        self.AddEdgesProperties()



    def IsBridgeTarjan(self, v1, v2) -> bool:
        bridges = self.BridgesTarjanAlgorithm()
        if (v1,v2) in bridges:
            return True
        return False



    def IsBridgeNaive(self, v1, v2) -> bool:
        bridges = self.BridgesNaiveAlgorithm()
        if (v1,v2) in bridges:
            return True
        return False

    

    def ShowGraph(self) -> None:
        fig, ax = plt.subplots(figsize=(5,5))
        ig.plot(
            self.graph,
            target=ax,
            layout="circle", #print nodes in a circular layout
            vertex_size=0.2,
            vertex_color=["white"],
            vertex_frame_width=1.0,
            vertex_frame_color="black",
            vertex_label=self.graph.vs['name'],
        )
        plt.show()



    #<editor-fold desc="Tarjan">
    def DFSTarjan(self, source, disc, low, parent, bridges, time, adj_list) -> None:
        disc[source] = time
        low[source] = time
        time += 1
        for target in adj_list[source]:
            if disc[target] == -1:
                parent[target] = source
                self.DFSTarjan(target, disc, low, parent, bridges, time, adj_list)
                low[source] = min(low[source], low[target])
                if low[target] > disc[source]:
                    bridges.append((source, target))
            elif target != parent[source]:
                low[source] = min(low[source], disc[target])



    def BridgesTarjanAlgorithm(self) -> list:
        graph = self.graph.copy()
        adjList = graph.get_adjlist()
        numVertices = graph.vcount()
        disc = [-1] * numVertices
        low = [-1] * numVertices
        parent = [-1] * numVertices
        time = 0
        bridges = []
        for indexVertice in range(numVertices):
            if disc[indexVertice] == -1:
                self.DFSTarjan(indexVertice, disc, low, parent, bridges, time, adjList)
        return bridges
    #</editor-fold>



    #<editor-fold desc="Naive">
    def BridgesBFSAlgorithm(self) -> None:
        adjList = self.graph.get_adjlist()
        bridges = []
        for v1 in range(self.GetAmountVertices()):
            for v2 in adjList[v1]:
                components = len(self.graph.components())
                self.RemoveEdge(v1,v2)
                aux = len(self.graph.components())
                if aux > components:
                    bridges.append((v1,v2))
                self.AddEdge(v1,v2)
        bridges = self.RemoveDuplicateEdge(bridges)
        return bridges



    def RemoveDuplicateEdge(self,bridges) -> list:
        remove = []
        for i in range(len(bridges)):
            for j in range(i+1, len(bridges)):
                if bridges[i][0] == bridges[j][1] and bridges[i][1] == bridges[j][0]:
                    remove.append(bridges[j])
        for i in remove:
            for j in bridges:
                if i == j:
                    bridges.remove(i)
        bridges.reverse()
        return bridges
    #</editor-fold>



    #<editor-fold desc="Naive">
    def DFSNaive(self, v, visited,bridges) -> list:
        visited.add(v)
        for neighbour in self.graph.get_adjlist()[v]:
            if neighbour not in visited:
                components = len(self.graph.components())
                auxGraph = self.graph.copy()
                edgeId = auxGraph.get_eid(v, neighbour, error=False)
                auxGraph.delete_edges([edgeId])
                aux = len(auxGraph.components())
                if aux > components:
                    bridges.append((v,neighbour))
                self.DFSNaive(neighbour, visited,bridges)


 
    def BridgesNaiveAlgorithm(self) -> list:
        visited = set()
        bridges = []
        for i in self.GetVertices():
            if i not in visited:
                self.DFSNaive(i, visited, bridges)
        return bridges
    #</editor-fold>



    #<editor-fold desc="Fleury Tarjan">
    def FleuryTarjan(self,source=0) -> list:
        eulerTourList = []
        for vertex in range(self.graph.vcount()):
            if self.graph.vs[vertex].degree() % 2 != 0 :
                source = vertex
                break
        self.__printEulerUtil(source,eulerTourList)
        return eulerTourList
    


    def __printEulerUtil(self,source,eulerTourList) -> None:
        for target in self.graph.get_adjlist()[source]:
            if self.__isValidNextEdgeTarjan(source,target) and self.GetAmountEdges() != 0:
                eulerTourList.append((source,target))
                self.RemoveEdge(source, target)
                self.__printEulerUtil(target,eulerTourList)



    def __isValidNextEdgeTarjan(self, source, target) -> None:
        if len(self.graph.get_adjlist()[source]) == 1:
            return True
        else:
            normal = (source,target) not in self.BridgesTarjanAlgorithm()
            inverse = (target,source) not in self.BridgesTarjanAlgorithm()
            return normal and inverse
    #</editor-fold>
    


    #<editor-fold desc="Fleury Naive">
    def FleuryNaive(self,source=0) -> list:
        eulerTourList = []
        for vertex in range(self.GetAmountVertices()):
            if self.graph.vs[vertex].degree() % 2 != 0 :
                source = vertex
                break
        self.__printEulerUtilNaive(source,eulerTourList)
        return eulerTourList

    

    def __printEulerUtilNaive(self,source,eulerTourList) -> None:
        for target in self.graph.get_adjlist()[source]:
            if self.__isValidNextEdgeNaive(source,target) and self.GetAmountEdges() != 0:
                eulerTourList.append((source,target))
                self.RemoveEdge(source, target)
                self.__printEulerUtilNaive(target,eulerTourList)

    

    def __isValidNextEdgeNaive(self, source, target) -> None:
        if len(self.graph.get_adjlist()[source]) == 1:
            return True
        else:
            normal = (source,target) not in self.BridgesNaiveAlgorithm()
            inverse = (target,source) not in self.BridgesNaiveAlgorithm()
            return normal and inverse
    #</editor-fold>


    
    def Duplicate(self,bridges) -> list:
        aux = []
        for (source,target) in bridges:
            aux.append((target,source))
        aux = [*bridges, *aux]
        return aux