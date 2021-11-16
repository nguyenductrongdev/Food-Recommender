from .db_utils import cursor, db


class BinhLuan:

    def get_all():
        sql = """
            SELECT * 
            FROM binh_luan, nguoi_dung 
            WHERE binh_luan.ND_MA = nguoi_dung.ND_MA
        """
        cursor.execute(sql)
        return cursor.fetchall()

    def create(fields):
        ND_MA = fields["ND_MA"]
        TP_MA = fields["TP_MA"]
        BL_NOI_DUNG = fields["BL_NOI_DUNG"]
        BL_THOI_GIAN = fields["BL_THOI_GIAN"]

        sql = """
            INSERT INTO binh_luan(ND_MA, TP_MA, BL_NOI_DUNG, BL_THOI_GIAN) 
            VALUES (%s, %s, %s, %s)
        """
        val = (ND_MA, TP_MA, BL_NOI_DUNG, BL_THOI_GIAN)
        cursor.execute(sql, val)
        db.commit()
