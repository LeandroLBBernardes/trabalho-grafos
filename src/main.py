from graph import GraphRepresentation
import time
import sys

sys.setrecursionlimit(200000000)

def FleuryTarjanExample() -> None:
    g = GraphRepresentation(7)
    g.AddEdge(0,1)
    g.AddEdge(0,2)
    g.AddEdge(1,2)
    g.AddEdge(2,3)
    g.AddEdge(3,1)
    g.AddEdge(1,4)
    g.AddEdge(3,4)
    g.AddEdge(4,5)
    g.AddEdge(3,5)
    g.AddEdge(2,5)
    g.AddEdge(4,6)
    g.AddEdge(5,6)

    g.ShowGraph()
    print(g.FleuryTarjan())



def FleuryNaiveExample() -> None:
    g = GraphRepresentation(6)
    g.AddEdge(0,1)
    g.AddEdge(0,2)
    g.AddEdge(1,2)
    g.AddEdge(2,3)
    g.AddEdge(3,1)
    g.AddEdge(1,4)
    g.AddEdge(3,4)
    g.AddEdge(4,5)
    g.AddEdge(3,5)
    g.AddEdge(2,5)

    g.ShowGraph()
    print(g.FleuryNaive())

#Caso queira testar a biblioteca aproveite o método main
#Mais explicações se encontram no vídeo gravado e no relatório escrito
def main() -> None:
    
    FleuryTarjanExample() #printa o caminho euleriano usando Tarjan para verificar pontes
    FleuryNaiveExample() #printa o caminho euleriano usando Naive para verificar pontes

    return 0
    
if __name__ == '__main__':
    main()