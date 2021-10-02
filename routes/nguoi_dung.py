from middlewares.require_login import require_login
from flask import Blueprint, request, abort, jsonify, url_for, render_template, redirect, flash, send_file, session, make_response
from jinja2 import TemplateNotFound
import logging

from models.nguoi_dung import NguoiDung
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh

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
    # get user for template
    _ = list(filter(lambda nd: str(nd.get('ND_MA')) ==
                    request.cookies.get("ND_MA"), nguoi_dung_list))

    ND_TAI_KHOAN = _[0].get("ND_TAI_KHOAN") if len(_) > 0 else None
    user_info = {
        "ND_TAI_KHOAN": ND_TAI_KHOAN,
    }
    # get user for template
    food_type_list = DanhMucThucPham.get_all()
    unit_list = DanhMucDonViTinh.get_all()
    return render_template(
        "add_request.html",
        user_info=user_info,
        food_type_list=food_type_list,
        unit_list=unit_list,
        user_list=nguoi_dung_list,
    )


@route.route('/<nd_tai_khoan>', methods=['GET'])
@require_login()
def private_page(nd_tai_khoan):
    nguoi_dung_list = NguoiDung.get_all()

    # get user for template
    _ = list(filter(lambda nd: str(nd.get('ND_TAI_KHOAN')) ==
                    nd_tai_khoan, nguoi_dung_list))

    ND_TAI_KHOAN = _[0].get("ND_TAI_KHOAN") if len(_) > 0 else None
    user_info = {
        "ND_TAI_KHOAN": ND_TAI_KHOAN,
    }
    # get user for template
    return render_template(
        "user.html",
        user_info=user_info,
    )
