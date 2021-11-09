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
            TP_SUAT_BAN = fields["TP_SUAT_BAN"] or None
            sql = """
                INSERT INTO thuc_pham(ND_MA, DMTP_MA, TP_TEN, TP_MO_TA, TP_HINH_ANH, TP_DON_GIA, DMDVT_MA, TP_SO_LUONG, TP_NGAY_BAN, TP_VI_TRI_BAN_DO, TP_DIA_CHI, TP_SUAT_BAN) 
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            pram = (ND_MA, DMTP_MA, TP_TEN, TP_MO_TA, TP_HINH_ANH,
                    TP_DON_GIA, DMDVT_MA, TP_SO_LUONG, TP_NGAY_BAN, TP_VI_TRI_BAN_DO, TP_DIA_CHI, TP_SUAT_BAN)
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

    def find(**col_filter):
        WHITE_LIST = ["TP_MA"]
        WHITE_LIST += [*map(lambda e: e.lower(), WHITE_LIST)]

        food_list = ThucPham.get_all()
        # all filter target must into white list
        assert all([
            f in WHITE_LIST
            for f in col_filter.keys()
        ])
        tp_ma = col_filter.get("tp_ma") or col_filter.get("TP_MA")
        # filter for tp_ma (tp_ma is primary key)
        if tp_ma:
            find = [
                food
                for food in food_list
                if int(food["TP_MA"]) == int(tp_ma)
            ]
            return find[0] if len(find) == 1 else None

    def update(data):
        tp_ma = data["TP_MA"]
        del data["TP_MA"]

        cols = data.keys()
        params = [*data.values(), tp_ma]

        sql = f"""
            UPDATE thuc_pham
            SET {", ".join([f"{col} = %s" for col in cols])}
            WHERE TP_MA = %s
        """
        print(sql)
        cursor.execute(sql, params)
        db.commit()
