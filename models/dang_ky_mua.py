from .db_utils import cursor, db


class DangKyMua:

    def create(fields):
        ND_MA = fields["ND_MA"]
        TP_MA = fields["TP_MA"]
        DKM_SO_LUONG = fields["DKM_SO_LUONG"]
        DKM_THOI_GIAN = fields["DKM_THOI_GIAN"]
        DKM_GHI_CHU = fields["DKM_GHI_CHU"]

        sql = """
            INSERT INTO dang_ky_mua(ND_MA, TP_MA, DKM_SO_LUONG, DKM_THOI_GIAN, DKM_GHI_CHU) 
            VALUES (%s, %s, %s, %s, %s)
        """
        val = (ND_MA, TP_MA, DKM_SO_LUONG, DKM_THOI_GIAN, DKM_GHI_CHU)

        cursor.execute(sql, val)
        db.commit()
