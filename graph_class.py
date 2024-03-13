from collections import defaultdict

class Graph:
 
    # Constructor
    def __init__(self, map, bridges, islands, empty):
 
        # Default dictionary to store graph
        if empty:
            self.graph = []
            self.all_bridges = bridges
            self.bridges = []
        else:
            self.graph = build_graph(map, bridges, islands)
            self.bridges = bridges
    
    def add_edge(self, direction, number, island):
        bridges = get_bridges_with_island(island, self.all_bridges)
        simple_list =[]
        for bridge in bridges:
            if direction == "up":
                if bridge['direction'] == 'vert' and bridge['ends_at'] == island:
                    simple_list.append((bridge['starts_at'], bridge['ends_at']))
            elif direction == "down":
                if bridge['direction'] == 'vert' and bridge['starts_at'] == island:
                    print("found bridge")
                    simple_list.append((bridge['starts_at'], bridge['ends_at']))
            elif direction == "right":
                if bridge['direction'] == 'horiz' and bridge['starts_at'] == island:
                    simple_list.append((bridge['starts_at'], bridge['ends_at']))
            elif direction == "left":
                if bridge['direction'] == 'horiz' and bridge['ends_at'] == island:
                    simple_list.append((bridge['starts_at'], bridge['ends_at']))
        if self.in_graph(island):
            for adjacency in self.graph:
                if adjacency['coordinates'] == island:
                    adjacency['bridges'] += (simple_list)
        else:
            adjacency = {'coordinates': island, 'bridges': simple_list}
            self.graph.append(adjacency)
    def in_graph(self, island):
        for adjacency in self.graph:
            if adjacency['coordinates'] == island:
                return True
        return False

def get_bridges_with_island(island, bridges):
    print(island)
    print(bridges)
    matching_bridges =[]
    for bridge in bridges:
        if bridge['starts_at'] == island or bridge['ends_at'] == island:
            matching_bridges.append(bridge)
    return matching_bridges

    # solve_hashi(bridges, map)
def build_graph(map, bridges, islands):
    graph = []
    for island in islands:
        all_bridges = get_bridges_with_island(island['coordinates'], bridges)
        simple_list = []
        for bridge in all_bridges:
            simple_list.append((bridge['starts_at'], bridge['ends_at']))
        adjacency = {'coordinates': island['coordinates'], 'bridges': simple_list}
        graph.append(adjacency)
    return graph


