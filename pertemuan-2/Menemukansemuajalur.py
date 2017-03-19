def temukan_semua_jalur(self, awal_vertex, akhir_vertex, jalur=[]):
    """menemukan semua jalur dari awal_vertex ke
    akhir_vertex didalam graph"""
    graph = self.__graph_dict
    jalur = jalur + [awal_vertex]
    if awal_vertex == akhir_vertex:
        return [jalur]
    if awal_vertex not in graph:
        return []
    jalurs = []
    for vertex in graph[awal_vertex]:
        if vertex not in jalur:
            extended_jalurs = self.temukan_semua_jalur(vertex, akhir_vertex, jalur)
            for p in extended_jalurs:
                jalurs.append(p)
    return jalurs


g = {"a" : ["d", "f"],
     "b" : ["c"],
     "c" : ["b", "c", "d", "e"],
     "d" : ["a", "c"],
     "e" : ["c"],
     "f" : ["d"]
     }


a = input('awal vertex = ')
b = input('akhir vertex = ')
print('Semua jalur dari vertex ' + a + ' ke vertex ' + b + ':')
path = graph.temukan_semua_jalur(g, a, b)
print(path)