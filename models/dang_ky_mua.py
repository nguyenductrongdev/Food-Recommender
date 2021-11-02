from .db_utils import cursor, db


class DangKyMua:

    def get_all():
        sql = """
        SELECT * 
        FROM dang_ky_mua, nguoi_dung 
        WHERE dang_ky_mua.ND_MA = nguoi_dung.ND_MA
        """
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

    def update(data):
        # record is identified by nd_ma and tp_ma
        nd_ma = data["ND_MA"]
        tp_ma = data["TP_MA"]
        del data["ND_MA"]
        del data["TP_MA"]

        cols = data.keys()
        _params = [*data.values()]
        _conditions = [nd_ma, tp_ma]

        sql = f"""
            UPDATE dang_ky_mua
            SET {" ".join([f"{col} = %s" for col in cols])}
            WHERE ND_MA = %s AND TP_MA = %s
        """
        print(sql)
        cursor.execute(sql, [*_params, *_conditions])
        db.commit()

    def find(nd_ma: int, tp_ma: int) -> dict:
        register_list = DangKyMua.get_all()
        find = [
            register
            for register in register_list
            if int(register["ND_MA"]) == int(nd_ma) and int(register["TP_MA"]) == int(tp_ma)
        ]
        return find[0] if len(find) == 1 else None
