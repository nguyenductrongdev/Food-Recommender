from .db_utils import cursor


class LoaiThucPham:

    def get_all():
        cursor.execute("SELECT * FROM loai_thuc_pham")
        food_list = cursor.fetchall()
        return food_list
