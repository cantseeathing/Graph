class Graph:
    def __init__(self, gdict=None):
        if not gdict:
            gdict = {}
        else:
            self.gdict = gdict

    def add_edge(self, vertx, edge):
        self.gdict[vertx].append(edge)


custom_dict = {
    'a': ['b', 'c'],
    'b': ['a', 'd', 'e'],
    'c': ['a', 'e'],
    'd': ['b', 'e', 'f'],
    'e': ['d', 'f'],
    'f': ['d', 'e']
}

graph = Graph(gdict=custom_dict)
print(graph.gdict)
graph.add_edge(vertx='e', edge='c')
print(graph.gdict['e'])


class Graph_Adjacency_List:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ':', self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True
        else:
            return False

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
                return True
            except ValueError:
                return 'No edge between the vertices'
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for other_vertex in self.adjacency_list[vertex]:
                self.adjacency_list[other_vertex].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False


custom_graph = Graph_Adjacency_List()

custom_graph.add_vertex('A')
custom_graph.add_vertex('B')
custom_graph.add_vertex('C')
custom_graph.add_vertex('D')

custom_graph.print_graph()

custom_graph.add_edge('A', 'B')
custom_graph.add_edge('B', 'C')
custom_graph.add_edge('A', 'C')
custom_graph.add_edge('D', 'A')
custom_graph.add_edge('D', 'C')

custom_graph.print_graph()
print('//////////////')
custom_graph.remove_edge('A', 'C')
custom_graph.print_graph()

print('//////////////')
custom_graph.remove_vertex('D')
custom_graph.print_graph()