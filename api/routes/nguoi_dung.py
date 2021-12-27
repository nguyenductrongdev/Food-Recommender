import math
import numpy as np
import pandas as pd
from const import COMPLETED, MERGED
from models.chi_tiet_dang_ky_mua import ChiTietDangKyMua
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
    register_detail_list = ChiTietDangKyMua.get_all()

    def _get_ctdkm(dkm_ma: int, tp_ma: int) -> dict:
        dkm_ma = int(dkm_ma)
        tp_ma = int(tp_ma)

        df = pd.DataFrame(register_detail_list)
        df = df[
            df.apply(
                lambda row: row["DKM_MA"] == dkm_ma and row["TP_MA"] == tp_ma,
                axis=1
            )
        ]

        return df.to_dict("records")[0] if len(df) else None

    # get all clustur in mongo db database of current user as list
    list_of_clusters = get_recommend_data(nd_ma=user_info["ND_MA"])

    list_of_clusters = sorted(
        list_of_clusters, key=lambda data: data["cluster"]["cost"]
    )

    # sort cluster by cost
    cluster_df = pd.DataFrame(list_of_clusters)
    # print(cluster_df)

    response_dict = {}
    for _, data in cluster_df.iterrows():
        tp_ma = data["cluster"]["nodes"][0]["detail"]["TP_MA"]
        if tp_ma not in response_dict:
            response_dict[tp_ma] = []

        # replaced nan by None
        for node in data["cluster"]["nodes"]:
            if bool(node["detail"]["CTDKM_TRANG_THAI"]) and math.isnan(node["detail"]["CTDKM_TRANG_THAI"]):
                node["detail"]["CTDKM_TRANG_THAI"] = None

        approve_db_count = len([
            node
            for node in data["cluster"]["nodes"]
            if _get_ctdkm(
                dkm_ma=node["detail"]["DKM_MA"],
                tp_ma=node["detail"]["TP_MA"]
            )["CTDKM_TRANG_THAI"] in [MERGED, COMPLETED]
        ])

        # skip when one of cluster/ctdkm item merged
        print("approve_db_count", approve_db_count, len(data["cluster"]["nodes"]))
        is_skip_cluster = approve_db_count not in [
            0, len(data["cluster"]["nodes"])
        ]

        if not is_skip_cluster:
            # append to response_dict
            response_dict[tp_ma].append({
                "cluster_index": data["cluster_index"],
                "nodes": data["cluster"]["nodes"],
            })

    with open("just_for_test.json", "w") as f:
        json.dump(response_dict, f)

    # tp_ma_of_clusters explain
    """
        {
            tp_ma: [
                {"cluster_index": 1, nodes: []}
            ]
        }
    """
    response_dict = {
        key: value
        for key, value in response_dict.items()
        if value
    }

    return {
        "recommend_data": response_dict
    }
