import pandas as pd
from models.dang_ky_mua import DangKyMua
from schema import Schema, And, Use, Optional, SchemaError
from functools import wraps
import uuid
import os
import logging
import configparser
from flask import Blueprint, Flask, json, request,  jsonify, url_for, render_template, redirect, flash, send_file, session


from models.thuc_pham import ThucPham
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.nguoi_dung import NguoiDung


route = Blueprint(
    'api_thuc_pham',
    __name__,
)


config = configparser.ConfigParser()
CONFIG_PATH = os.path.abspath("./config.ini")
config.read(CONFIG_PATH)


def check(api_schema, api_params):
    try:
        api_schema.validate(api_params)
        return True
    except SchemaError:
        return False


@route.route('/', methods=['GET'])
def index():
    thuc_pham_list = ThucPham.get_all()
    query_string_dict = request.values

    # param for pagination
    limit = query_string_dict.get("limit")
    page = query_string_dict.get("page")

    nd_ma = query_string_dict.get("nd_ma")
    dmtp_ma = query_string_dict.get("dmtp_ma")

    if nd_ma:
        thuc_pham_list = list(filter(
            lambda food: food.get("ND_MA") == int(nd_ma), thuc_pham_list))

    if dmtp_ma:
        thuc_pham_list = list(filter(
            lambda food: food.get("DMTP_MA") == int(dmtp_ma), thuc_pham_list))

    if page:
        page = int(page)
        limit = int(limit)

        start_index = limit*(page-1)
        end_index = start_index + limit
        thuc_pham_list = thuc_pham_list[start_index: end_index]

    return {
        "foods": thuc_pham_list
    }


@route.route('/goi-y', methods=['GET'])
def recommend():
    try:
        thuc_pham_list = ThucPham.get_all()

        query_string_dict = request.values

        api_schema = Schema([
            {
                'ncm_dmtp': And(Use(str)),
                'ncm_sl': And(Use(str)),
                'ncm_dmdvt': And(Use(str)),
            }
        ])

        recommend_request = json.loads(query_string_dict["recommend_request"])

        # make sure api param is valid schema
        assert check(api_schema, recommend_request)
        # get all dmtp_ma from db
        db_dmtp_ma_list = [
            *map(lambda db_thuc_pham: db_thuc_pham["DMTP_MA"], thuc_pham_list)
        ]
        # make sure all ncm_dmtp is valid value
        assert all([
            int(req["ncm_dmtp"]) in db_dmtp_ma_list
            for req in recommend_request
        ])

        # sort by dmtp_ma and cost
        ncm_dmtm_ma = [
            *map(lambda req: int(req["ncm_dmtp"]), recommend_request)
        ]
        data = [
            *filter(lambda db_thuc_pham: int(db_thuc_pham["DMTP_MA"]) in ncm_dmtm_ma, thuc_pham_list)
        ]

        cost_order_df = pd.DataFrame(data).sort_values(
            by=["DMTP_MA", "TP_DON_GIA"],
        )
        recommend_result = cost_order_df.to_dict('records')
        return {
            "shop": recommend_result,
        }

    except Exception as e:
        raise
        return {"message": str(e) or "Internal server error"}, 500


@route.route('/<tp_ma>', methods=['PUT'])
def sale(tp_ma):
    query_string_dict = request.values
    nd_ma = query_string_dict["nd_ma"]
    payload = query_string_dict["payload"]
    # get currebt food counts
    current_food = ThucPham.find(TP_MA=tp_ma)
    count = float(current_food["TP_SO_LUONG"]) - float(payload)
    # # update food count to thuc_pham table
    ThucPham.update({
        "TP_MA": tp_ma,
        "TP_SO_LUONG": count,
    })
    # update to set registered is done
    DangKyMua.update({
        "ND_MA": nd_ma,
        "TP_MA": tp_ma,
        "DKM_TRANG_THAI": 1,
    })

    return query_string_dict
