triangles = nx.triangles(G)
for node, triangle_count in triangles.items():
    print(f"Node {node}: Triangle Count = {triangle_count}")