from werkzeug.wrappers import Response
from flask import request, jsonify, url_for, render_template, redirect, flash, send_file, session, make_response
import logging

from models.nguoi_dung import NguoiDung


def login():
    """
        Render login page
    """
    return render_template("login.html")


def register():
    """
        Render register page
    """
    return render_template("register.html")


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
            "ND_SO_DIEN_THOAI": query_string_dict.get("txPhone", None),
            "ND_EMAIL": query_string_dict.get("txEmail", None),
        }
        NguoiDung.create(new_user)
        return {
            "query_string_dict": query_string_dict,
            "message": "Đăng ký thành công",
        }
    except Exception as e:
        logging.getLogger("__main__").exception(e)


def post_login():
    """
        Handle request from form data
    """
    try:
        query_string_dict = request.values

        username = query_string_dict["txtTaiKhoan"]
        password = query_string_dict["txtMatKhau"]

        user_list = NguoiDung.get_all()
        # return {
        #     "user_list": user_list,
        # }
        # find current user
        current_user = list(filter(
            lambda user: user["ND_TAI_KHOAN"] == username and user["ND_MAT_KHAU"] == password, user_list))
        current_user = current_user[0] if len(current_user) else None
        # set behavior depending on user
        if current_user:
            print("xxxxxxxxxxxxxx", current_user)
            response = make_response(render_template(
                "user.html", user=current_user))
            response.set_cookie('ND_MA', str(current_user["ND_MA"]))
            return response
        else:
            return redirect('/nguoi-dung/dang-nhap')
    except Exception as e:
        logging.getLogger("__main__").exception(e)
        raise
        # return redirect('/nguoi-dung/dang-nhap')
