import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import math

# Load dataset
data = pd.read_csv("routes.csv")
print("\n✅ Dataset loaded successfully:")
print(data.head())

# Create a directed weighted graph
G = nx.DiGraph()

# Add edges
for i, row in data.iterrows():
    if pd.notnull(row['source']) and pd.notnull(row['target']) and pd.notnull(row['distance']):
        G.add_edge(str(row['source']), str(row['target']), weight=float(row['distance']))

print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Example: shortest path using Dijkstra
start = "Central"
end = "SanJuan"

try:
    path = nx.dijkstra_path(G, start, end, weight='weight')
    distance = nx.dijkstra_path_length(G, start, end, weight='weight')
    print(f"Shortest path from {start} to {end}: {path}")
    print(f"Total distance: {distance} km")
except nx.NetworkXNoPath:
    print(f"No path exists between {start} and {end}")
    

# Graph visualization (stable version)
plt.figure(figsize=(12, 10))
pos = nx.circular_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='lightgreen', node_size=1300, edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=9, font_weight='bold')

for (u, v, d) in G.edges(data=True):
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    if not (math.isfinite(x1) and math.isfinite(y1) and math.isfinite(x2) and math.isfinite(y2)):
        continue
    plt.plot([x1, x2], [y1, y2], color='gray', linewidth=1.3, alpha=0.8)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    plt.text(mx, my, f"{d['weight']}", fontsize=8, color='blue', ha='center', va='center')

plt.title("Delivery Route Network - Graph Representation", fontsize=13, fontweight='bold')
plt.axis('off')
plt.tight_layout()
plt.show()
