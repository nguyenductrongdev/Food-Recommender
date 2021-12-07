from .db_utils import cursor, db


class DanhMucDonViTinh:

    def get_all():
        cursor.execute("SELECT * FROM danh_muc_don_vi_tinh")
        food_list = cursor.fetchall()
        return food_list

    # def update(data):
    #     dmtvt_ma = data.pop("DMDVT_MA")

    #     cols = data.keys()
    #     params = [*data.values(), dmtvt_ma]

    #     sql = f"""
    #         UPDATE danh_muc_don_vi_tinh
    #         SET {", ".join([f"{col} = %s" for col in cols])}
    #         WHERE DMDVT_MA = %s
    #     """
    #     print(sql)
    #     cursor.execute(sql, params)
    #     db.commit()
