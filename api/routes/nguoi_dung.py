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
            "DMTP_MA": query_string_dict["slDanhMucThucPham"],
            "CTNCM_SO_LUONG": query_string_dict["numSoLuong"],
            "DMDVT_MA": query_string_dict["slDonVi"],
            "NCM_THOI_GIAN": query_string_dict["txtThoiGian"],
        }
        NhuCauMua.create(newRequest)
        return {"message": "Success"}, 200
    except Exception as e:
        return {"message": "Error"}, 500
