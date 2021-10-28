from .db_utils import cursor, db


class DangKyMua:

    def get_all():
        sql = "SELECT * FROM dang_ky_mua"
        cursor.execute(sql)
        return cursor.fetchall()

    def create(fields):
        ND_MA = fields["ND_MA"]
        TP_MA = fields["TP_MA"]
        DKM_SO_LUONG = fields["DKM_SO_LUONG"]
        DKM_GHI_CHU = fields["DKM_GHI_CHU"]
        DKM_THOI_GIAN = fields["DKM_THOI_GIAN"]

        DKM_DIA_CHI = fields["DKM_DIA_CHI"]
        DKM_VI_TRI_BAN_DO = fields["DKM_VI_TRI_BAN_DO"]

        sql = """
            INSERT INTO dang_ky_mua(ND_MA, TP_MA, DKM_SO_LUONG, DKM_THOI_GIAN, DKM_GHI_CHU, DKM_DIA_CHI, DKM_VI_TRI_BAN_DO) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        val = (ND_MA, TP_MA, DKM_SO_LUONG, DKM_THOI_GIAN,
               DKM_GHI_CHU, DKM_DIA_CHI, DKM_VI_TRI_BAN_DO)

        cursor.execute(sql, val)
        db.commit()
