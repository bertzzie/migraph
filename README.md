Representasi Graph dengan Adjecent List
---------------------------------------

Representasi sederhana graph dengan menggunakan adjacent list.

Contoh penggunaan:

    from migraph import MiGraph

    graph = MiGraph()
    graph.add_vertices(['a', 'b', 'c'])
    graph.add_edges(('a', 'b', 2), ('a', 'c', 3))

Contoh penelusuran:

    vx  = graph.get_vertices()
    ns  = graph.get_neighbour(vx[0])
    ns1 = graph.get_neighbour(ns[0])

Untuk sekarang hanya bisa merepresentasikan *weighted graph* searah.
