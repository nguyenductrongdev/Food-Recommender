from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session
import configparser
import uuid
import os
import json

from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.dang_ky_mua import DangKyMua
from models.chi_tiet_dang_ky_mua import ChiTietDangKyMua
from models.thuc_pham import ThucPham

from middlewares.require_login import require_login
from utils import get_user_info

from recommend_kits import update_recommend_data

route = Blueprint(
    'thuc_pham',
    __name__,
    template_folder='templates',
)

config = configparser.ConfigParser()
CONFIG_PATH = os.path.abspath("./config.ini")
config.read(CONFIG_PATH)


@route.route('/<tp_ma>', methods=['GET'])
def tp_index(tp_ma):
    try:
        registered_detail_list = ChiTietDangKyMua.get_all()
        # get current list
        food = ThucPham.find(TP_MA=int(tp_ma))

        role = "not_login"
        # get all register already to handle
        ready_registered_list = [
            register_detail
            for register_detail in registered_detail_list
            if int(register_detail["TP_MA"]) == int(tp_ma) and
            not register_detail["CTDKM_TRANG_THAI"] and
            int(register_detail["CTDKM_SO_LUONG"]) <= int(food["TP_SO_LUONG"]) and
            int(register_detail["CTDKM_SO_LUONG"]) % (
                food["TP_SUAT_BAN"] or 1) == 0
        ]

        unready_registered_list = [
            register_detail
            for register_detail in registered_detail_list
            # match tp_ma
            if int(register_detail["TP_MA"]) == int(tp_ma) and
            # status not buy
            not register_detail["CTDKM_TRANG_THAI"] and
            # cannot buy cause number of
            (int(register_detail["CTDKM_SO_LUONG"]) %
             (food["TP_SUAT_BAN"] or 1) != 0)
        ]
        # print("[DEBUG] unready_registered_list",
        #       unready_registered_list[0])

        try:
            user_info = get_user_info()

            is_registered = [
                register
                for register in registered_detail_list
                if str(register["TP_MA"]) == str(tp_ma) and
                str(register["ND_MA"]) == str(user_info["ND_MA"]) and
                not register["DKM_TRANG_THAI"]
            ]
            is_registered = len(is_registered) == 1

            if int(user_info["ND_MA"]) == int(food["ND_MA"]):
                role = "owner"
            elif is_registered:
                role = "registered"
            else:
                role = "normal_customer"
        except Exception as e:
            pass

        unready_registered_list = [
            *map(lambda x: {**x, }, unready_registered_list)]

        return render_template(
            "food.html",
            food=food,
            user_info=user_info,
            role=role,
            ready_registered_list=ready_registered_list,
            # just display List da dang ky for bcf
            unready_registered_list=unready_registered_list if food["TP_SUAT_BAN"] else None,
        )
    except Exception as e:
        pass


@ route.route('/them', methods=['GET'])
@ require_login()
def add_thuc_pham():
    food_list = DanhMucThucPham.get_all()
    user_info = get_user_info()

    # get user for template
    return render_template(
        "add_thuc_pham.html",
        user_info=user_info,
        food_list=food_list,
    )


@ route.route('/them', methods=['POST'])
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
            "TP_SUAT_BAN": query_string_dict.get("numSoLuongBanSi"),
        }
        ThucPham.create(new_thuc_pham)
        file.save(file_path)
        print(new_thuc_pham)
        return redirect("/thuc-pham/them")
    except Exception as e:
        raise


@route.route('/cap-nhat/<int:tp_ma>', methods=['GET'])
def food_update_ui(tp_ma):
    user_info = get_user_info()
    food = ThucPham.find(TP_MA=int(tp_ma))

    return render_template(
        "food_update.html",
        user_info=user_info,
        food=food,
    )


@route.route('/cap-nhat/<int:tp_ma>', methods=['POST'])
def food_update(tp_ma):
    # Get new value from BE
    query_string_dict = request.values
    update_data = {
        "TP_TEN": query_string_dict["txtTenThucPham"],
        "TP_SO_LUONG": query_string_dict["numSoLuong"],
        "TP_DON_GIA": query_string_dict["numDonGia"],
        "TP_DIA_CHI": query_string_dict["txtAddress"],
        "TP_MO_TA": query_string_dict["txtMoTa"],
        "TP_VI_TRI_BAN_DO": query_string_dict["txtViTriBanDo"],
    }
    ThucPham.update({
        "TP_MA": tp_ma,
        **update_data
    })
    return redirect(f"/thuc-pham/{tp_ma}")


@route.route('/dang-ky', methods=['POST'])
def tp_dang_ky_mua():
    """
        Add food register and details by form, add just one ctncm
    """
    TEST_MODE = False

    query_string_dict = request.values

    """
        UPDATE MySQL database:
        - Read from browser
        - Update into MySQL database
    """
    new_dang_ky_mua = {
        "ND_MA": query_string_dict.get("txtNDMa"),

        "DKM_THOI_GIAN": query_string_dict.get("txtThoiGian"),
        "DKM_DIA_CHI": query_string_dict.get("txtAddress"),
        "DKM_VI_TRI_BAN_DO": query_string_dict.get("txtViTriBanDo"),
    }

    REGISTER_CREATED = DangKyMua.create(
        new_dang_ky_mua) if not TEST_MODE else {"DKM_MA": -1}

    new_chi_tiet_dang_ky_mua = {
        "TP_MA": query_string_dict.get("txtTPMa"),
        "DKM_MA": REGISTER_CREATED["DKM_MA"],

        "CTDKM_SO_LUONG": query_string_dict.get("numSoLuongDangKy"),
        "CTDKM_GHI_CHU": query_string_dict.get("txtNote"),
    }
    # print(f"[DEBUG] new_chi_tiet_dang_ky_mua {new_chi_tiet_dang_ky_mua}")
    not TEST_MODE and ChiTietDangKyMua.create(new_chi_tiet_dang_ky_mua)

    """
        UPDATE MONGODB:
        - Read from MySQL database and generate cluster
        - Update cluster into MongoDB database
    """
    tp_ma = int(query_string_dict["txtTPMa"])
    if ThucPham.find(TP_MA=tp_ma).get("TP_SUAT_BAN"):
        update_recommend_data(tp_ma=tp_ma)

    return redirect("/")
