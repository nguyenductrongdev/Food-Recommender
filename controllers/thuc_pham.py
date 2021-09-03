from flask import Flask, request, jsonify, url_for, render_template, redirect, flash, send_file, session

from models.loai_thuc_pham import LoaiThucPham


def add_thuc_pham():
    food_list = LoaiThucPham.get_all()
    return render_template("add_thuc_pham.html", food_list=food_list)
