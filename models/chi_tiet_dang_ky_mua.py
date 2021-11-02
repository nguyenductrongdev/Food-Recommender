from .db_utils import cursor, db


class ChiTietDangKyMua:

    def get_all():
        sql = """
        SELECT * 
        FROM chi_tiet_dang_ky_mua, dang_ky_mua, thuc_pham, nguoi_dung
        WHERE chi_tiet_dang_ky_mua.DKM_MA = dang_ky_mua.DKM_MA
            AND dang_ky_mua.ND_MA = nguoi_dung.ND_MA
            AND chi_tiet_dang_ky_mua.TP_MA = thuc_pham.TP_MA
        """
        cursor.execute(sql)
        return cursor.fetchall()

    def create(fields):
        CTDKM_SO_LUONG = fields["CTDKM_SO_LUONG"]
        CTDKM_GHI_CHU = fields["CTDKM_GHI_CHU"]
        TP_MA = fields["TP_MA"]
        DKM_MA = fields["DKM_MA"]

        sql = """
            INSERT INTO chi_tiet_dang_ky_mua(CTDKM_SO_LUONG, CTDKM_GHI_CHU, TP_MA, DKM_MA) 
            VALUES (%s, %s, %s, %s)
        """
        val = (CTDKM_SO_LUONG, CTDKM_GHI_CHU, TP_MA, DKM_MA)

        cursor.execute(sql, val)
        db.commit()
