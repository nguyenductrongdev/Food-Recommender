from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session

from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.dang_ky_mua import DangKyMua
from models.thuc_pham import ThucPham


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
