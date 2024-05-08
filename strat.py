import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cm


def add_nodes_and_edges(G, dictionary, parent=None):
    viridis = cm.get_cmap("viridis", 6)
    cmap = viridis.colors[::-1]

    for key, value in dictionary.items():
        node_label = key
        if key.startswith("RvL") or key.startswith("RvR"):
            node_color = 0
        elif "grip" in key.lower():
            node_color = 1
        elif "step" in key.lower() or "push" in key.lower() or "pull" in key.lower():
            node_color = 2
        elif key.startswith("R "):
            node_color = 3
        elif key.startswith("L "):
            node_color = 4
        else:
            node_color = 5

        if parent:
            G.add_edge(parent, key)

        G.add_node(
            key,
            label=node_label,
            color=cmap[node_color],
            size=5000 if node_color in (3, 4) else 2000,
        )

        if isinstance(value, dict):
            add_nodes_and_edges(G, value, key)


stances = [
    {
        "RvR": {
            "Grip fight middle distance": {
                "Sleeve grip": {
                    "Collar grip": {
                        "Sprint step pull left": {"R Ko-uchi": {}, "R Osoto": {}},
                        "Pull forwards.": {
                            "R Sasae": {
                                "Back step, pull deep sprint step R": {
                                    "R Uchi-mata": {}
                                }
                            },
                            "L Ko-uchi": {
                                "R Ko-uchi": {"L De-ashi": {}, "R Ippon-seoi": {}},
                                "R Sasae": {},
                            },
                            "R swing Uchi-mata": {},
                        },
                        "Push sprint step back": {"R Ko-uchi": {}, "R O-uchi": {}},
                        "Left twist step forwards": {
                            "R Koshi-guruma": {},
                            "R Uchi-mata..": {},
                            "R Ippon-seoi..": {},
                        },
                    },
                    "Second sleeve grip (elbow)": {
                        "Pull forwards": {"R Uchi-mata.": {}},
                        "R Sode": {},
                        "L Sode": {},
                    },
                    "Cross grip": {
                        "R Osoto": {},
                        "R Ko-uchi-makikomi": {},
                        "L Reverse Kata-guruma": {},
                    },
                    "Push drive collapse first sleeve grip": {
                        "Pull forwards..": {"R Ippon-seoi.": {}},
                    },
                },
                "Armpit grip": {"Collar grip.": {"R Osoto.": {}}},
            },
        },
    },
    {
        "RvL": {
            "Grip fight middle distance": {
                "Collar grip (inside)": {
                    "Sleeve grip": {
                        "Shoulder up uke's collar grip": {
                            "Deep waist grip": {
                                "R Yagura-nage": {},
                                "R O-goshi": {},
                                "R Hane-goshi": {},
                            },
                            "Stab step R": {"Back-step L": {"R Uchi-mata": {}}},
                            "R Ko-soto": {
                                "Deep back-step L": {
                                    "R swing Harai-goshi": {},
                                    "R swing Tai-otoshi": {},
                                    "R Tani-otoshi": {
                                        "R Ashi-guruma": {},
                                        "R Osoto": {},
                                    },
                                    "R Ura-nage": {},
                                },
                            },
                            "Push sprint step": {
                                "Back-step L": {
                                    "R Uchi-mata": {},
                                    "R O-uchi": {
                                        "L Harai-tsurikomi-ashi": {
                                            "R Osoto": {"L De-ashi": {}}
                                        }
                                    },
                                },
                                "L Ippon-seoi": {},
                            },
                        }
                    }
                },
                "Collar grip (outside)": {"Collar grip (inside)": {}},
                "Double grip near sleeve": {
                    "Pull in": {"R belt grip": {"R Sumi-gaeshi": {}}}
                },
            }
        }
    },
]

for stance in stances:

    G = nx.DiGraph()
    add_nodes_and_edges(G, stance)
    node_colors = [data["color"] for _, data in G.nodes(data=True)]
    node_sizes = [data["size"] for _, data in G.nodes(data=True)]
    pos = nx.nx_pydot.graphviz_layout(G, prog="dot")

    fig = plt.figure(1, figsize=(15, 10))  # , font_size=10
    nx.draw(
        G,
        with_labels=True,
        node_color=node_colors,
        font_size=8,
        node_size=node_sizes,
        alpha=0.3,
        arrows=True,
        pos=pos,
    )
    plt.title("Strat")
    plt.show()
