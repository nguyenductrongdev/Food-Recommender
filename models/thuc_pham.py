import logging

from .db_utils import cursor, db


class ThucPham:
    def create(fields):
        # print(fields)
        # return
        try:
            ND_MA = fields["ND_MA"]
            DMTP_MA = fields["DMTP_MA"]
            TP_TEN = fields["TP_TEN"]
            TP_MO_TA = fields["TP_MO_TA"]
            TP_HINH_ANH = fields["TP_HINH_ANH"]
            TP_DON_GIA = fields["TP_DON_GIA"]
            DMDVT_MA = fields["DMDVT_MA"]
            TP_SO_LUONG = fields["TP_SO_LUONG"]
            TP_NGAY_BAN = fields["TP_NGAY_BAN"]
            TP_VI_TRI_BAN_DO = fields["TP_VI_TRI_BAN_DO"]
            TP_DIA_CHI = fields["TP_DIA_CHI"]
            TP_SO_LUONG_BAN_SI = fields["TP_SO_LUONG_BAN_SI"] or None
            sql = """
                INSERT INTO thuc_pham(ND_MA, DMTP_MA, TP_TEN, TP_MO_TA, TP_HINH_ANH, TP_DON_GIA, DMDVT_MA, TP_SO_LUONG, TP_NGAY_BAN, TP_VI_TRI_BAN_DO, TP_DIA_CHI, TP_SO_LUONG_BAN_SI) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            pram = (ND_MA, DMTP_MA, TP_TEN, TP_MO_TA, TP_HINH_ANH,
                    TP_DON_GIA, DMDVT_MA, TP_SO_LUONG, TP_NGAY_BAN, TP_VI_TRI_BAN_DO, TP_DIA_CHI, TP_SO_LUONG_BAN_SI)
            cursor.execute(sql, pram)
            db.commit()
        except Exception as e:
            logging.getLogger("__main__").exception(e)
            raise

    def get_all():
        sql = """
            SELECT * 
            FROM thuc_pham, danh_muc_thuc_pham, danh_muc_don_vi_tinh, nguoi_dung
            WHERE thuc_pham.DMDVT_MA = danh_muc_don_vi_tinh.DMDVT_MA
                AND thuc_pham.DMTP_MA = danh_muc_thuc_pham.DMTP_MA
                AND thuc_pham.ND_MA = nguoi_dung.ND_MA
        """

        cursor.execute(sql)
        return cursor.fetchall()
