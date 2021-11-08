import math
import numpy as np
import pandas as pd
from utils import get_user_info
from recommend_kits import update_recommend_data, get_recommend_data
import json
from models.chi_tiet_nhu_cau_mua import ChiTietNhuCauMua
from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session

from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.nhu_cau_mua import NhuCauMua

route = Blueprint(
    'api_nguoi_dung',
    __name__,
    template_folder='templates',
)


@route.route('/them-nhu-cau-mua', methods=['POST'])
def them_nhu_cau_mua():
    """
        Add nhu cau mua by form
    """
    try:
        query_string_dict = request.values
        newRequest = {
            "ND_MA": request.cookies.get("ND_MA"),
            "NCM_THOI_GIAN": query_string_dict["txtThoiGian"],
        }

        # Create NhuCauMua record
        new_food_request = NhuCauMua.create(newRequest)

        request_list = query_string_dict["requires"]
        request_list = json.loads(request_list)

        # print("request_list", request_list)

        for food_request_detail in request_list:
            # insert to ctncm
            new_rerquest_detail = {
                "DMTP_MA": food_request_detail["danhMuc"],
                "NCM_MA": new_food_request["NCM_MA"],
                "CTNCM_SO_LUONG": food_request_detail["soLuong"],
                "DMDVT_MA": food_request_detail["donVi"],
            }
            ChiTietNhuCauMua.create(new_rerquest_detail)

        return {"message": "Success"}, 200
    except Exception as e:
        return {"message": "Error"}, 500


@route.route('/goi-y-mua-chung', methods=['GET'])
def recommend_page():
    user_info = get_user_info()

    # get all clustur in mongo db database of current user as list
    list_of_clusters = get_recommend_data(nd_ma=user_info["ND_MA"])

    # sort cluster by cost
    cluster_df = pd.DataFrame(list_of_clusters).sort_values(by=["cost"])
    print(cluster_df)

    tp_ma_of_clusters = {}
    for i, cluster in cluster_df.iterrows():
        tp_ma = cluster["nodes"][0]["detail"]["TP_MA"]

        # map Nan to None
        for node_index in range(len(cluster["nodes"])):
            if math.isnan(cluster["nodes"][node_index]["detail"]["CTDKM_TRANG_THAI"]):
                cluster["nodes"][node_index]["detail"]["CTDKM_TRANG_THAI"] = None

        # append cluster["nodes"] to cluster of tp_ma
        if tp_ma in tp_ma_of_clusters.keys():
            tp_ma_of_clusters[tp_ma].append(
                cluster["nodes"]
            )
        else:
            tp_ma_of_clusters[tp_ma] = [cluster["nodes"]]

    with open("just_for_test.json", "w") as f:
        json.dump(tp_ma_of_clusters, f)

    # tp_ma_of_clusters explain
    """
        {
            tp_ma: [
                clusters [],
                clusters [],
            ]
        }

        new:
        {
            tp_ma: {
                cluster_index: [nodes],
                cluster_index: [nodes],
            }
        }
    """
    return {
        "recommend_data": tp_ma_of_clusters
    }
