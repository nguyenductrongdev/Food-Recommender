from .db_utils import cursor


class DanhMucDonViTinh:

    def get_all():
        cursor.execute("SELECT * FROM danh_muc_don_vi_tinh")
        food_list = cursor.fetchall()
        return food_list
