import math
from functools import wraps
import configparser
import os
from flask import Flask, request, jsonify, url_for, render_template, redirect, flash, send_file, session
import logging
from models.dang_ky_mua import DangKyMua
from pythonjsonlogger import jsonlogger
from flask import g


from routes.nguoi_dung import route as nguoi_dung_route
from routes.thuc_pham import route as thuc_pham_route

from api.routes.thuc_pham import route as api_thuc_pham_route
from api.routes.nguoi_dung import route as api_nguoi_dung_route


from models.thuc_pham import ThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.thuc_pham import ThucPham

from utils import get_user_info
import sys

# append to view db_utils
sys.path.append(os.path.abspath("./models/"))


app = Flask(__name__)

config = configparser.ConfigParser()
CONFIG_PATH = os.path.abspath("./config.ini")
config.read(CONFIG_PATH)
app.config['UPLOAD_FOLDER'] = config['APP']['UPLOAD_FOLDER']

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
hdlr = logging.FileHandler("log/system.log")
fmt = jsonlogger.JsonFormatter(
    "%(levelname)s %(asctime)s %(filename)s %(lineno)s %(message)s")
hdlr.setFormatter(fmt)
log.addHandler(hdlr)


@app.route('/admin', methods=['GET'])
def admin_page():

    return render_template(
        "admin.html",
        dmtp_list=DanhMucThucPham.get_all(),
    )


@app.route('/', methods=['GET'])
def index():
    nguoi_dung_list = NguoiDung.get_all()
    thuc_pham_list = ThucPham.get_all()
    danh_muc_thuc_pham_list = DanhMucThucPham.get_all()
    # print(danh_muc_thuc_pham_list)

    def dmtp_is_leaf(dmtp):
        # print(dmtp)
        parent_list = [
            *map(lambda item: item["DMTP_MA_DMTM_CHA"], danh_muc_thuc_pham_list)
        ]
        # leaf is not parent anywhere and have parent
        return dmtp["DMTP_MA"] not in parent_list and dmtp["DMTP_MA_DMTM_CHA"]

    # filter dmtp, just get leaf node
    dmtp_leaf = [
        *filter(dmtp_is_leaf, danh_muc_thuc_pham_list)
    ]

    user_info = get_user_info()

    return render_template(
        "index.html",
        user_info=user_info,
        food_list=thuc_pham_list[:20],
        user_list=nguoi_dung_list,
        danh_muc_thuc_pham_list=dmtp_leaf,

        max_of_price=max(
            thuc_pham_list,
            key=lambda food: food["TP_DON_GIA"]
        )["TP_DON_GIA"],
    )


@app.route('/checkout', methods=['GET'])
def checkout():
    user_info = get_user_info()
    return render_template(
        'checkout.html',
        user_info=user_info,
    )


@app.route('/food-map/', methods=['GET'])
def food_map():
    food_list = ThucPham.get_all()
    danh_muc_thuc_pham_list = DanhMucThucPham.get_all()
    target_dmtp = None

    def _get_leafs():
        parent_list = [
            *map(lambda item: item["DMTP_MA_DMTM_CHA"], danh_muc_thuc_pham_list)
        ]

        def dmtp_is_leaf(dmtp):
            # leaf is not parent anywhere and have parent
            return dmtp["DMTP_MA"] not in parent_list and dmtp["DMTP_MA_DMTM_CHA"]

        # filter dmtp, just get leaf node
        dmtp_leaf = [
            *filter(dmtp_is_leaf, danh_muc_thuc_pham_list)
        ]
        return dmtp_leaf

    query_string_dict = request.values
    if query_string_dict.get("dmtp_ma"):
        food_list = [
            *filter(lambda food: int(food["DMTP_MA"]) == int(query_string_dict.get("dmtp_ma")), food_list)
        ]
        target_dmtp = [
            dmtp
            for dmtp in DanhMucThucPham.get_all()
            if int(dmtp.get("DMTP_MA")) == int(query_string_dict.get("dmtp_ma"))
        ][0]

    custom_food_list = []

    def _is_number(n):
        try:
            float(n)
            return True
        except:
            return False

    for i, food in enumerate(food_list):
        longitude, latitude = food.get("TP_VI_TRI_BAN_DO").split("|")
        if not _is_number(longitude) or not _is_number(latitude):
            continue

        custom_food_list.append({
            **food,
            "longitude": longitude,
            "latitude": latitude,
        })

    return render_template(
        "food_map.html",
        user_info=get_user_info(),
        custom_food_list=custom_food_list,
        dmtp_list=_get_leafs(),
        target_dmtp=target_dmtp,
    )


@app.route(r'/api/unit')
def get_unit():
    from models.db_utils import cursor, db
    DMTP_MA = request.args.get("dmtp_ma")
    sql = f"""
        SELECT danh_muc_don_vi_tinh.DMDVT_MA, DMDVT_TEN
        FROM danh_muc_thuc_pham, danh_muc_don_vi_tinh, dm_don_vi_tinh_dm_thuc_pham
        WHERE danh_muc_thuc_pham.DMTP_MA = {DMTP_MA}
            AND danh_muc_thuc_pham.DMTP_MA = dm_don_vi_tinh_dm_thuc_pham.DMTP_MA
            AND dm_don_vi_tinh_dm_thuc_pham.DMDVT_MA = danh_muc_don_vi_tinh.DMDVT_MA
    """
    cursor.execute(sql)
    units = cursor.fetchall()
    return {
        "units": units
    }, 200


# Non-API routes
app.register_blueprint(thuc_pham_route, url_prefix='/thuc-pham')
app.register_blueprint(nguoi_dung_route, url_prefix='/nguoi-dung')

# API routes
app.register_blueprint(api_thuc_pham_route, url_prefix='/api/thuc-pham')
app.register_blueprint(api_nguoi_dung_route, url_prefix='/api/nguoi-dung')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
