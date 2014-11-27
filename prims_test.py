from migraph import MiGraph
from mst import prims

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
         ('e', 'c', 3)]
vertices = ['a', 'b', 'c', 'd', 'e']
g = MiGraph()

g.add_vertices(vertices)
g.add_edges(edges)

res = prims(g, 3)
print(res.vertices())
print(res.edges())

