import logging

from .db_utils import cursor, db


class NhuCauMua:
    def create(new_request: dict):
        print("new_request", new_request)
        ND_MA = new_request.get('ND_MA')
        DMTP_MA = new_request.get('DMDVT_MA')
        CTNCM_SO_LUONG = new_request.get('CTNCM_SO_LUONG')
        DMDVT_MA = new_request.get('DMDVT_MA')
        NCM_THOI_GIAN = new_request.get('NCM_THOI_GIAN')
        sql = """
            INSERT INTO nhu_cau_mua(NCM_MA, ND_MA, NCM_THOI_GIAN) 
            VALUES (%s, %s, %s)
        """
        param = (ND_MA, DMDVT_MA, NCM_THOI_GIAN)
        cursor.execute(sql, param)

        # insert to ncm_dmtm
        NCM_MA = cursor.lastrowid
        sql = """
            INSERT INTO chi_tiet_nhu_cau_mua(DMTP_MA, NCM_MA, CTNCM_SO_LUONG) 
            VALUES (%s, %s, %s)
        """
        param = (DMTP_MA, NCM_MA, CTNCM_SO_LUONG)
        cursor.execute(sql, param)

        db.commit()
