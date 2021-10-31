import math
import json
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import traveling_salesman_problem
import matplotlib.pyplot as plt
import requests

from models.chi_tiet_nhu_cau_mua import ChiTietNhuCauMua
from models.nhu_cau_mua import NhuCauMua
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.nguoi_dung import NguoiDung
from models.thuc_pham import ThucPham
from models.dang_ky_mua import DangKyMua

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
    """
        Get groups that have sum equal the sale
    """
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


def recommand_for_big_cube_food():
    """
        This func will call when one more food register created
        result fomat: {TP_MA: int - ND_MA: list}
    """

    food_list = ThucPham.get_all()
    register_list = DangKyMua.get_all()

    recommand_dict = {}  # TP_MA: [ND_MA]

    # get all food only buy the big cube
    big_cube_food = [
        food
        for food in food_list
        if food["TP_SO_LUONG_BAN_SI"]
    ]

    for bcf in big_cube_food:
        # get all registered of the big cube food
        filtered_register = [
            register
            for register in register_list
            if str(register["TP_MA"]) == str(bcf["TP_MA"])
        ]
        # generate group
        target = bcf["TP_SO_LUONG_BAN_SI"]
        # group of the registered
        groups = recommend_buy_big_cube(
            registered_list=filtered_register, target=target
        )
        # init min
        min_group_info = {
            "cost": math.inf,
            "members": []
        }
        for group in groups:
            print(
                f"""group for food {bcf.get("TP_MA")} {[u["ND_MA"] for u in group]}""")
            # generate graph by add multi edges

            def generateGraph() -> CustomGraph:
                """
                    Generate graph that contain all user's registered (nodes) and road (edges)
                """
                G = CustomGraph()
                for i in range(len(group)):
                    for j in range(i+1, len(group)):
                        try:
                            # must get weight here
                            coord_src = group[i]["DKM_VI_TRI_BAN_DO"].split(
                                "|")
                            coord_dest = group[j]["DKM_VI_TRI_BAN_DO"].split(
                                "|")
                            weight_1 = get_onroad_distance(
                                coord_src, coord_dest)
                            G.add_edge(group[i], group[j], weight_1)

                            # add edges to food place to src/dest place
                            coord_food = bcf.get("TP_VI_TRI_BAN_DO").split("|")
                            weight_food_src = get_onroad_distance(
                                coord_food, coord_src)
                            weight_food_dest = get_onroad_distance(
                                coord_food, coord_dest)
                            G.add_edge(bcf, group[i], weight_food_src)
                            G.add_edge(bcf, group[j], weight_food_dest)
                        except Exception as e:
                            pass
                return G

            G = generateGraph()
            # G.show()
            #  calc cost for ship this group (by on road distance)
            ship_cost = G.calc_sale_path()

            if ship_cost < min_group_info["cost"]:
                min_group_info["cost"] = ship_cost
                min_group_info["members"] = group

        # find group has minimum cost
        min_usert_ids = [
            user["ND_MA"]
            for user in min_group_info["members"]
        ]
        # print(f"Recommend {bcf['TP_MA']} to users: {min_usert_ids}")
        recommand_dict[bcf['TP_MA']] = min_usert_ids

    return recommand_dict


if __name__ == "__main__":
    # result = recommand_for_big_cube_food()
    # print(result)
    pass
