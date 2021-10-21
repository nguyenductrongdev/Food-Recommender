import logging

from .db_utils import cursor, db


class NhuCauMua:
    def get_all():
        sql = """
            SELECT * 
            FROM nhu_cau_mua
        """
        cursor.execute(sql)
        return cursor.fetchall()

    def create(new_request: dict):
        print("new_request", new_request)
        ND_MA = new_request.get('ND_MA')
        NCM_THOI_GIAN = new_request.get('NCM_THOI_GIAN')
        sql = """
            INSERT INTO nhu_cau_mua(ND_MA, NCM_THOI_GIAN) 
            VALUES (%s, %s)
        """
        param = (ND_MA, NCM_THOI_GIAN)

        cursor.execute(sql, param)
        db.commit()
        return {
            "NCM_MA": cursor.lastrowid,
        }
