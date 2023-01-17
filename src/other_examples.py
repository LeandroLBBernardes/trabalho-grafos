from graph import GraphRepresentation
import time
import sys

#para rodar os exemplos basta fazer a chamada aos métodos e digitar python src/other_examples.py
def RemoveEdgeExample():
    g = GraphRepresentation(3)
    g.AddEdge(0,1)
    g.AddEdge(1,2)
    g.AddEdge(2,0)

    g.ShowGraph()
    g.RemoveEdge(2,0)
    g.ShowGraph()

def VerticesNameExample():
    g = GraphRepresentation(3)
    g.AddEdge(0,1)
    g.AddEdge(1,2)
    g.AddEdge(2,0)

    g.ShowGraph()
    g.SetVertexName(1,'A')
    g.ShowGraph()
    g.SetVerticesName()
    g.ShowGraph()

def AdjacencyListExample():
    g = GraphRepresentation(3)
    g.AddEdge(0,1)
    g.AddEdge(1,2)
    g.AddEdge(2,0)

    g.ShowAdjacencyList()
    g.ShowGraph()

def AdjacencyMatrixExample():
    g = GraphRepresentation(3)
    g.AddEdge(0,1)
    g.AddEdge(1,2)
    g.AddEdge(2,0)

    g.ShowAdjacencyMatrix()
    g.ShowGraph()