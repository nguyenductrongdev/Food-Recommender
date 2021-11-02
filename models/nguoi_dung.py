import logging

from .db_utils import cursor, db


class NguoiDung:
    def create(new_user: dict):
        try:
            ND_TAI_KHOAN = new_user["ND_TAI_KHOAN"]
            ND_MAT_KHAU = new_user["ND_MAT_KHAU"]

            ND_HO_TEN = new_user.get("ND_HO_TEN", None)
            ND_DIA_CHI = new_user.get("ND_DIA_CHI", None)
            ND_SO_DIEN_THOAI = new_user.get("ND_SO_DIEN_THOAI", None)
            ND_EMAIL = new_user.get("ND_EMAIL", None)

            sql = """
                INSERT INTO nguoi_dung(ND_TAI_KHOAN, ND_MAT_KHAU, ND_HO_TEN, ND_DIA_CHI, ND_SO_DIEN_THOAI, ND_EMAIL) 
                VALUES(%s, %s, %s, %s, %s, %s)
            """
            val = (ND_TAI_KHOAN, ND_MAT_KHAU, ND_HO_TEN, ND_DIA_CHI,
                   ND_SO_DIEN_THOAI, ND_EMAIL)

            cursor.execute(sql, val)
            db.commit()

            logging.getLogger("__main__").info(
                f"create {ND_TAI_KHOAN} success")
        except Exception as e:
            logging.getLogger("__main__").exception(e)
            raise

    def get_all():
        try:
            sql = "SELECT * FROM nguoi_dung"
            cursor.execute(sql)
            return cursor.fetchall()
        except Exception as e:
            logging.getLogger("__main__").exception(e)
            raise

    def find_by_id(nd_ma: int) -> dict:
        find = [
            user
            for user in NguoiDung.get_all()
            if int(user["ND_MA"]) == int(nd_ma)
        ]
        return find[0] if len(find) == 1 else None
