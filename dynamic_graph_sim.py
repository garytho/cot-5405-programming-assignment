import random
from numpy.random import choice

#this function takes as input the number of time steps to simulate,
#the probability p of a birth occuring
def simulate_dynamic_random_graph(time_length, p ):

    #initial graph
    graph = [[0]]
    
    graph_degree = [len(x) for x in graph]
    
    vertex_count = 1
    edge_count = 1
    
    
    vertex_hist = [vertex_count]
    edge_hist = [edge_count]
    
    
    for time_step in range(time_length):
        
        graph_degree = [len(x) for x in graph]
        if sum(graph_degree) == 0:
            break

        if random.random() <= p:
            #do birthing process
            graph = do_birth(graph, graph_degree, edge_count)
            edge_count += 1
            vertex_count += 1
        else:
            #do death process
            graph, vertex_count, edge_count = do_death(graph, graph_degree, vertex_count, edge_count)
            
        vertex_hist.append(vertex_count)
        edge_hist.append(edge_count)
    


def do_birth(graph, graph_degree, edge_count):
    if len(graph) == 1:
        new_node_loc = 0
    else:
        p= [ x  for x in graph_degree]
        bottom = sum(p)
        p = [1.0 * x / bottom for x in p]
        new_node_loc = choice(list(range(len(graph))), len(graph), p)[0]

    #our new node is attached to new_node_loc
    graph[new_node_loc].append(len(graph))
    graph.append([new_node_loc])
    return graph

def do_death(graph, graph_degree, vertex_count, edge_count):

    if len([x  for x in graph if x != []]) == 1:
        return [], 0, 0

    p = []
    for x in graph_degree:
        print(graph)
        if x == 0:
            p.append(0.0)
        else:
            p.append(1.0 * (vertex_count - x))
    bottom = sum(p)

    p = [1.0 * x / bottom for x in p]
    
    dead_node_loc = choice(list(range(len(graph))), len(graph), p)[0]
    edges_lost = graph_degree[dead_node_loc]
    for x in range(len(graph)):
        if dead_node_loc in graph[x]:
            graph[x].remove(dead_node_loc)
    graph[dead_node_loc] = []
    
    
    return graph, vertex_count - 1, edge_count - edges_lost
    
    
    
#example run
simulate_dynamic_random_graph(10, 0.5)