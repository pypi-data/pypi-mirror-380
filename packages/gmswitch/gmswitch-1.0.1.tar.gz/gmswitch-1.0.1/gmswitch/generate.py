import networkx as nx
import random
import numpy as np
from .measures import adjacency_spectrum, are_cospectral

def generate_non_cospectral_graphs(num_graphs, n, p, max_tries: int = 100, directed: bool = True) -> list:
    """
    Generate a set G of non-cospectral graphs.
    :param num_graphs: number of distinct graphs to generate
    :param n: number of nodes per graph
    :param p: probability of edge creation (Erdős–Rényi model)
    """
    graphs = []
    spectra = []
    tries = 0

    while tries < max_tries and len(graphs) < num_graphs:
        g = nx.erdos_renyi_graph(n, p, directed=directed)
        # check if g is cospectral to any already in set
        g_spectra = adjacency_spectrum(g)
        if not any(np.array_equal(g_spectra, s) for s in spectra):
            graphs.append(g)
            tries = 0
            continue
        tries += 1

    return graphs

def generate_non_isomorphic_graphs(num_graphs, n, p, max_tries: int = 100) -> list:
    """
    Generate a set G of non-isomorphic graphs.
    :param num_graphs: number of distinct graphs to generate
    :param n: number of nodes per graph
    :param p: probability of edge creation (Erdős–Rényi model)
    """
    GM = nx.algorithms.isomorphism.GraphMatcher
    graphs = []
    tries = 0

    while tries < max_tries and len(graphs) < num_graphs:
        g = nx.erdos_renyi_graph(n, p, directed=True)
        # check if g is isomorphic to any already in set
        if not any(GM(g, h).is_isomorphic() for h in graphs):
            graphs.append(g)
            tries = 0
            continue
        tries += 1

    return graphs

def generate_isomorphic_set(g, k) -> list:
    """
    Generate k isomorphic copies of g by permuting node labels.
    """
    nodes = list(g.nodes())
    copies = []
    for _ in range(k):
        perm = nodes[:]
        random.shuffle(perm)
        mapping = dict(zip(nodes, perm))
        h = nx.relabel_nodes(g, mapping)
        copies.append(h)
    return copies








