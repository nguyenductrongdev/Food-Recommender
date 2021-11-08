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

    food_type_list = DanhMucThucPham.get_all()
    unit_list = DanhMucDonViTinh.get_all()
    return render_template(
        "add_request.html",
        user_info=user_info,
        food_type_list=food_type_list,
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
            if int(register["TP_MA"]) == int(food["TP_MA"]) and
            not register["DKM_TRANG_THAI"] and
            int(register["CTDKM_SO_LUONG"]) <= int(food["TP_SO_LUONG"]) and
            int(register["CTDKM_SO_LUONG"]) % (
                food["TP_SUAT_BAN"] or 1) == 0
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
    # nd_ma = 6
    print(tp_ma, cluster_index, nd_ma)
    # join_cluster(tp_ma=tp_ma, cluster_index=cluster_index, nd_ma=nd_ma)

    return redirect("/nguoi-dung/goi-y-mua-chung")
