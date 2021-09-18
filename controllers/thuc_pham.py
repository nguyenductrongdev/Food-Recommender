from flask import Flask, request, jsonify, url_for, render_template, redirect, flash, send_file, session

from models.loai_thuc_pham import LoaiThucPham
from models.nguoi_dung import NguoiDung


def add_thuc_pham():
    food_list = LoaiThucPham.get_all()

    user_list = NguoiDung.get_all()

    current_user = list(filter(
        lambda user: user["ND_TAI_KHOAN"] == request.cookies.get("ND_MA") or "", user_list))
    current_user = current_user[0] if len(current_user) else None

    return render_template("add_thuc_pham.html", food_list=food_list, user=current_user)
