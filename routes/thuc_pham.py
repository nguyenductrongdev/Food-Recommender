from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session

from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.dang_ky_mua import DangKyMua

from middlewares.require_login import require_login
from models.thuc_pham import ThucPham
import configparser
import uuid
import os


route = Blueprint(
    'thuc_pham',
    __name__,
    template_folder='templates',
)

config = configparser.ConfigParser()
CONFIG_PATH = os.path.abspath("./config.ini")
config.read(CONFIG_PATH)


def get_user_info():
    nguoi_dung_list = NguoiDung.get_all()
    try:
        # get user for template
        user_info = list(
            filter(lambda nd: str(nd.get('ND_MA')) ==
                   request.cookies.get("ND_MA"), nguoi_dung_list)
        )[0]

        # get user for template
        return user_info
    except Exception as e:
        return None


@route.route('/<tp_ma>', methods=['GET'])
@require_login()
def tp_index(tp_ma):
    food_list = ThucPham.get_all()
    registered_list = DangKyMua.get_all()

    food = list(
        filter(lambda food: food.get("TP_MA") == int(tp_ma), food_list)
    )[0]

    user_info = get_user_info()

    is_registered = [
        register
        for register in registered_list
        if str(register["TP_MA"]) == str(tp_ma) and str(register["ND_MA"]) == str(user_info["ND_MA"])
    ]
    is_registered = len(is_registered) == 1

    role = "registered" if is_registered else "normal_customer"

    return render_template(
        "food.html",
        food=food,
        user_info=user_info,
        role=role,
    )


@route.route('/them', methods=['GET'])
@require_login()
def add_thuc_pham():
    food_list = DanhMucThucPham.get_all()
    user_info = get_user_info()

    # get user for template
    return render_template(
        "add_thuc_pham.html",
        user_info=user_info,
        food_list=food_list,
    )


@route.route('/them', methods=['POST'])
def post_them_thuc_pham():
    """
        Create thuc pham
    """
    try:
        query_string_dict = request.values
        file = request.files.get('fHinhAnh')
        file_ext = file.filename.split('.')[-1]
        file_path = os.path.join(
            config['APP']['UPLOAD_FOLDER'], f"{str(uuid.uuid4())}.{file_ext}")

        new_thuc_pham = {
            "ND_MA": request.cookies.get("ND_MA") or query_string_dict.get("ND_MA"),
            "DMTP_MA": query_string_dict.get("slLoaiThucPham"),
            "TP_TEN": query_string_dict.get("txtTenThucPham"),
            "TP_MO_TA": query_string_dict.get("txtMoTa"),
            "TP_HINH_ANH": file_path,
            "TP_DON_GIA": query_string_dict.get("numDonGia"),
            "TP_SO_LUONG": query_string_dict.get("numSoLuong"),
            "DMDVT_MA": query_string_dict.get("slDonVi"),
            "TP_VI_TRI_BAN_DO": query_string_dict.get("txtViTriBanDo"),
            "TP_NGAY_BAN": query_string_dict.get("txtNgayBan"),
            "TP_DIA_CHI": query_string_dict.get("txtAddress"),
            "TP_SO_LUONG_BAN_SI": query_string_dict.get("numSoLuongBanSi"),
        }
        ThucPham.create(new_thuc_pham)
        file.save(file_path)
        print(new_thuc_pham)
        return redirect("/thuc-pham/them")
    except Exception as e:
        raise


@route.route('/dang-ky', methods=['POST'])
def tp_dang_ky_mua():
    print("ok")
    query_string_dict = request.values
    new_dang_ky_mua = {
        "ND_MA": query_string_dict.get("txtNDMa"),

        "TP_MA": query_string_dict.get("txtTPMa"),
        "DKM_THOI_GIAN": query_string_dict.get("txtThoiGian"),
        "DKM_SO_LUONG": query_string_dict.get("numSoLuongDangKy"),
        "DKM_GHI_CHU": query_string_dict.get("txtNote"),
        "DKM_DIA_CHI": query_string_dict.get("txtAddress"),
        "DKM_VI_TRI_BAN_DO": query_string_dict.get("txtViTriBanDo"),
    }
    DangKyMua.create(new_dang_ky_mua)
    return redirect("/")
