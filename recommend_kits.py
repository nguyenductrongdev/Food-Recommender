from numpy import ndenumerate
import pandas as pd
import math
import json
import networkx as nx
from networkx.algorithms.approximation.traveling_salesman import traveling_salesman_problem
import matplotlib.pyplot as plt
import requests

from models.chi_tiet_nhu_cau_mua import ChiTietNhuCauMua
from models.nhu_cau_mua import NhuCauMua
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.chi_tiet_dang_ky_mua import ChiTietDangKyMua
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.nguoi_dung import NguoiDung
from models.thuc_pham import ThucPham
from models.dang_ky_mua import DangKyMua

import time
import collections

from typing import List, Dict

from models.db_utils import mongo_db


groups = []

CLUSTERS_OF_FOOD_COLLECTION = "clusters_of_food"


def _subset_sum(registers: list, target: float, current_group: list = []) -> None:
    global groups

    s = sum([register["CTDKM_SO_LUONG"] for register in current_group])

    # check if the current_group sum is equals to target
    if s % target == 0:
        # append 1D current_group group to 2D groups list
        groups += [current_group]
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(registers)):
        n = registers[i]
        remaining = registers[i+1:]
        _subset_sum(remaining, target, current_group + [n])


def get_groups(registere_detail_list, target) -> list:
    """
        Get groups that have sum equal the sale
    """
    global groups
    groups = []
    _subset_sum(registere_detail_list, target)
    # return by ignore empty list at head
    return groups[1:]


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


def recommand_for_big_cube_food(tp_ma: int) -> dict:
    """
        This func will call when one more food register created
        return format: {"cost": int, "register_detail_list": list}
    """

    # check food is need recommend
    if tp_ma not in [
        food["TP_MA"]
        for food in ThucPham.get_all() if food["TP_SUAT_BAN"]
    ]:
        print("[WARNING] Food not sale by bcf")
        return

    # get register details contain THIS FOOD ID and not done
    register_details_df = pd.DataFrame(ChiTietDangKyMua.get_all())
    register_details_df = register_details_df[
        (register_details_df["TP_MA"] == tp_ma) & (
            register_details_df["CTDKM_TRANG_THAI"].isin([float("nan"), 0]))
    ]

    # get all clusters fit target value
    raw_data = register_details_df.to_dict('records')
    target = ThucPham.find(TP_MA=tp_ma)["TP_SUAT_BAN"]
    clusters = get_groups(registere_detail_list=raw_data, target=target)

    def generateGraph(food: dict, cluster: list) -> CustomGraph:
        """
            Generate graph that contain all user's registered (nodes) and road (edges)
        """
        G = CustomGraph()
        for i in range(len(cluster)):
            for j in range(i+1, len(cluster)):
                try:
                    # must get weight here
                    coord_src = cluster[i]["DKM_VI_TRI_BAN_DO"].split(
                        "|")
                    coord_dest = cluster[j]["DKM_VI_TRI_BAN_DO"].split(
                        "|")
                    weight_1 = get_onroad_distance(
                        coord_src, coord_dest)
                    G.add_edge(cluster[i], cluster[j], weight_1)

                    # add edges to food place to src/dest place
                    coord_food = food.get("TP_VI_TRI_BAN_DO").split("|")
                    weight_food_src = get_onroad_distance(
                        coord_food, coord_src)
                    weight_food_dest = get_onroad_distance(
                        coord_food, coord_dest)
                    G.add_edge(food, cluster[i], weight_food_src)
                    G.add_edge(food, cluster[j], weight_food_dest)
                except Exception as e:
                    pass
        return G

    # find the cluster that have min cost
    food_info = ThucPham.find(TP_MA=tp_ma)
    # define min callback

    def get_cost_callback(cluster: list) -> float:
        G = generateGraph(food=food_info, cluster=cluster)
        # calc code: cost calc by on road distance. Can define more here
        cost = G.calc_sale_path()
        return cost

    # append cost field for clusters
    clusters = [
        *map(lambda cluster: {"register_detail_list": cluster, "cost": get_cost_callback(cluster)}, clusters)
    ]

    return clusters


def update_recommend_data(tp_ma: int) -> None:
    """
        Update recommend data into MongoDB
        (*notice: each cluster identify by list of DKM_MA)
    """
    calc_clusters = recommand_for_big_cube_food(tp_ma=tp_ma)

    # # sample data
    # calc_clusters = [
    #     {
    #         "cost": 10,
    #         "register_detail_list": [
    #             {
    #                 "TP_MA": 10,
    #                 "DKM_MA": 99,
    #                 "CTDKM_SO_LUONG": 20,
    #                 "ND_MA": 99,
    #             }
    #         ],
    #     },
    # ]

    try:
        # get old document
        old_mongo_document = list(mongo_db[CLUSTERS_OF_FOOD_COLLECTION].find(
            {"TP_MA": tp_ma}
        ))[0]

        # list of dkm_ma dai dien cho cluster
        old_cluster_dkm_ma_list = [
            sorted([*map(lambda node: node["detail"]["DKM_MA"], cluster["nodes"])])
            for cluster in old_mongo_document["clusters"]
        ]

        calc_cluster_dkm_ma_list = [
            sorted([
                item["DKM_MA"] for item in cluster["register_detail_list"]
            ])
            for cluster in calc_clusters
        ]

        # find new clusters need to update
        # print(old_cluster_dkm_ma_list, "\n", calc_cluster_dkm_ma_list)

        new_clusters_of_dkm_ma = []
        for items_1 in calc_cluster_dkm_ma_list:
            # append when the cluster not exist any cluster
            if all([collections.Counter(items_1) != collections.Counter(items_2) for items_2 in old_cluster_dkm_ma_list]):
                new_clusters_of_dkm_ma += [items_1]

        print(f"the new {new_clusters_of_dkm_ma}")

        # update new clusters
        def _find_cluster_by_dkm_ma_list(filter_list: List[int]) -> List[dict]:
            # filter_list: list of dkm_ma to filter
            for cluster in calc_clusters:
                # get dkm_ma list of current cluster
                cluster_dkm_ma_list = sorted([
                    item["DKM_MA"]
                    for item in cluster["register_detail_list"]
                ])
                # find and return cluster info
                if collections.Counter(sorted(cluster_dkm_ma_list)) == collections.Counter(sorted(filter_list)):
                    return cluster
            return None

        for dkm_ma_list in new_clusters_of_dkm_ma:
            cluster_info = _find_cluster_by_dkm_ma_list(dkm_ma_list)
            new_cluster = {
                "host": None,
                "cost": cluster_info["cost"],
                "nodes": [{
                    "approve": False,
                    "detail": cluster_info["register_detail_list"]
                }]
            }
            # important handle
            # old_mongo_document["clusters"].push(new_cluster)

            mongo_db[CLUSTERS_OF_FOOD_COLLECTION].update_one(
                {"TP_MA": tp_ma},
                {
                    "$push": {"clusters": new_cluster}
                }
            )
    except IndexError:
        print("[INFO] Create new mongodb document")
        new_mongo_document = {
            "TP_MA": tp_ma,
            "clusters": [
                {
                    "host": None,
                    "cost": cluster["cost"],
                    "nodes": [
                        {"approve": False, "detail": detail}
                        for detail in cluster["register_detail_list"]
                    ]
                }
                for cluster in calc_clusters
            ]
        }
        mongo_db[CLUSTERS_OF_FOOD_COLLECTION].insert_one(new_mongo_document)
    except Exception:
        print(f"[ERROR] bug")


def get_recommend_data(nd_ma: int) -> list:
    """
        Get all mongo documents that include the specified user
    """
    cluster_result = []
    data_list = list(
        mongo_db[CLUSTERS_OF_FOOD_COLLECTION].find(
            {}, {"_id": 0}
        )
    )

    for document in data_list:
        # print(f"document for {document['TP_MA']}")
        # get clusters that include specified user in current document
        valid_clusters = []
        for cluster in document["clusters"]:
            if nd_ma in [int(node["detail"]["ND_MA"]) for node in cluster["nodes"]]:
                valid_clusters.append(cluster)

        if len(valid_clusters):
            # concat valid_clusters to result
            cluster_result += valid_clusters

    return cluster_result


def join_cluster(tp_ma, cluster_index, nd_ma):
    """
        [Notice] This function communicate with MongoDB
        Execute join cluster behavior and select host
    """

    # get MongoDB document
    mongodb_document = mongo_db[CLUSTERS_OF_FOOD_COLLECTION].find_one({
        "TP_MA": tp_ma
    })

    # find node index
    node_index = -1
    for i, node in enumerate(mongodb_document["clusters"][cluster_index]["nodes"]):
        if int(node["detail"]["ND_MA"]) == int(nd_ma):
            node_index = i

    print(f"[DEBUG] {tp_ma} > {cluster_index} > {node_index}")
    # set approve of specified user is True
    mongo_db[CLUSTERS_OF_FOOD_COLLECTION].update_one(
        {"TP_MA": tp_ma},
        {
            "$set": {
                f"clusters.{cluster_index}.nodes.{node_index}.approve": True,
            }
        }
    )

    # check to set host of cluster if can, the cluster is ready when all approve
    is_ready_cluster = all([
        node["approve"] for node in mongodb_document["clusters"][cluster_index]["nodes"]
    ])
    if is_ready_cluster:
        host_node = max(
            mongodb_document["clusters"][cluster_index]["nodes"],
            key=lambda node: node["detail"]["CTDKM_SO_LUONG"]
        )
        # host value is nd_ma if
        host_value = host_node["detail"]["ND_MA"]
        mongo_db[CLUSTERS_OF_FOOD_COLLECTION].update_one(
            {"TP_MA": tp_ma},
            {
                "$set": {
                    f"clusters.{cluster_index}.host": host_value
                }
            }
        )


if __name__ == "__main__":
    start_time = time.time()
    update_recommend_data(tp_ma=12)
    print(f"Run {time.time() - start_time} seconds")

    # CLUSTERS_OF_FOOD_COLLECTION = "clusters_of_food"
    # x = mongo_db[CLUSTERS_OF_FOOD_COLLECTION].find({"TP_MA": 12})
    # print(list(x))

    pass
