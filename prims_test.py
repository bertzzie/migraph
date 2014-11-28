from migraph import MiGraph
from mst import prims
from mst import kruskal
import random

edges = [('a', 'e', 1),
         ('a', 'b', 3),
         ('b', 'a', 3),
         ('b', 'e', 2),
         ('b', 'c', 9),
         ('b', 'd', 2),
         ('c', 'b', 9),
         ('c', 'e', 7),
         ('c', 'd', 3),
         ('d', 'b', 2),
         ('d', 'c', 3),
         ('e', 'a', 1),
         ('e', 'b', 2),
         ('e', 'c', 7)]
vertices = ['a', 'b', 'c', 'd', 'e']
g = MiGraph()

g.add_vertices(vertices)
g.add_edges(edges)

res = prims(g, random.randint(0, len(vertices)-1))
krs = kruskal(g)

print(res.vertices())
print(res.edges())

print(krs)
