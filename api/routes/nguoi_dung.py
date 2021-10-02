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
