import logging

from .db_utils import cursor, db


class ThucPham:
    def create(fields):
        try:
            ND_MA = fields["ND_MA"]
            LTP_MA = fields["LTP_MA"]
            TP_MO_TA = fields["TP_MO_TA"]
            TP_HINH_ANH = fields["TP_HINH_ANH"]
            TP_DON_GIA = fields["TP_DON_GIA"]
            TP_SO_LUONG = fields["TP_SO_LUONG"]
            TP_DON_VI = fields["TP_DON_VI"]
            sql = """
                INSERT INTO thuc_pham(ND_MA, LTP_MA, TP_MO_TA, TP_HINH_ANH, TP_DON_GIA, TP_SO_LUONG, TP_DON_VI) 
                VALUES(%s, %s, %s, %s, %s, %s, %s)
            """
            pram = (ND_MA, LTP_MA, TP_MO_TA, TP_HINH_ANH,
                    TP_DON_GIA, TP_SO_LUONG, TP_DON_VI)

            cursor.execute(sql, pram)
            db.commit()
        except Exception as e:
            logging.getLogger("__main__").exception(e)
            return None
