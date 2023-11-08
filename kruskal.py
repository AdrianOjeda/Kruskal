import networkx as nx
import matplotlib.pyplot as plt
import random

# Crear un grafo
G = nx.Graph()
random.seed(61)

# Agregar nodos
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
G.add_nodes_from(nodes)

# Agregar aristas con pesos
edges_with_weights = [
    ("A", "G", 10),
    ("A", "I", 11),
    ("A", "F", 2),
    ("B", "D", 21),
    ("B", "G", 22),
    ("B", "I", 14),
    ("C", "H", 7),
    ("C", "A", 9),
    ("C", "D", 11),
    ("D", "B", 9),
    ("D", "F", 13),
    ("D", "J", 19),
    ("E", "C", 16),
    ("E", "B", 3),
    ("E", "D", 9),
    ("E", "A", 14),
    ("F", "B", 15),
    ("G", "I", 5),
    ("G", "C", 17),
    ("H", "B", 16),
    ("H", "A", 18),
    ("I", "H", 16),
    ("I", "J", 12),
    ("J", "C", 11),
    ("J", "A", 14)
]

G.add_weighted_edges_from(edges_with_weights)

# Posiciones de los nodos
pos = nx.spring_layout(G, seed=61)

# Crear una figura con dos subgráficos
fig, axes = plt.subplots(1, 2, figsize=(15, 8))

# Dibuja el grafo original
nx.draw(G, pos, with_labels=True, ax=axes[0])
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=axes[0])
axes[0].set_title("Grafo Original")

# Dibuja el grafo con Kruskal
pos = nx.spring_layout(G, seed=61)
mst = nx.minimum_spanning_tree(G, algorithm="kruskal")
nx.draw(mst, pos, with_labels=True, ax=axes[1])
labels = nx.get_edge_attributes(mst, "weight")
nx.draw_networkx_edge_labels(mst, pos, edge_labels=labels, ax=axes[1])
axes[1].set_title("Grafo con Kruskal")

# Mostrar la figura
plt.show()
