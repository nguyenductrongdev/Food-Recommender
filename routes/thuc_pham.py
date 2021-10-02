from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session

from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.dang_ky_mua import DangKyMua

from middlewares.require_login import require_login
from models.thuc_pham import ThucPham

route = Blueprint(
    'thuc_pham',
    __name__,
    template_folder='templates',
)


@route.route('/', methods=['GET'])
@require_login()
def tp_index():
    food_list = ThucPham.get_all()
    nguoi_dung_list = NguoiDung.get_all()

    query_string_dict = request.values
    tp_ma = query_string_dict.get("tp_ma")

    food = list(
        filter(lambda food: food.get("TP_MA") == int(tp_ma), food_list)
    )[0]

    # get user for template
    _ = list(filter(lambda nd: str(nd.get('ND_MA')) ==
                    request.cookies.get("ND_MA"), nguoi_dung_list))

    user_info = _[0]
    # get user for template

    return render_template(
        "food.html",
        food=food,
        user_info=user_info
    )


@route.route('/them', methods=['GET'])
@require_login()
def add_thuc_pham():
    food_list = DanhMucThucPham.get_all()
    unit_list = DanhMucDonViTinh.get_all()
    nguoi_dung_list = NguoiDung.get_all()

    current_user = list(filter(
        lambda user: user["ND_TAI_KHOAN"] == request.cookies.get("ND_MA") or "", nguoi_dung_list))
    current_user = current_user[0] if len(current_user) else None

    # get user for template
    _ = list(filter(lambda nd: str(nd.get('ND_MA')) ==
                    request.cookies.get("ND_MA"), nguoi_dung_list))

    ND_TAI_KHOAN = _[0].get("ND_TAI_KHOAN") if len(_) > 0 else None
    user_info = {
        "ND_TAI_KHOAN": ND_TAI_KHOAN,
    }
    # get user for template

    return render_template(
        "add_thuc_pham.html",
        user_info=user_info,
        food_list=food_list,
        user=current_user,
        # unit_list=unit_list
    )


@route.route('/dang-ky', methods=['POST'])
def tp_dang_ky_mua():
    print("ok")
    query_string_dict = request.values
    new_dang_ky_mua = {
        "ND_MA": query_string_dict.get("txtNDMa"),
        "TP_MA": query_string_dict.get("txtTPMa"),
        "DKM_SO_LUONG": query_string_dict.get("numSoLuongDangKy"),
    }
    DangKyMua.create(new_dang_ky_mua)
    # return str(new_dang_ky_mua)
    # print(new_dang_ky_mua)
    return redirect("/")
