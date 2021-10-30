import json
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import traveling_salesman_problem
import matplotlib.pyplot as plt
import requests

groups = []


def _subset_sum(registers: list, target: float, current_group: list = []) -> None:
    global groups

    s = sum([register["DKM_SO_LUONG"] for register in current_group])

    # check if the current_group sum is equals to target
    if s == target:
        # append 1D current_group group to 2D groups list
        groups += [current_group]
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(registers)):
        n = registers[i]
        remaining = registers[i+1:]
        _subset_sum(remaining, target, current_group + [n])


def recommend_buy_big_cube(registered_list, target) -> list:
    global groups
    groups = []
    _subset_sum(registered_list, target)
    return groups


class CustomGraph(nx.Graph):
    def __init__(self):
        super().__init__()

    def add_edge(self, user1: dict, user2: dict, weight: float = None):
        assert user1["ND_MA"]
        assert user2["ND_MA"]

        u = f"""{user1["ND_MA"]}"""
        v = f"""{user2["ND_MA"]}"""

        super().add_node(u)
        super().add_node(v)
        super().add_edge(u, v, weight=weight)

    def calc_sale_path(self, nodes: list = None) -> float:
        """
            Calculate shipping costs to all nodes
        """
        nodes = nodes or self.nodes
        nodes = [*map(lambda node: str(node), nodes)]

        salesman_path = traveling_salesman_problem(self, nodes=nodes)
        total_cost = 0.0
        # calc sum for all shipping edges
        total_cost = sum([
            self[str(salesman_path[i])][str(salesman_path[i+1])]["weight"]
            for i in range(len(salesman_path)-1)
        ])
        return total_cost

    def show(self):
        options = {
            "font_size": 10,
            "node_size": 2000,
            "node_color": "white",
            "edgecolors": "black",
            "linewidths": 5,
            "width": 5,
            "with_labels": True,
        }
        nx.draw_networkx(self, **options)
        nx.draw_networkx_edge_labels(
            self,
            pos=nx.spring_layout(self),
            edge_labels=nx.get_edge_attributes(self, 'weight'),
            font_size=10
        )
        ax = plt.gca()
        ax.margins(0.20)
        plt.axis("off")
        plt.show()


def get_onroad_distance(coord_src: list, coord_dest: list) -> float:
    """
        Get on road distance in kilometer
    """
    latitude_1, longitude_1 = coord_src
    latitude_2, longitude_2 = coord_dest
    r = requests.get(
        f"http://router.project-osrm.org/route/v1/legs/{longitude_1},{latitude_1};{longitude_2},{latitude_2}?overview=false")
    route = json.loads(r.content)["routes"][0]
    return route["distance"]/1000


if __name__ == "__main__":
    # G = CustomGraph()
    # a = {"ND_MA": 1, "ND_TEN": "Test 1"}
    # b = {"ND_MA": 2, "ND_TEN": "Test 2"}
    # c = {"ND_MA": 3, "ND_TEN": "Test 3"}

    # G.add_edge(a, b, 3)
    # G.add_edge(a, c, 2)

    # print(G.edges)

    pass
