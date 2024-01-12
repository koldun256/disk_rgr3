import numpy as np
import time
from random import randint

def random_weight():
    return randint(-5, 10)

def get_edge(edges, source, dest):
    for s, d, w in edges:
        if s == source and d == dest:
            return w
    return np.inf

def random_graph(n):
    edges = []
    for i in range(n - 1):
        edges.append((i, i + 1, random_weight()))
    for i in range(n):
        for _ in range(3):
            source = i
            dest = randint(n)
            w = random_weight()
            if get_edge(edges, source, dest) == np.inf:
                edges.append((source, dest, w))
    return edges

start = time.perf_counter()
edges = [
    (0, 2, 0),
    (0, 7, 0),
    (0, 9, -2),
    (0, 11, -1),
    (1, 11, 1),
    (2, 1, 0),
    (2, 11, 7),
    (2, 14, 7),
    (3, 1, 10),
    (3, 6, 5),
    (3, 8, 9),
    (3, 11, 5),
    (3, 13, 8),
    (4, 0, 10),
    (4, 3, -2),
    (4, 7, 10),
    (4, 8, 1),
    (4, 12, 8),
    (5, 1, 9),
    (5, 2, 1),
    (5, 4, 1),
    (5, 9, 4),
    (5, 14, 7),
    (6, 4, 1),
    (6, 9, 5),
    (7, 0, 9),
    (7, 8, 9),
    (7, 11, 4),
    (7, 13, 5),
    (8, 1, 4),
    (8, 7, 7),
    (9, 0, 4),
    (9, 1, -2),
    (9, 5, 3),
    (9, 10, 10),
    (9, 14, 7),
    (10, 3, -3),
    (10, 4, 4),
    (10, 6, 1),
    (10, 11, 7),
    (10, 13, 7),
    (11, 3, 6),
    (11, 7, 6),
    (11, 12, -3),
    (12, 7, 10),
    (12, 9, 9),
    (12, 10, 8),
    (13, 2, -3),
    (13, 3, 10),
    (13, 5, 4),
    (13, 8, -2),
    (13, 12, 10),
    (14, 0, 9),
    (14, 4, -1),
    (14, 7, 9)
]

def BellmanFord(edges, source, N):
    d = [np.inf] * N
    d[source] = 0
    # compute distances
    for i in range(N - 1):
        for v1, v2, w in edges:
            d[v2] = min(d[v1] + w, d[v2])
    # detect negative cycles
    for v1, v2, w in edges:
        if d[v1] + w < d[v2]:
            raise Exception("Negative cycle")

    return d

d = BellmanFord(edges, 0, 15)
print(d)
print(d[14])

print((time.perf_counter() - start) * 1000)