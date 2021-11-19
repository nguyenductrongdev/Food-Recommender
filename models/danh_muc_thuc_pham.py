from .db_utils import cursor


class DanhMucThucPham:

    def get_all():
        cursor.execute("SELECT * FROM danh_muc_thuc_pham")
        food_list = cursor.fetchall()
        return food_list

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
