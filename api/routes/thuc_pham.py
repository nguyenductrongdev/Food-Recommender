from functools import wraps
import uuid
import os
import logging
import configparser
from flask import Blueprint, Flask, request,  jsonify, url_for, render_template, redirect, flash, send_file, session

from models.thuc_pham import ThucPham

route = Blueprint(
    'api_thuc_pham',
    __name__,
)


config = configparser.ConfigParser()
CONFIG_PATH = os.path.abspath("./config.ini")
config.read(CONFIG_PATH)


@route.route('/', methods=['GET'])
def index():
    thuc_pham_list = ThucPham.get_all()
    query_string_dict = request.values

    nd_ma = query_string_dict.get("nd_ma")
    dmtp_ma = query_string_dict.get("dmtp_ma")

    if nd_ma:
        thuc_pham_list = list(filter(
            lambda food: food.get("ND_MA") == int(nd_ma), thuc_pham_list))

    if dmtp_ma:
        thuc_pham_list = list(filter(
            lambda food: food.get("DMTP_MA") == int(dmtp_ma), thuc_pham_list))

    return {
        "foods": thuc_pham_list
    }
