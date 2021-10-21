from .db_utils import cursor, db


class ChiTietNhuCauMua:
    def get_all():
        sql = """
            SELECT * 
            FROM chi_tiet_nhu_cau_mua, danh_muc_don_vi_tinh, danh_muc_thuc_pham 
            WHERE chi_tiet_nhu_cau_mua.dmdvt_ma = danh_muc_don_vi_tinh.dmdvt_ma
                AND chi_tiet_nhu_cau_mua.dmtp_ma = danh_muc_thuc_pham.dmtp_ma
        """
        print(sql)
        cursor.execute(sql)
        food_list = cursor.fetchall()
        return food_list

    def create(fields):
        print("fields", fields)
        DMTP_MA = fields["DMTP_MA"]
        NCM_MA = fields["NCM_MA"]
        CTNCM_SO_LUONG = fields["CTNCM_SO_LUONG"]
        DMDVT_MA = fields["DMDVT_MA"]

        sql = """
            INSERT INTO chi_tiet_nhu_cau_mua(DMTP_MA, NCM_MA, CTNCM_SO_LUONG, DMDVT_MA) 
            VALUES (%s, %s, %s, %s)
        """
        val = (DMTP_MA, NCM_MA, CTNCM_SO_LUONG, DMDVT_MA)

        cursor.execute(sql, val)
        db.commit()
