import configparser
import logging
import os
from flask import Flask, request, jsonify, url_for, render_template, redirect, flash, send_file, session
import uuid

from models.thuc_pham import ThucPham

config = configparser.ConfigParser()
CONFIG_PATH = os.path.abspath("./config.ini")
config.read(CONFIG_PATH)


def api_them_thuc_pham():
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
            "LTP_MA": query_string_dict.get("slLoaiThucPham"),
            "TP_MO_TA": query_string_dict.get("txtMoTa"),
            "TP_HINH_ANH": file_path,
            "TP_DON_GIA": query_string_dict.get("numDonGia"),
            "TP_SO_LUONG": query_string_dict.get("numSoLuong"),
            "TP_DON_VI": query_string_dict.get("slDonVi"),
        }

        ThucPham.create(new_thuc_pham)
        file.save(file_path)
        return {
            "result": new_thuc_pham,
            "message": "Thêm thành công",
        }
    except Exception as e:
        logging.getLogger("__main__").exception(e)
        return {"message": "Có lỗi xảy ra"}, 500
