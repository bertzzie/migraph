from migraph import MiGraph
from mst import kruskal

vertices = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 5),
    ('A', 'D', 3),
    ('B', 'C', 4),
    ('B', 'D', 2),
    ('C', 'D', 1),
]

g = MiGraph()
g.add_vertices(vertices)
g.add_edges(edges)

mst = kruskal(g)

minimum_spanning_tree = set([
('A', 'B', 1),
('B', 'D', 2),
('C', 'D', 1),
])

# Should print true
print(mst == minimum_spanning_tree)
