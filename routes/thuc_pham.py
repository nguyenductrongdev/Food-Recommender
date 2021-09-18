from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session

from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung

route = Blueprint(
    'thuc_pham',
    __name__,
    template_folder='templates',
)


@route.route('/them', methods=['GET'])
def add_thuc_pham():
    food_list = DanhMucThucPham.get_all()
    unit_list = DanhMucDonViTinh.get_all()
    user_list = NguoiDung.get_all()

    current_user = list(filter(
        lambda user: user["ND_TAI_KHOAN"] == request.cookies.get("ND_MA") or "", user_list))
    current_user = current_user[0] if len(current_user) else None

    return render_template("add_thuc_pham.html", food_list=food_list, user=current_user, unit_list=unit_list)
