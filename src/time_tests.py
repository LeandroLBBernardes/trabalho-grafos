from graph import GraphRepresentation
import time
import sys

sys.setrecursionlimit(200000000)

#metodos utilizados para testar o tempo computacional
#para rodar basta digitar no terminal: python src/time_tests.py
def Timer100Naive(): 
    g = GraphRepresentation(100)
    for i in range(g.GetAmountVertices()):
        if i == 99:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryNaive()
    end = time.time()
    return end - start


def Timer100Tarjan(): 
    g = GraphRepresentation(100)
    for i in range(g.GetAmountVertices()):
        if i == 99:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryTarjan()
    end = time.time()
    return end - start


def Timer1000Tarjan(): 
    g = GraphRepresentation(1000)
    for i in range(g.GetAmountVertices()):
        if i == 999:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryTarjan()
    end = time.time()
    return end - start

def Timer1000Naive(): 
    g = GraphRepresentation(1000)
    for i in range(g.GetAmountVertices()):
        if i == 999:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryNaive()
    end = time.time()
    return end - start

def Timer10000Tarjan(): 
    g = GraphRepresentation(10000)
    for i in range(g.GetAmountVertices()):
        if i == 9999:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryTarjan()
    end = time.time()
    return end - start

def Timer10000Naive(): 
    g = GraphRepresentation(10000)
    for i in range(g.GetAmountVertices()):
        if i == 9999:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryNaive()
    end = time.time()
    return end - start

def Timer100000Tarjan(): 
    g = GraphRepresentation(100000)
    for i in range(g.GetAmountVertices()):
        if i == 99999:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryTarjan()
    end = time.time()
    return end - start

def Timer100000Naive(): 
    g = GraphRepresentation(100000)
    for i in range(g.GetAmountVertices()):
        if i == 99999:
            g.AddEdge(i,0)
            continue
        g.AddEdge(i,i+1)

    start = time.time()
    g.FleuryNaive()
    end = time.time()
    return end - start

print('======100 Vertices======')
print('-Tarjan: {0} segundos'.format(Timer100Tarjan()))
print('-Naive: {0} segundos'.format(Timer100Naive()))

print('\n\n======1000 Vertices======')
print('-Tarjan: {0} segundos'.format(Timer1000Tarjan()))
print('-Naive: {0} segundos'.format(Timer1000Naive()))

print('\n\n======10000 Vertices======')
print('-Tarjan: {0} segundos'.format(Timer10000Tarjan()))
print('-Naive: {0} segundos'.format(Timer10000Naive()))

print('\n\n======100.000 Vertices======')
print('-Tarjan: {0} segundos'.format(Timer100000Tarjan()))
print('-Naive: {0} segundos'.format(Timer100000Naive()))