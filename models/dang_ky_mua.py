from .db_utils import cursor, db


class DangKyMua:

    def create(fields):
        ND_MA = fields["ND_MA"]
        TP_MA = fields["TP_MA"]
        DKM_SO_LUONG = fields["DKM_SO_LUONG"]

        sql = """
            INSERT INTO dang_ky_mua(ND_MA, TP_MA, DKM_SO_LUONG) 
            VALUES (%s, %s, %s)
        """
        val = (ND_MA, TP_MA, DKM_SO_LUONG)

        cursor.execute(sql, val)
        db.commit()
