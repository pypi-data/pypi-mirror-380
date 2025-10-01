# Godsil-McKay Switch

This repository contains a simple implementation of the [Godsil-McKay switch](https://link.springer.com/article/10.1007/BF02189621).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[github](https://github.com/ahmeterdem1/godsil_mckay)
[pypi](https://pypi.org/project/gmswitch/)

## Graph Spectra

Graph spectrum is the set of eigenvalues of the adjacency matrix of a graph. This set can be
used to obtain information about the graph, without directly looking at the graph. For certain
but not all graphs, the adjacency spectrum can be uniquely identifying, at the same level as
isomorphism. However, there are many examples of non-isomorphic graphs that share the same
spectrum. Those graphs are called *cospectral* graphs.

## Constructing Cospectral Graphs

Godsil and McKay provided a method to construct cospectral graphs. The method is based on
partitioning the set of vertices of a given graph according to some rules. Then, edges
between certain groups of vertices are *switched*, which provably results in a graph
that is cospectral to the initial one, although not necessarily isomorphic.

### Partitioning

The given graph is partitioned into sets 

$$π=(C_1, C_2, \ldots C_k, D)$$ 

such that (1) any two vertices in $C_i$ have the same number of neighbours in $C_j$ 
and (2) $v \in D$ has either 0, $|C_i|/2$, or $|C_i|$ neighbours in $C_i$ for all $i$.

Such a partition will provide a basis for the switch. In the implementation given in this
repository, we search possible partitions of $π=(C, D)$, i.e. with only one set $C$.
This choice relaxes the need to satisfy condition (1) above. However, the subgraph defined
by $C$ must be regular, i.e. all vertices in $C$ must have the same degree.

### Switching

For all $v \in D$, if $v$ has $|C|/2$ neighbours in $C$, we delete those edges and connect $v$
to the other $|C|/2$ vertices in $C$ instead. This switching operation will produce a graph
that is cospectral to the original one.

## Resources

In the repository, we have also provided a dataset of graph that are all not cospectral to each other.
They can be used as input to the Godsil-McKay switch implementation to generate cospectral graphs, which
would also be not cospectral to the rest of the dataset.

## Example Usage

```python

from gmswitch.switch import simple_partition, godsil_mckay_switch
from gmswitch.measures import are_cospectral, adjacency_spectrum
import networkx as nx

G = nx.erdos_renyi_graph(10, 0.5)
C, D = None, None

for n in range(3, 7):
    C, D = simple_partition(G, n)  # try to find a (C, D) partition with |C|=n or n+1, whichever is even
    if C is not None:  # C and D is returned as None, if such a partition is impossible
        break

if C is not None:
    print("Found a valid (C, D) partition")
    G_switched = godsil_mckay_switch(G, C, D)  # Perform GM switch
    print("Are the original and switched graphs cospectral?", are_cospectral(G, G_switched))
    print("Original graph spectrum:", adjacency_spectrum(G))
    print("Switched graph spectrum:", adjacency_spectrum(G_switched))
else:
    print("No valid (C, D) partition found")
```

## Examples

Below is a valid $(C, D)$ partition for the plotted graph, where green nodes are the set of D
and blue nodes are the set of C. Notice that each green node either has no connection to blue nodes,
or is connected to half of the blue nodes, or could also be connected to all blue nodes. Also, subgraph
induced by $C$ (blue nodes) is a regular graph.

![partition1](https://raw.githubusercontent.com/ahmeterdem1/godsil_mckay/refs/heads/main/images/partition1.png)

Below is the graph after performing the Godsil-McKay switch on the above graph. The edges of node 4,
has been switched, so that now it connects to the other half of blue nodes. All other connections remain.
It can be verified in polynomial time that the graphs here before and after the switch are cospectral.

![switch1](https://raw.githubusercontent.com/ahmeterdem1/godsil_mckay/refs/heads/main/images/switch1.png)

Before switch

![partition2](https://raw.githubusercontent.com/ahmeterdem1/godsil_mckay/refs/heads/main/images/partition2.png)

After switch

![switch2](https://raw.githubusercontent.com/ahmeterdem1/godsil_mckay/refs/heads/main/images/switch2.png)

Before switch

![partition3](https://raw.githubusercontent.com/ahmeterdem1/godsil_mckay/refs/heads/main/images/partition3.png)

After switch

![switch3](https://raw.githubusercontent.com/ahmeterdem1/godsil_mckay/refs/heads/main/images/switch3.png)