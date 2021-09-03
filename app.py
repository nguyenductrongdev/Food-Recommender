import configparser
import os
from flask import Flask, request, jsonify, url_for, render_template, redirect, flash, send_file, session
import logging
from pythonjsonlogger import jsonlogger

from models.loai_thuc_pham import LoaiThucPham
from models.thuc_pham import ThucPham

from controllers.nguoi_dung import login, post_login, register, post_register
from controllers.thuc_pham import add_thuc_pham

from api.controllers.thuc_pham import api_them_thuc_pham

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


def index():
    return render_template("index.html")


app.add_url_rule("/", view_func=index)

app.add_url_rule("/nguoi-dung/dang-nhap", view_func=login, methods=["GET"])
app.add_url_rule("/nguoi-dung/dang-nhap",
                 view_func=post_login, methods=["POST"])

app.add_url_rule("/nguoi-dung/dang-ky", view_func=register, methods=["GET"])
app.add_url_rule("/nguoi-dung/dang-ky",
                 view_func=post_register, methods=["POST"])

app.add_url_rule("/thuc-pham/them",
                 view_func=add_thuc_pham, methods=['GET'])

app.add_url_rule("/api/thuc-pham/them",
                 view_func=api_them_thuc_pham, methods=['POST'])


if __name__ == "__main__":
    app.run(debug=True)
