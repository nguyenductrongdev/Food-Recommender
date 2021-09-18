from .db_utils import cursor


class DanhMucThucPham:

    def get_all():
        cursor.execute("SELECT * FROM danh_muc_thuc_pham")
        food_list = cursor.fetchall()
        return food_list
