class Graph():
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for (i, j) in self.edges:
            if i in self.graph_dict.keys():
                self.graph_dict[i].append(j)
            else:
                self.graph_dict[i] = [j]
        
        print(self.graph_dict)

    def get_paths(self, start, end, path = []):
        path = path + [start] 

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
            
        return paths
    
    def get_shortestpaths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return []
        paths = []
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortestpaths(node, end, path)

            if shortest_path is None or len(shortest_path) > len(sp):
                shortest_path = sp

        return shortest_path


# M is Mumbai, P is Paris , N is nweyork , D is dubai, T is Toronto
routes = [("M", "D"), 
          ("M", "P"), 
          ("P", "D"), 
          ("P", "N"), 
          ("D", "N"), 
          ("N", "T")]

graph_dc = Graph(routes)

print(graph_dc.get_paths("M", "N"))
print(graph_dc.get_shortestpaths("M", "N"))
