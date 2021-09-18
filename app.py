import configparser
import os
from flask import Flask, request, jsonify, url_for, render_template, redirect, flash, send_file, session
import logging
from pythonjsonlogger import jsonlogger


from routes.nguoi_dung import route as nguoi_dung_route
from routes.thuc_pham import route as thuc_pham_route

from api.routes.thuc_pham import route as api_thuc_pham_route


from models.thuc_pham import ThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nguoi_dung import NguoiDung
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.thuc_pham import ThucPham


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


@app.route('/', methods=['GET'])
def index():
    # food_list = ThucPham.get_all()
    # user_list = NguoiDung.get_all()
    # food_type_list = DanhMucThucPham.get_all()

    # # food_list with extra field
    # for i, food in enumerate(food_list):
    #     ND_TAI_KHOAN = user_list[user_list == ]

    #     DMTP_TEN = ""

    #     food_list[i].update({
    #         "ND_TAI_KHOAN": ND_TAI_KHOAN,
    #         "DMTP_TEN": DMTP_TEN,
    #     })

    food_list = []
    return render_template("index.html", food_list=food_list)


@app.route('/food-map', methods=['GET'])
def food_map():

    food_list = ThucPham.get_all()
    danh_muc_thuc_pham_list = DanhMucThucPham.get_all()
    danh_muc_don_vi_tinh_list = DanhMucDonViTinh.get_all()

    geo_location_list = []
    info_in_location = []

    for food in food_list:
        longitude, latitude = food.get("TP_VI_TRI_BAN_DO").split("|")
        geo_location_list.append({
            "longitude": longitude,
            "latitude": latitude,
        })

        DMDVT_TEN = list(filter(lambda dmdvt: dmdvt.get("DMDVT_MA") ==
                                food.get("DMDVT_MA"), danh_muc_don_vi_tinh_list))[0].get("DMDVT_TEN")
        DMTP_TEN = list(filter(lambda dmtp: dmtp.get("DMTP_MA") ==
                               food.get("DMTP_MA"), danh_muc_thuc_pham_list))[0].get("DMTP_TEN")

        info_in_location.append({
            "TP_NGAY_BAN": food.get("TP_NGAY_BAN"),
            "DMTP_TEN": DMTP_TEN,
            "TP_SO_LUONG": food.get("TP_SO_LUONG"),
            "DMDVT_TEN": DMDVT_TEN,
        })

    print(info_in_location)

    return render_template("food_map.html", geo_location_list=geo_location_list, lengthLocation=len(geo_location_list), information_in_location=info_in_location)


# Non-API routes
app.register_blueprint(thuc_pham_route, url_prefix='/thuc-pham')
app.register_blueprint(nguoi_dung_route, url_prefix='/nguoi-dung')

# API routes
app.register_blueprint(api_thuc_pham_route, url_prefix='/api/thuc-pham')


if __name__ == "__main__":
    app.run(debug=True)
