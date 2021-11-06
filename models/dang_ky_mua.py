from .db_utils import cursor, db


class DangKyMua:

    def get_all():
        sql = """
        SELECT * 
        FROM dang_ky_mua, chi_tiet_dang_ky_mua, nguoi_dung, thuc_pham 
        WHERE dang_ky_mua.ND_MA = nguoi_dung.ND_MA
            AND dang_ky_mua.DKM_MA = chi_tiet_dang_ky_mua.DKM_MA
            AND chi_tiet_dang_ky_mua.TP_MA = thuc_pham.TP_MA
        """
        cursor.execute(sql)
        return cursor.fetchall()

    def create(fields):
        # ND_MA move to optional for khach van lai
        ND_MA = fields.get("ND_MA")
        DKM_THOI_GIAN = fields["DKM_THOI_GIAN"]
        DKM_DIA_CHI = fields["DKM_DIA_CHI"]
        DKM_VI_TRI_BAN_DO = fields["DKM_VI_TRI_BAN_DO"]

        sql = """
            INSERT INTO dang_ky_mua(ND_MA, DKM_THOI_GIAN, DKM_DIA_CHI, DKM_VI_TRI_BAN_DO) 
            VALUES (%s, %s, %s, %s)
        """
        val = (ND_MA, DKM_THOI_GIAN, DKM_DIA_CHI, DKM_VI_TRI_BAN_DO)

        cursor.execute(sql, val)
        db.commit()
        return {
            "DKM_MA": cursor.lastrowid,
        }

    def update(**data):
        # record is identified by nd_ma and tp_ma
        dkm_ma = data["DKM_MA"]
        del data["DKM_MA"]

        cols = data.keys()
        _params = data.values()

        cols = data.keys()

        sql = f"""
            UPDATE dang_ky_mua
            SET {" ".join([f"{col} = %s" for col in cols])}
            WHERE DKM_MA = %s
        """
        print(sql)
        cursor.execute(sql, [*_params, dkm_ma])
