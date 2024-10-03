# Import necessary libraries
import networkx as nx
import matplotlib.pyplot as plt

# Function to create a mind map
def create_mind_map(center_node, nodes):
    # Create a new graph
    G = nx.Graph()

    # Add the central node
    G.add_node(center_node)

    # Add other nodes connected to the central node
    for node, sub_nodes in nodes.items():
        G.add_node(node)
        G.add_edge(center_node, node)
        
        # Add sub-nodes to the mind map
        for sub_node in sub_nodes:
            G.add_node(sub_node)
            G.add_edge(node, sub_node)

    # Draw the graph
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.3, iterations=50)  # Position the nodes
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    
    # Show the graph
    plt.show()

# Example usage
if __name__ == "__main__":
    center = "Minecraft Server Migration"
    # Define the nodes and their sub-nodes
    nodes = {
        "Power": ["HotSwap Power", "Power Backup installed"],
        "Transportation": ["Cyber Truck", "Loading/Unloading server (NO DAMAGE PLEASE)", "Hire a professional Driver"],
        "Reliablity": ["Post Migration Testing"],
        "Test": ["test"],
    }
    
    create_mind_map(center, nodes)
