import numpy as np
import networkx as nx

def adjacency_spectrum(G):
    """Return sorted eigenvalues of the adjacency matrix of G."""
    A = nx.to_numpy_array(G)   # adjacency matrix as NumPy array
    eigvals = np.linalg.eigvals(A)
    # Sort to make comparison consistent, round to avoid floating-point noise
    return np.round(np.sort(np.real(eigvals)), 5)

def are_cospectral(G, H):
    """Check if two graphs are cospectral."""
    return np.array_equal(adjacency_spectrum(G), adjacency_spectrum(H))


