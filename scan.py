#************************************************************
#   scan_print_map.py
#   Scan a hashi puzzle from stdin, store it in a numpy array,
#   and print it out again.
#
import numpy as np
import sys

from graph_class import Graph

def main():
    code = ".123456789abc"
    nrow, ncol, map = scan_map()
    print("this is ur hashi")
    for r in range(nrow):

        for c in range(ncol):
            print(code[map[r][c]],end="")
        print()
    print(map)
    bridges = get_all_possible_bridges(map)
    islands = get_islands(map)
    # adjacency list of all islands with all bridges
    whole_graph = Graph(map, bridges, islands, empty = False)
    # empty graph to add nodes to
    solution = Graph(map, bridges, islands, empty = True)

    print(whole_graph.graph)
    print(solution.graph)

    check_corners(whole_graph, map, solution)
    print(solution.graph)
    # solve_hashi(bridges, map)


def get_islands(map):
    islands = []
    for index, row in enumerate(map):
        for index2, island in enumerate(row):
            if island != 0:
                islands.append({'coordinates': (index, index2), 'bridges': island})
    return islands
            
def solve_hashi(bridges, map):
    # check corners
    check_corners(bridges, map)

def check_corners(graph, map, solution):
    if map[0][0] == 6:
        solution.add_edge("down", 3, (0,0))
        solution.add_edge("right", 3, (0,0))
    if map[len(map) - 1][0] == 6:
        solution.add_edge("up", 3, (len(map) - 1,0))
        solution.add_edge("right", 3, (len(map) - 1,0))
    if map[0][len(map[0]) -1] == 6:
        solution.add_edge("down", 3, (0,len(map[0]) -1))
        solution.add_edge("left", 3, (0,len(map[0]) -1))
    if map[len(map) -1][len(map[0]) -1] == 6:
        solution.add_edge("up", 3, (len(map) - 1,len(map[0]) -1))
        solution.add_edge("left", 3, (len(map) - 1,len(map[0]) -1))
    # if map[len(map) -1][0] == 6 or map[0][len(map) -1] or map[len(map) -1][len(map) -1]:
        

def get_all_possible_bridges(map):
    horiz_bridges =[]
    #scan horizontally
    for row_index, row in enumerate(map):
        for index, island in enumerate(row):
            bridge_len = 0
            bridge_found = False
            if island == 0:
                continue
            for count in range(index + 1, len(row)):
                if count == len(row):
                    pass
                
                if row[count] != 0:
                    bridge_found = True
                    bridge_len +=1
                    break
                if count == len(row) -1:
                    break
                bridge_len += 1
            if bridge_found:
                horiz_bridges.append({'starts_at': (row_index, index), 'ends_at': (row_index, index + bridge_len), 'possible_lengths': [0,1,2,3], 'direction': "horiz"})

                # maybe a list with all four cardianl bridges for each island
    vert_bridges = []
    for col_index in range(len(map[0])):
        for index, row in enumerate(map):
            bridge_len = 0
            bridge_found = False
            if row[col_index] == 0:
                continue
            for count in range(index + 1, len(map)):
                if count == len(map):
                    break
                if map[count][col_index] != 0:
                    bridge_found = True
                    bridge_len +=1
                    break
                if count == len(map) -1:
                    break
                bridge_len += 1
            if bridge_found:
                vert_bridges.append({'starts_at': (index, col_index), 'ends_at': (index + bridge_len, col_index), 'possible_lengths': [0,1,2,3], 'direction': "vert"})
    #             # maybe a list with all four cardianl bridges for each island
    return horiz_bridges + vert_bridges
            
        
def scan_map():
    text = []
    for line in sys.stdin:
        row = []
        for ch in line:
            n = ord(ch)
            if n >= 48 and n <= 57:    # between '0' and '9'
                row.append(n - 48)
            elif n >= 97 and n <= 122: # between 'a' and 'z'
                row.append(n - 87)
            elif ch == '.':
                row.append(0)
        text.append(row)

    nrow = len(text)
    ncol = len(text[0])

    map = np.zeros((nrow,ncol),dtype=np.int32)
    for r in range(nrow):
        for c in range(ncol):
            map[r,c] = text[r][c]
    
    return nrow, ncol, map


if __name__ == '__main__':
    main()