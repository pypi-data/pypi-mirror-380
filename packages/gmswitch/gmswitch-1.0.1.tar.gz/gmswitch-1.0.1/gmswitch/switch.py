import networkx as nx
from itertools import combinations
import random
from copy import deepcopy

def induced_subgraph_is_regular(G, C):
    """Return (bool, degree) if induced subgraph G[C] is regular (all vertices same degree)."""
    sub = G.subgraph(C)
    degrees = [d for _, d in sub.degree()]
    return len(set(degrees)) == 1

def simple_partition(G: nx.Graph, n: int = 1, trivial: bool = False):

    nodes = list(G.nodes())
    V = set(G.nodes())
    C = None
    D = None
    valid = False

    if (len(nodes) - n) % 2:  # size of C
        n += 1
    C_size = len(nodes) - n

    random.shuffle(nodes)

    for candidates in combinations(nodes, n):
        D = set(candidates)
        C = V - D
        Ns = []
        for node in D:
            count = 0
            for other_node in C:
                count += G.number_of_edges(node, other_node)
            Ns.append(count)

        #Ns = [len(G.edges(node)) for node in D]
        conditions = [(k == 0) or (k == C_size // 2) or (k == C_size) for k in Ns]

        if all(conditions) and induced_subgraph_is_regular(G, C):
            # We do not accept the trivial partition by default
            if not trivial and (all(k == 0 for k in Ns) or all(k == C_size for k in Ns)):
                continue
            valid = True
            break

    if valid:
        return C, D
    return None, None

def get_partitions(G: nx.Graph, trivial: bool = False) -> list:
    N = G.number_of_nodes()
    partitions = []
    for n in range(1, N // 2 + 1):
        C, D = simple_partition(G, n=n, trivial=trivial)
        if C is not None:
            partitions.append((C, D))
    return partitions


def godsil_mckay_switch(G: nx.Graph, C, D) -> nx.Graph:
    """
    Perform Godsil-McKay switching on graph G.
    :param G: input graph (networkx Graph)
    :param C: subset of vertices in G (set)
    :param D: subset of vertices in G (set)
    :return: switched graph (networkx Graph)
    """

    half_c = len(C) // 2
    H = deepcopy(G)
    for d in D:
        neighbors = list(G.neighbors(d))
        C_neighbors = set(c for c in neighbors if c in C)
        non_C_neighbors = set(c for c in C if c not in neighbors)

        # Remove edges to current neighbors in C
        #print(d, len(C_neighbors))
        if len(C_neighbors) == half_c:
            for c in C_neighbors:
                H.remove_edge(d, c)

            # Add edges to non-neighbors in C
            for c in non_C_neighbors:
                H.add_edge(d, c)

    return H


