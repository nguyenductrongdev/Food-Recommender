from models.thuc_pham import ThucPham
from middlewares.require_login import require_login
from flask import Blueprint, request, abort, jsonify, url_for, render_template, redirect, flash, send_file, session, make_response
from jinja2 import TemplateNotFound
import logging

from models.chi_tiet_nhu_cau_mua import ChiTietNhuCauMua
from models.nguoi_dung import NguoiDung
from models.danh_muc_thuc_pham import DanhMucThucPham
from models.danh_muc_don_vi_tinh import DanhMucDonViTinh
from models.nhu_cau_mua import NhuCauMua
from utils import get_user_info

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


@route.route('/nhu-cau-mua', methods=['GET'])
def nhu_cau_mua():
    nguoi_dung_list = NguoiDung.get_all()
    food_requests = NhuCauMua.get_all()
    requests_details = ChiTietNhuCauMua.get_all()

    def get_request_details(req_ma):
        return list(filter(lambda req_detail: int(req_detail["NCM_MA"]) == int(req_ma), requests_details))

    for i in range(len(food_requests)):
        # get request_details
        req_details = get_request_details(food_requests[i]["NCM_MA"])
        food_requests[i].update({
            "details": req_details,
        })

    # get user for template
    _ = list(filter(lambda nd: str(nd.get('ND_MA')) ==
                    request.cookies.get("ND_MA"), nguoi_dung_list))

    ND_TAI_KHOAN = _[0].get("ND_TAI_KHOAN") if len(_) > 0 else None
    user_info = {
        "ND_TAI_KHOAN": ND_TAI_KHOAN,
    }
    # get user for template

    return render_template(
        "food_requests.html",
        food_requests=food_requests,
        user_info=user_info
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


@route.route(r'/<nd_tai_khoan>/cua-hang', methods=['GET'])
@require_login()
def shop(nd_tai_khoan):
    nguoi_dung_list = NguoiDung.get_all()
    thuc_pham_list = ThucPham.get_all()
    danh_muc_thuc_pham_list = DanhMucThucPham.get_all()

    # get user for template
    try:
        ND_TAI_KHOAN = list(filter(lambda nd: str(nd.get('ND_MA')) ==
                                   request.cookies.get("ND_MA"), nguoi_dung_list))[0].get("ND_TAI_KHOAN")
        user_info = {
            "ND_TAI_KHOAN": ND_TAI_KHOAN,
        }
    except:
        user_info = None
    # get user for template

    food_list = list(
        filter(lambda food: food["ND_TAI_KHOAN"] == nd_tai_khoan, thuc_pham_list))
    return render_template(
        "shop.html",
        user_info=user_info,
        food_list=food_list,
    )


@route.route('/goi-y-mua-chung', methods=['GET'])
def recommend_page():
    from recommend_kits import recommand_for_big_cube_food
    food_list = ThucPham.get_all()
    user_info = get_user_info()
    # get all recommend for all big cube foods
    recommends = recommand_for_big_cube_food()

    def get_tp_by_tp_ma(tp_ma: int):
        find = [
            food
            for food in food_list
            if int(food["TP_MA"]) == int(tp_ma)
        ]
        return find[0] if len(find) == 1 else None

    # consider the recommend contain current user as alert
    alerts = []
    for tp_ma, user_ids in recommends.items():
        if int(user_info["ND_MA"]) not in user_ids:
            continue

        tp = get_tp_by_tp_ma(tp_ma=tp_ma)
        alerts.append({
            "TP_TEN": tp["TP_TEN"],
        })
    print("alerts", alerts)

    return render_template(
        "recommends.html",
        user_info=user_info,
        alerts=alerts,
    )
