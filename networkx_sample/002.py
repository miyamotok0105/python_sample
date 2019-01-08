#coding = utf-8
import networkx as nx
import matplotlib.pyplot as plt

all_edges_0 = [(1,2), (2,3)]
print(all_edges_0)

def init_graph():
    g = nx.DiGraph()
    g.add_edges_from(all_edges_0)
    return g

def plot_graph(g):
    pos = nx.spring_layout(g, k=1.8)
    plt.figure(figsize=(15,15))
    a_graph = nx.nx_agraph.to_agraph(g)

    a_graph.node_attr.update(fontname="MS Gothic")
    a_graph.layout("dot")
    a_graph.draw("test.png")
    nx.draw_networkx(g, pos)
    nx.write_gexf(g, 'test.xml') 
    plt.show()

g = init_graph()
plot_graph(g)