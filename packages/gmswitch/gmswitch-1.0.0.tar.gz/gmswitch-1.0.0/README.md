# Godsil-McKay Switch

This repository contains a simple implementation of the [Godsil-McKay switch](https://link.springer.com/article/10.1007/BF02189621).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[github](https://github.com/ahmeterdem1/godsil_mckay)

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

## Examples

Below is a valid $(C, D)$ partition for the plotted graph, where green nodes are the set of D
and blue nodes are the set of C. Notice that each green node either has no connection to blue nodes,
or is connected to half of the blue nodes, or could also be connected to all blue nodes. Also, subgraph
induced by $C$ (blue nodes) is a regular graph.

![partition1](images/partition1.png)

Below is the graph after performing the Godsil-McKay switch on the above graph. The edges of node 4,
has been switched, so that now it connects to the other half of blue nodes. All other connections remain.
It can be verified in polynomial time that the graphs here before and after the switch are cospectral.

![switch1](images/switch1.png)

Before switch

![partition2](images/partition2.png)

After switch

![switch2](images/switch2.png)

Before switch

![partition3](images/partition3.png)

After switch

![switch3](images/switch3.png)