from .db_utils import cursor, db


class DanhMucThucPham:

    def get_all():
        cursor.execute("SELECT * FROM danh_muc_thuc_pham")
        food_list = cursor.fetchall()
        return food_list

    def create(fields):
        DMTP_TEN = fields['DMTP_TEN']
        DMTP_MA_DMTM_CHA = fields['DMTP_MA_DMTM_CHA']

        sql = """
            INSERT INTO danh_muc_thuc_pham(DMTP_TEN, DMTP_MA_DMTM_CHA)
            VALUES(%s, %s)
        """

        params = (DMTP_TEN, DMTP_MA_DMTM_CHA)
        cursor.execute(sql, params)
        db.commit()

    def update(data: dict):
        dmtvt_ma = data.pop("DMTP_MA")
        cols = data.keys()
        params = [*data.values(), dmtvt_ma]

        sql = f"""
            UPDATE danh_muc_thuc_pham
            SET {", ".join([f"{col} = %s" for col in cols])}
            WHERE DMTP_MA = %s
        """
        cursor.execute(sql, params)
        db.commit()

    def utils_get_leafs() -> list:
        db_danh_muc_thuc_pham_all = DanhMucThucPham.get_all()

        def dmtp_is_leaf(dmtp: dict) -> bool:
            parent_list = [
                *map(lambda item: item["DMTP_MA_DMTM_CHA"], db_danh_muc_thuc_pham_all)
            ]
            # leaf is not parent anywhere and have parent
            return dmtp["DMTP_MA"] not in parent_list and dmtp["DMTP_MA_DMTM_CHA"]

        # filter dmtp, just get leaf node
        dmtp_leaf = [
            *filter(dmtp_is_leaf, db_danh_muc_thuc_pham_all)
        ]
        return dmtp_leaf
