import calendar
import os
import sys
import json
import math
import datetime
from const import COMPLETED, MERGED
from middlewares.require_login import require_login
from flask import Blueprint, request, abort, jsonify, url_for, render_template, redirect, flash, send_file, session, make_response
from uuid import uuid4
from jinja2 import TemplateNotFound
import logging
import pandas as pd


from models.chi_tiet_dang_ky_mua import ChiTietDangKyMua
from models.dang_ky_mua import DangKyMua
from models.thuc_pham import ThucPham
from models.chi_tiet_nhu_cau_mua import ChiTietNhuCauMua
from models.nguoi_dung import NguoiDung
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nhu_cau_mua import NhuCauMua

from recommend_kits import update_recommend_data, get_recommend_data, join_cluster
from utils import get_user_info

from models.db_utils import mongo_db

route = Blueprint(
    'nguoi_dung',
    __name__,
    template_folder='templates',
)


@route.route('/dang-nhap', methods=['GET'])
def login():
    """
        Render login page
    """
    return render_template("login.html")


@route.route('/dang-nhap', methods=['POST'])
def post_login():
    """
        Handle request from form data
    """
    try:
        query_string_dict = request.values

        username = query_string_dict["txtTaiKhoan"]
        password = query_string_dict["txtMatKhau"]

        user_list = NguoiDung.get_all()
        current_user = list(filter(
            lambda user: user["ND_TAI_KHOAN"] == username and user["ND_MAT_KHAU"] == password, user_list))
        current_user = current_user[0] if len(current_user) else None
        # set behavior depending on user
        if current_user:
            response = make_response(
                redirect(f"/nguoi-dung/{current_user.get('ND_TAI_KHOAN')}"))
            response.set_cookie('ND_MA', str(current_user["ND_MA"]))
            return response
        else:
            return redirect('/nguoi-dung/dang-nhap')
    except Exception as e:
        logging.getLogger("__main__").exception(e)
        abort(500)


@route.route('/dang-ky', methods=['GET'])
def register():
    """
        Render register page
    """
    return render_template("register.html")


@route.route('/dang-ky', methods=['POST'])
def post_register():
    """
        Create new user form api
    """
    try:
        query_string_dict = request.args
        new_user = {
            "ND_TAI_KHOAN": query_string_dict["txtTaiKhoan"],
            "ND_MAT_KHAU": query_string_dict["txtPassword"],
            "ND_HO_TEN": query_string_dict.get("txtFullname", None),
            "ND_DIA_cHI": query_string_dict.get("txtDiaChi", None),
            "ND_SO_DIEN_THOAI": query_string_dict.get("txtPhone", None),
            "ND_EMAIL": query_string_dict.get("txtEmail", None),
        }
        NguoiDung.create(new_user)
        return {
            "query_string_dict": query_string_dict,
            "message": "Đăng ký thành công",
        }
    except Exception as e:
        logging.getLogger("__main__").exception(e)
        abort(500)


@route.route('/dang-xuat', methods=['GET'])
def logout():
    resp = make_response(redirect("/"))
    resp.set_cookie('ND_MA', expires=0)
    return resp


@route.route('/them-nhu-cau-mua', methods=['GET'])
@require_login()
def add_request():
    nguoi_dung_list = NguoiDung.get_all()
    user_info = get_user_info()

    danh_muc_thuc_pham_list = DanhMucThucPham.get_all()
    unit_list = DanhMucDonViTinh.get_all()

    def dmtp_is_leaf(dmtp):
        # print(dmtp)
        parent_list = [
            *map(lambda item: item["DMTP_MA_DMTM_CHA"], danh_muc_thuc_pham_list)
        ]
        # leaf is not parent anywhere and have parent
        return dmtp["DMTP_MA"] not in parent_list and dmtp["DMTP_MA_DMTM_CHA"]

    # filter dmtp, just get leaf node
    dmtp_leaf = [
        *filter(dmtp_is_leaf, danh_muc_thuc_pham_list)
    ]

    return render_template(
        "add_request.html",
        user_info=user_info,
        food_type_list=dmtp_leaf,
        unit_list=unit_list,
        user_list=nguoi_dung_list,
    )


@route.route('/nhu-cau-mua', methods=['GET'])
def nhu_cau_mua():
    nguoi_dung_list = NguoiDung.get_all()
    food_requests = NhuCauMua.get_all()
    requests_details = ChiTietNhuCauMua.get_all()

    def get_request_details(req_ma):
        return list(filter(lambda req_detail: int(req_detail["NCM_MA"]) == int(req_ma), requests_details))

    for i in range(len(food_requests)):
        # get request_details
        req_details = get_request_details(food_requests[i]["NCM_MA"])
        food_requests[i].update({
            "details": req_details,
        })

    user_info = get_user_info()

    return render_template(
        "food_requests.html",
        food_requests=food_requests,
        user_info=user_info
    )


@route.route('/<nd_tai_khoan>', methods=['GET'])
@require_login()
def private_page(nd_tai_khoan):
    user_info = get_user_info()

    return render_template(
        "user.html",
        user_info=user_info,
    )


@route.route(r'/<nd_tai_khoan>/cua-hang', methods=['GET'])
@require_login()
def shop(nd_tai_khoan):
    food_list = ThucPham.get_all()
    registered_list = DangKyMua.get_all()

    def get_ready_registered_count(food: dict) -> int:
        """
            Get all registered that ready for process
        """
        ready_registered_list = [
            register
            for register in registered_list
            if all([
                # match food id
                int(register["TP_MA"]) == int(food["TP_MA"]),
                # enough to sale
                float(register["CTDKM_SO_LUONG"]) <= float(
                    food["TP_SO_LUONG"]),
                # not complete
                register["CTDKM_TRANG_THAI"] not in [COMPLETED],
                # fit count to sale
                float(register["CTDKM_SO_LUONG"]) > 0 and float(register["CTDKM_SO_LUONG"]) % (
                    food["TP_SUAT_BAN"] or register["CTDKM_SO_LUONG"]) == 0
            ])
        ]
        return len(ready_registered_list)

    user_info = get_user_info()

    food_list = [
        {
            **food,
            "ready_registered_count": get_ready_registered_count(food)
        }
        for food in food_list
        if food["ND_TAI_KHOAN"] == nd_tai_khoan

    ]
    # food_list = [*filter(lambda food: food["ND_TAI_KHOAN"]
    #                      == nd_tai_khoan, thuc_pham_list)]

    return render_template(
        "shop.html",
        user_info=user_info,
        food_list=food_list,

        data=json.dumps(food_list),
    )


@route.route('/goi-y-mua-chung', methods=['GET'])
def recommend_page():
    """
        Show clusters from mongo db
    """
    user_info = get_user_info()

    return render_template(
        "recommends.html",
        user_info=user_info,
    )


@route.route('/approve-join-cluster', methods=['POST'])
def approve_join_cluster():
    """
        Approve join cluster by set node of user: node.approve = true in MongoDB
    """

    query_string_dict = request.values
    user_info = get_user_info()

    tp_ma = query_string_dict["tp_ma"]
    cluster_index = query_string_dict["cluster_index"]
    nd_ma = user_info["ND_MA"]
    # tp_ma = 10
    # cluster_index = 0
    # nd_ma = 3
    print(tp_ma, cluster_index, nd_ma)
    join_cluster(
        tp_ma=int(tp_ma),
        cluster_index=int(cluster_index),
        nd_ma=int(nd_ma)
    )

    return redirect("/nguoi-dung/goi-y-mua-chung")


@route.route("/dashboard/<int:nd_ma>", methods=['GET'])
def dashboard(nd_ma):
    from db_utils import cursor
    user_info = get_user_info()
    query_string_dict = request.values
    filter_tp_ma_list = json.loads(
        query_string_dict.get('jsonFilterProduct') or "[]")

    print(
        f"[INFO/DASHBOARD] json {query_string_dict.get('jsonFilterProduct')}")

    CURRENT_MONTH_OPTION_VALUE = "current_month"

    CURRENT_YEAR = int(datetime.datetime.now().strftime("%Y"))
    CURRENT_MONTH = int(datetime.datetime.now().strftime("%m"))
    CURRENT_DAY = int(datetime.datetime.now().strftime("%d"))

    chart = {
        "header_rows": [],
        "rows": [],
    }

    def get_db_data() -> list:
        custom_sql = """
            SELECT
                dang_ky_mua.ND_MA as NguoiMua, thuc_pham.ND_MA as NguoiBan,
                danh_muc_thuc_pham.DMTP_TEN, chi_tiet_dang_ky_mua.CTDKM_SO_LUONG, dang_ky_mua.DKM_MA,
                chi_tiet_dang_ky_mua.CTDKM_GHI_CHU, thuc_pham.TP_DON_GIA, dang_ky_mua.DKM_THOI_GIAN,
                chi_tiet_dang_ky_mua.CTDKM_TRANG_THAI, thuc_pham.TP_MA
            FROM danh_muc_thuc_pham, thuc_pham, chi_tiet_dang_ky_mua, dang_ky_mua, nguoi_dung
            WHERE danh_muc_thuc_pham.DMTP_MA = thuc_pham.DMTP_MA
                AND thuc_pham.TP_MA = chi_tiet_dang_ky_mua.TP_MA
                AND chi_tiet_dang_ky_mua.DKM_MA = dang_ky_mua.DKM_MA
                AND dang_ky_mua.ND_MA = nguoi_dung.ND_MA
        """
        cursor.execute(custom_sql)
        return cursor.fetchall()

    def get_total(df: pd.DataFrame, day: int = None, month: int = None, year: int = None, tp_ma: int = None) -> float:
        """df: clean and ready to use dataframe"""
        total = 0.0
        for _, series in df.iterrows():
            _year, _month, _day = series["DKM_THOI_GIAN"].split("-")

            match_year = True if not year else int(year) == int(_year)
            match_month = True if not month else int(month) == int(_month)
            match_day = True if not day else int(day) == int(_day)
            match_tp_ma = True if not tp_ma else int(
                tp_ma) == int(series["TP_MA"])

            if all([match_year, match_month, match_day, match_tp_ma]):
                total += series["CTDKM_SO_LUONG"] * series["TP_DON_GIA"]

        return total

    db_df = pd.DataFrame(get_db_data())

    # draw each day of current month
    if query_string_dict.get("slFilterTime") == CURRENT_MONTH_OPTION_VALUE:
        print(f"[INFO/draw_day]")
        # if have specified food ids
        if len(filter_tp_ma_list):
            lines = []
            for day in range(1, CURRENT_DAY+1):
                print(day, "ahihi")
                line = [str(day), ]
                for tp_ma in filter_tp_ma_list:
                    total_of_food = get_total(
                        db_df,
                        day=day,
                        month=CURRENT_MONTH,
                        year=CURRENT_YEAR,
                        tp_ma=int(tp_ma),
                    )
                    line.append(total_of_food)
                lines.append(line)

            # build chart
            chart["header_rows"] = [
                {"type": "string", "text": "Tháng"},
                *[
                    {
                        "type": "number",
                        "type": "number", "text": f"{ThucPham.find(TP_MA=tp_ma)['TP_TEN']} (id: {ThucPham.find(TP_MA=tp_ma)['TP_MA']})",
                    }
                    for tp_ma in filter_tp_ma_list
                ]
            ]
            chart["rows"] = lines
        else:
            # not any specified food id
            lines = []
            for day in range(1, CURRENT_DAY+1):
                total_of_food = get_total(
                    db_df,
                    month=CURRENT_MONTH,
                    year=CURRENT_YEAR,
                    day=int(day),
                )
                lines.append([str(day), total_of_food])

            # build chart
            chart["header_rows"] = [
                {"type": "string", "text": "Ngày"},
                {"type": "number", "text": "Tổng tiền"},
            ]
            chart["rows"] = lines

    else:
        # draw each month of specified year
        print(f"[INFO/draw_month]")
        focus_year = int(
            query_string_dict.get("slFilterTime") or CURRENT_YEAR
        )
        if len(filter_tp_ma_list):
            lines = []
            for month in range(1, CURRENT_MONTH+1):
                line = [str(month), ]
                for tp_ma in filter_tp_ma_list:
                    total_of_food = get_total(
                        db_df,
                        month=int(month),
                        year=int(focus_year),
                        tp_ma=int(tp_ma),
                    )
                    print(f"m: {month}, total: {total_of_food}")
                    line.append(total_of_food)

                lines.append(line)
            # build chart
            chart["header_rows"] = [
                {"type": "string", "text": "Tháng"},
                *[
                    {
                        "type": "number", "text": f"{ThucPham.find(TP_MA=tp_ma)['TP_TEN']} (id: {ThucPham.find(TP_MA=tp_ma)['TP_MA']})",
                    }
                    for tp_ma in filter_tp_ma_list
                ]
            ]
            chart["rows"] = lines
        else:
            print(f"[INFO] year/not_id")
            # not any specified food id
            lines = []
            for month in range(1, CURRENT_MONTH+1):
                total_of_food = get_total(
                    db_df,
                    month=month,
                    year=focus_year,
                )
                lines.append([str(month), total_of_food])

            # build chart
            chart["header_rows"] = [
                {"type": "string", "text": "Tháng"},
                {"type": "number", "text": "Tổng tiền"},
            ]
            chart["rows"] = lines

    print(chart)
    return render_template(
        "user_thong_ke.html",
        user_info=user_info,

        chart_title=f"Biểu đồ thống kê",
        chart=chart,

        owner_foods=[
            *filter(lambda food: food["ND_MA"] == user_info["ND_MA"], ThucPham.get_all())
        ],

        # default
        slFilterTime=query_string_dict.get("slFilterTime") or CURRENT_YEAR,
        slFilterProduct=query_string_dict.get("slFilterProduct", ""),
    )


@ route.route("/danh-sach-dang-ky-mua/<int:nd_ma>", methods=['GET'])
def list_of_ctncm(nd_ma):
    user_info = get_user_info()
    list_of_ctncm = ChiTietDangKyMua.get_all()
    # sort near to far
    list_of_ctncm = sorted(
        list_of_ctncm,
        key=lambda ctncm: datetime.datetime.strptime(
            ctncm["DKM_THOI_GIAN"],
            "%Y-%m-%d").date(),
        reverse=True
    )

    df = pd.DataFrame(list_of_ctncm)
    df = df[df["ND_MA"] == int(nd_ma)]
    # count in firt column
    df["order"] = list(range(1, len(df)+1))

    return render_template(
        "list_of_ctdkm.html",
        user_info=user_info,
        data_list=df.to_dict('records'),
    )
