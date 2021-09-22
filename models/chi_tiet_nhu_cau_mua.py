from .db_utils import cursor, db


class ChiTietNhuCauMua:
    def get_all():
        cursor.execute("SELECT * FROM danh_muc_don_vi_tinh")
        food_list = cursor.fetchall()
        return food_list

    def create(fields):
        print("fields", fields)
        DMTP_MA = fields["DMTP_MA"]
        NCM_MA = fields["NCM_MA"]
        CTNCM_SO_LUONG = fields["CTNCM_SO_LUONG"]

        sql = """
            INSERT INTO chi_tiet_nhu_cau_mua(DMTP_MA, NCM_MA, CTNCM_SO_LUONG) VALUES (%s, %s, %s)
        """
        val = (DMTP_MA, NCM_MA, CTNCM_SO_LUONG)

        cursor.execute(sql, val)
        db.commit()
