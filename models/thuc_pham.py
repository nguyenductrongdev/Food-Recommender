import logging

from .db_utils import cursor, db


class ThucPham:
    def create(fields):
        try:
            ND_MA = fields["ND_MA"]
            DMTP_MA = fields["DMTP_MA"]
            TP_MO_TA = fields["TP_MO_TA"]
            TP_HINH_ANH = fields["TP_HINH_ANH"]
            TP_DON_GIA = fields["TP_DON_GIA"]
            TP_SO_LUONG = fields["TP_SO_LUONG"]
            DMDVT_MA = fields["DMDVT_MA"]
            TP_NGAY_BAN = fields["TP_NGAY_BAN"]
            TP_VI_TRI_BAN_DO = fields["TP_VI_TRI_BAN_DO"]
            sql = """
                INSERT INTO thuc_pham(ND_MA, DMTP_MA, TP_MO_TA, TP_HINH_ANH, TP_DON_GIA, TP_SO_LUONG, DMDVT_MA, TP_NGAY_BAN, TP_VI_TRI_BAN_DO) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            pram = (ND_MA, DMTP_MA, TP_MO_TA, TP_HINH_ANH,
                    TP_DON_GIA, TP_SO_LUONG, DMDVT_MA, TP_NGAY_BAN, TP_VI_TRI_BAN_DO)
            print("fields*********", fields)
            cursor.execute(sql, pram)
            db.commit()
        except Exception as e:
            logging.getLogger("__main__").exception(e)
            raise

    def get_all():
        sql = "SELECT * FROM thuc_pham"
        cursor.execute(sql)
        return cursor.fetchall()
