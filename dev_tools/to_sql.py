import urllib3
import datetime
import math
import re
import os
from typing import Counter
import pandas as pd
import numpy as np
from uuid import uuid4
import urllib.request


product_df = pd.read_excel("products.xlsx", index_col=[0])

TABLE_NGUOI_DUNG = []
TABLE_THUC_PHAM = []
TABLE_DANH_MUC_THUC_PHAM = []
TABLE_DANH_MUC_DON_VI_TINH = []


def generate_geo():
    df = pd.read_excel("./locations-plus.xlsx")
    max_index = len(df) - 1
    index = 0
    while True:
        yield dict(df.iloc[index])
        if index == max_index:
            index = 0
        index += 1


def generate_ND():
    mock_data = [
        {
            "ND_HO_TEN": "Christin Arnaudot",
            "ND_EMAIL": "carnaudot0@opensource.org",
            "ND_SO_DIEN_THOAI": "6289518344"
        }, {
            "ND_HO_TEN": "Ronni Puckring",
            "ND_EMAIL": "rpuckring1@pen.io",
            "ND_SO_DIEN_THOAI": "1985645779"
        }, {
            "ND_HO_TEN": "Tani Gunston",
            "ND_EMAIL": "tgunston2@npr.org",
            "ND_SO_DIEN_THOAI": "5131704945"
        }, {
            "ND_HO_TEN": "Audra Ropkes",
            "ND_EMAIL": "aropkes3@accuweather.com",
            "ND_SO_DIEN_THOAI": "2973307232"
        }, {
            "ND_HO_TEN": "Magdalene Bartoszewicz",
            "ND_EMAIL": "mbartoszewicz4@microsoft.com",
            "ND_SO_DIEN_THOAI": "8146458653"
        }, {
            "ND_HO_TEN": "Berenice Melhuish",
            "ND_EMAIL": "bmelhuish5@bizjournals.com",
            "ND_SO_DIEN_THOAI": "6695437491"
        }, {
            "ND_HO_TEN": "Janie Pardey",
            "ND_EMAIL": "jpardey6@is.gd",
            "ND_SO_DIEN_THOAI": "3178141748"
        }, {
            "ND_HO_TEN": "Winonah Smeath",
            "ND_EMAIL": "wsmeath7@chicagotribune.com",
            "ND_SO_DIEN_THOAI": "1758368330"
        }, {
            "ND_HO_TEN": "Korney Bergeau",
            "ND_EMAIL": "kbergeau8@myspace.com",
            "ND_SO_DIEN_THOAI": "6365472445"
        }, {
            "ND_HO_TEN": "Silvio Durrett",
            "ND_EMAIL": "sdurrett9@utexas.edu",
            "ND_SO_DIEN_THOAI": "5856605771"
        }, {
            "ND_HO_TEN": "Xavier Ollie",
            "ND_EMAIL": "xolliea@sciencedirect.com",
            "ND_SO_DIEN_THOAI": "1034991154"
        }, {
            "ND_HO_TEN": "Reade McCrea",
            "ND_EMAIL": "rmccreab@ted.com",
            "ND_SO_DIEN_THOAI": "8441546904"
        }, {
            "ND_HO_TEN": "Aldus Bunkle",
            "ND_EMAIL": "abunklec@cornell.edu",
            "ND_SO_DIEN_THOAI": "3417840993"
        }, {
            "ND_HO_TEN": "Conni Manthroppe",
            "ND_EMAIL": "cmanthropped@techcrunch.com",
            "ND_SO_DIEN_THOAI": "5076042810"
        }, {
            "ND_HO_TEN": "Mathew Mortimer",
            "ND_EMAIL": "mmortimere@ezinearticles.com",
            "ND_SO_DIEN_THOAI": "7791989843"
        }, {
            "ND_HO_TEN": "Reeva Blyth",
            "ND_EMAIL": "rblythf@php.net",
            "ND_SO_DIEN_THOAI": "8872015911"
        }, {
            "ND_HO_TEN": "Karole MacBey",
            "ND_EMAIL": "kmacbeyg@freewebs.com",
            "ND_SO_DIEN_THOAI": "5451604502"
        }, {
            "ND_HO_TEN": "Broddie Kendell",
            "ND_EMAIL": "bkendellh@de.vu",
            "ND_SO_DIEN_THOAI": "9834014484"
        }, {
            "ND_HO_TEN": "Ignace Faughny",
            "ND_EMAIL": "ifaughnyi@sohu.com",
            "ND_SO_DIEN_THOAI": "8102861775"
        }, {
            "ND_HO_TEN": "Randolf Jaycox",
            "ND_EMAIL": "rjaycoxj@npr.org",
            "ND_SO_DIEN_THOAI": "8525953601"
        }, {
            "ND_HO_TEN": "Alethea Weare",
            "ND_EMAIL": "awearek@arstechnica.com",
            "ND_SO_DIEN_THOAI": "5557665372"
        }, {
            "ND_HO_TEN": "Clarice Ardy",
            "ND_EMAIL": "cardyl@prweb.com",
            "ND_SO_DIEN_THOAI": "1047112675"
        }, {
            "ND_HO_TEN": "Harbert Levesque",
            "ND_EMAIL": "hlevesquem@businesswire.com",
            "ND_SO_DIEN_THOAI": "5603910119"
        }, {
            "ND_HO_TEN": "Brandise Cornewell",
            "ND_EMAIL": "bcornewelln@oaic.gov.au",
            "ND_SO_DIEN_THOAI": "2834936523"
        }, {
            "ND_HO_TEN": "Robina Isles",
            "ND_EMAIL": "risleso@virginia.edu",
            "ND_SO_DIEN_THOAI": "6733053058"
        }, {
            "ND_HO_TEN": "Randi Donke",
            "ND_EMAIL": "rdonkep@sourceforge.net",
            "ND_SO_DIEN_THOAI": "4594369281"
        }, {
            "ND_HO_TEN": "Lenore Seawright",
            "ND_EMAIL": "lseawrightq@nationalgeographic.com",
            "ND_SO_DIEN_THOAI": "5062602781"
        }, {
            "ND_HO_TEN": "Waverley Stalley",
            "ND_EMAIL": "wstalleyr@umich.edu",
            "ND_SO_DIEN_THOAI": "9527433239"
        }, {
            "ND_HO_TEN": "Delly Matteau",
            "ND_EMAIL": "dmatteaus@cbsnews.com",
            "ND_SO_DIEN_THOAI": "2567509131"
        }, {
            "ND_HO_TEN": "Craggie Golly",
            "ND_EMAIL": "cgollyt@shinystat.com",
            "ND_SO_DIEN_THOAI": "5077252758"
        }, {
            "ND_HO_TEN": "Claudine Peake",
            "ND_EMAIL": "cpeakeu@ihg.com",
            "ND_SO_DIEN_THOAI": "3655675899"
        }, {
            "ND_HO_TEN": "Sam Zannuto",
            "ND_EMAIL": "szannutov@europa.eu",
            "ND_SO_DIEN_THOAI": "6652354840"
        }, {
            "ND_HO_TEN": "Lian Simak",
            "ND_EMAIL": "lsimakw@scientificamerican.com",
            "ND_SO_DIEN_THOAI": "5691813334"
        }, {
            "ND_HO_TEN": "Camila Trusler",
            "ND_EMAIL": "ctruslerx@lycos.com",
            "ND_SO_DIEN_THOAI": "5774963449"
        }, {
            "ND_HO_TEN": "Marven Tregona",
            "ND_EMAIL": "mtregonay@wisc.edu",
            "ND_SO_DIEN_THOAI": "4262099892"
        }, {
            "ND_HO_TEN": "Shanan Castellini",
            "ND_EMAIL": "scastelliniz@nytimes.com",
            "ND_SO_DIEN_THOAI": "1331720422"
        }, {
            "ND_HO_TEN": "Brion Alderwick",
            "ND_EMAIL": "balderwick10@ucoz.ru",
            "ND_SO_DIEN_THOAI": "1571156245"
        }, {
            "ND_HO_TEN": "Maud Fobidge",
            "ND_EMAIL": "mfobidge11@psu.edu",
            "ND_SO_DIEN_THOAI": "1671311997"
        }, {
            "ND_HO_TEN": "Lawry Weymont",
            "ND_EMAIL": "lweymont12@posterous.com",
            "ND_SO_DIEN_THOAI": "4394441686"
        }, {
            "ND_HO_TEN": "Aluin Roskelly",
            "ND_EMAIL": "aroskelly13@fema.gov",
            "ND_SO_DIEN_THOAI": "7551462182"
        }, {
            "ND_HO_TEN": "Joey Cottey",
            "ND_EMAIL": "jcottey14@msu.edu",
            "ND_SO_DIEN_THOAI": "5111821525"
        }, {
            "ND_HO_TEN": "Addy Otson",
            "ND_EMAIL": "aotson15@over-blog.com",
            "ND_SO_DIEN_THOAI": "4785197788"
        }, {
            "ND_HO_TEN": "Renata Gossage",
            "ND_EMAIL": "rgossage16@joomla.org",
            "ND_SO_DIEN_THOAI": "9543587797"
        }, {
            "ND_HO_TEN": "Zechariah Gower",
            "ND_EMAIL": "zgower17@mapquest.com",
            "ND_SO_DIEN_THOAI": "5575409349"
        }, {
            "ND_HO_TEN": "Pavlov Hallatt",
            "ND_EMAIL": "phallatt18@nps.gov",
            "ND_SO_DIEN_THOAI": "7096181640"
        }, {
            "ND_HO_TEN": "Arley McRill",
            "ND_EMAIL": "amcrill19@gov.uk",
            "ND_SO_DIEN_THOAI": "7601323675"
        }, {
            "ND_HO_TEN": "Arlen Gossington",
            "ND_EMAIL": "agossington1a@utexas.edu",
            "ND_SO_DIEN_THOAI": "5331069733"
        }, {
            "ND_HO_TEN": "Vonny Ciccoloi",
            "ND_EMAIL": "vciccoloi1b@paginegialle.it",
            "ND_SO_DIEN_THOAI": "7522757857"
        }, {
            "ND_HO_TEN": "Ragnar Graffin",
            "ND_EMAIL": "rgraffin1c@sun.com",
            "ND_SO_DIEN_THOAI": "6304057653"
        }, {
            "ND_HO_TEN": "Davine Shalloo",
            "ND_EMAIL": "dshalloo1d@ucoz.com",
            "ND_SO_DIEN_THOAI": "8304282257"
        }, {
            "ND_HO_TEN": "Umeko August",
            "ND_EMAIL": "uaugust1e@marriott.com",
            "ND_SO_DIEN_THOAI": "7463249870"
        }, {
            "ND_HO_TEN": "Junette Merwede",
            "ND_EMAIL": "jmerwede1f@yolasite.com",
            "ND_SO_DIEN_THOAI": "5872101359"
        }, {
            "ND_HO_TEN": "Jenda Sames",
            "ND_EMAIL": "jsames1g@deliciousdays.com",
            "ND_SO_DIEN_THOAI": "6146833198"
        }, {
            "ND_HO_TEN": "Kendall Noquet",
            "ND_EMAIL": "knoquet1h@msu.edu",
            "ND_SO_DIEN_THOAI": "2678144680"
        }, {
            "ND_HO_TEN": "Dyana Spackman",
            "ND_EMAIL": "dspackman1i@github.io",
            "ND_SO_DIEN_THOAI": "9041216631"
        }, {
            "ND_HO_TEN": "Yancy Allonby",
            "ND_EMAIL": "yallonby1j@photobucket.com",
            "ND_SO_DIEN_THOAI": "6651177600"
        }, {
            "ND_HO_TEN": "Tabina Rotge",
            "ND_EMAIL": "trotge1k@msn.com",
            "ND_SO_DIEN_THOAI": "3539156176"
        }, {
            "ND_HO_TEN": "Franny Madgwick",
            "ND_EMAIL": "fmadgwick1l@abc.net.au",
            "ND_SO_DIEN_THOAI": "4155334591"
        }, {
            "ND_HO_TEN": "Marc de Bullion",
            "ND_EMAIL": "mde1m@unesco.org",
            "ND_SO_DIEN_THOAI": "3373813060"
        }, {
            "ND_HO_TEN": "Blanca Haggeth",
            "ND_EMAIL": "bhaggeth1n@t-online.de",
            "ND_SO_DIEN_THOAI": "7614904235"
        }, {
            "ND_HO_TEN": "Harcourt Godlonton",
            "ND_EMAIL": "hgodlonton1o@soundcloud.com",
            "ND_SO_DIEN_THOAI": "2706430241"
        }, {
            "ND_HO_TEN": "Lindsey Wankel",
            "ND_EMAIL": "lwankel1p@ustream.tv",
            "ND_SO_DIEN_THOAI": "6493176523"
        }, {
            "ND_HO_TEN": "Janeczka Huge",
            "ND_EMAIL": "jhuge1q@symantec.com",
            "ND_SO_DIEN_THOAI": "8985744310"
        }, {
            "ND_HO_TEN": "Jessey Culter",
            "ND_EMAIL": "jculter1r@globo.com",
            "ND_SO_DIEN_THOAI": "1908257300"
        }, {
            "ND_HO_TEN": "Ricky Pifford",
            "ND_EMAIL": "rpifford1s@canalblog.com",
            "ND_SO_DIEN_THOAI": "3736289182"
        }, {
            "ND_HO_TEN": "Tristan Coverdill",
            "ND_EMAIL": "tcoverdill1t@berkeley.edu",
            "ND_SO_DIEN_THOAI": "6588804171"
        }, {
            "ND_HO_TEN": "Guinevere Dawkes",
            "ND_EMAIL": "gdawkes1u@squidoo.com",
            "ND_SO_DIEN_THOAI": "8882588813"
        }, {
            "ND_HO_TEN": "Win Bevington",
            "ND_EMAIL": "wbevington1v@google.co.uk",
            "ND_SO_DIEN_THOAI": "5028042678"
        }, {
            "ND_HO_TEN": "Dacia Aldersley",
            "ND_EMAIL": "daldersley1w@craigslist.org",
            "ND_SO_DIEN_THOAI": "2834031414"
        }, {
            "ND_HO_TEN": "Hali Artrick",
            "ND_EMAIL": "hartrick1x@moonfruit.com",
            "ND_SO_DIEN_THOAI": "5636131759"
        }, {
            "ND_HO_TEN": "Devonne Suthren",
            "ND_EMAIL": "dsuthren1y@google.nl",
            "ND_SO_DIEN_THOAI": "2695347663"
        }, {
            "ND_HO_TEN": "Lydia Eberst",
            "ND_EMAIL": "leberst1z@state.tx.us",
            "ND_SO_DIEN_THOAI": "6062354509"
        }, {
            "ND_HO_TEN": "Bendicty Mallender",
            "ND_EMAIL": "bmallender20@boston.com",
            "ND_SO_DIEN_THOAI": "9804293331"
        }, {
            "ND_HO_TEN": "Alexia Frain",
            "ND_EMAIL": "afrain21@elegantthemes.com",
            "ND_SO_DIEN_THOAI": "3177372978"
        }, {
            "ND_HO_TEN": "Kathleen Goodrum",
            "ND_EMAIL": "kgoodrum22@oakley.com",
            "ND_SO_DIEN_THOAI": "7082112618"
        }, {
            "ND_HO_TEN": "Ossie Wyre",
            "ND_EMAIL": "owyre23@usnews.com",
            "ND_SO_DIEN_THOAI": "4294171694"
        }, {
            "ND_HO_TEN": "Lalo Randales",
            "ND_EMAIL": "lrandales24@unicef.org",
            "ND_SO_DIEN_THOAI": "8328565310"
        }, {
            "ND_HO_TEN": "Teriann Doughton",
            "ND_EMAIL": "tdoughton25@wired.com",
            "ND_SO_DIEN_THOAI": "8649649881"
        }, {
            "ND_HO_TEN": "Adina Ginsie",
            "ND_EMAIL": "aginsie26@telegraph.co.uk",
            "ND_SO_DIEN_THOAI": "2961973756"
        }, {
            "ND_HO_TEN": "Mozes Jakobsson",
            "ND_EMAIL": "mjakobsson27@twitpic.com",
            "ND_SO_DIEN_THOAI": "9566120848"
        }, {
            "ND_HO_TEN": "Miner Mahon",
            "ND_EMAIL": "mmahon28@samsung.com",
            "ND_SO_DIEN_THOAI": "7149953819"
        }, {
            "ND_HO_TEN": "Alexio Crum",
            "ND_EMAIL": "acrum29@java.com",
            "ND_SO_DIEN_THOAI": "2543157856"
        }, {
            "ND_HO_TEN": "Renault Egan",
            "ND_EMAIL": "regan2a@tinyurl.com",
            "ND_SO_DIEN_THOAI": "9575886128"
        }, {
            "ND_HO_TEN": "Abram Cartwright",
            "ND_EMAIL": "acartwright2b@theatlantic.com",
            "ND_SO_DIEN_THOAI": "1083864099"
        }, {
            "ND_HO_TEN": "Waring Preuvost",
            "ND_EMAIL": "wpreuvost2c@hc360.com",
            "ND_SO_DIEN_THOAI": "4588156224"
        }, {
            "ND_HO_TEN": "Benjamen Penritt",
            "ND_EMAIL": "bpenritt2d@addtoany.com",
            "ND_SO_DIEN_THOAI": "7859573058"
        }, {
            "ND_HO_TEN": "Keefer Gierck",
            "ND_EMAIL": "kgierck2e@cornell.edu",
            "ND_SO_DIEN_THOAI": "9295043905"
        }, {
            "ND_HO_TEN": "Stephana Crampin",
            "ND_EMAIL": "scrampin2f@army.mil",
            "ND_SO_DIEN_THOAI": "8166209544"
        }, {
            "ND_HO_TEN": "Scottie Corless",
            "ND_EMAIL": "scorless2g@ocn.ne.jp",
            "ND_SO_DIEN_THOAI": "1936945984"
        }, {
            "ND_HO_TEN": "Timi Scibsey",
            "ND_EMAIL": "tscibsey2h@answers.com",
            "ND_SO_DIEN_THOAI": "6436361033"
        }, {
            "ND_HO_TEN": "Gibby Carwithim",
            "ND_EMAIL": "gcarwithim2i@goo.gl",
            "ND_SO_DIEN_THOAI": "6108719018"
        }, {
            "ND_HO_TEN": "Violet Causier",
            "ND_EMAIL": "vcausier2j@purevolume.com",
            "ND_SO_DIEN_THOAI": "3801175525"
        }, {
            "ND_HO_TEN": "Andrus Loughney",
            "ND_EMAIL": "aloughney2k@furl.net",
            "ND_SO_DIEN_THOAI": "4489930423"
        }, {
            "ND_HO_TEN": "Kaela Copson",
            "ND_EMAIL": "kcopson2l@imageshack.us",
            "ND_SO_DIEN_THOAI": "7191874866"
        }, {
            "ND_HO_TEN": "Austina Monelli",
            "ND_EMAIL": "amonelli2m@shop-pro.jp",
            "ND_SO_DIEN_THOAI": "9592891332"
        }, {
            "ND_HO_TEN": "Daniella Pechan",
            "ND_EMAIL": "dpechan2n@sciencedirect.com",
            "ND_SO_DIEN_THOAI": "2048542712"
        }, {
            "ND_HO_TEN": "Ida Martyn",
            "ND_EMAIL": "imartyn2o@freewebs.com",
            "ND_SO_DIEN_THOAI": "4154087465"
        }, {
            "ND_HO_TEN": "Smitty Rolling",
            "ND_EMAIL": "srolling2p@spotify.com",
            "ND_SO_DIEN_THOAI": "7594051206"
        }, {
            "ND_HO_TEN": "Lebbie Massy",
            "ND_EMAIL": "lmassy2q@google.es",
            "ND_SO_DIEN_THOAI": "5372724240"
        }, {
            "ND_HO_TEN": "Forester Scimonelli",
            "ND_EMAIL": "fscimonelli2r@soundcloud.com",
            "ND_SO_DIEN_THOAI": "6881895986"
        }
    ]

    def gen():
        i = 1
        while True:
            yield i
            i += 1
    get_nd_ma = gen()

    sql = []
    for data in mock_data:
        ND_MA = next(get_nd_ma)
        ND_HO_TEN = data["ND_HO_TEN"]
        ND_EMAIL = data["ND_EMAIL"]
        ND_TAI_KHOAN = ND_EMAIL[:ND_EMAIL.index("@")]
        ND_MAT_KHAU = "12345678"
        ND_DIA_CHI = "Cần Thơ"
        ND_SO_DIEN_THOAI = "0" + data["ND_SO_DIEN_THOAI"][:-1]

        sql.append(
            re.sub(
                r"\s+", " ",
                f"""
                    INSERT INTO NGUOI_DUNG (ND_MA, ND_HO_TEN, ND_DIA_CHI, ND_SO_DIEN_THOAI, ND_EMAIL, ND_MAT_KHAU, ND_TAI_KHOAN)
                    VALUES ({ND_MA}, '{ND_HO_TEN}', '{ND_DIA_CHI}', '{ND_SO_DIEN_THOAI}',
                            '{ND_EMAIL}', '{ND_MAT_KHAU}', '{ND_TAI_KHOAN}')
                """.strip()
            )
        )

        TABLE_NGUOI_DUNG.append({
            "ND_MA": ND_MA, "ND_HO_TEN": ND_HO_TEN, "ND_DIA_CHI": ND_DIA_CHI,
            "ND_SO_DIEN_THOAI": ND_SO_DIEN_THOAI, "ND_MAT_KHAU": ND_MAT_KHAU, "ND_TAI_KHOAN": ND_TAI_KHOAN
        })

        with open("./ND.sql", "w", encoding="utf-8") as fp:
            fp.write("\n".join(sql))


def generate_DMTP():
    global TABLE_DANH_MUC_THUC_PHAM
    table = []
    print(product_df.columns)

    def gen():
        i = 1
        while True:
            yield i
            i += 1
    get_dmtp_ma = gen()

    sql = []

    # get skeleton
    category_list = product_df["category"].unique()
    parent_child_df = pd.DataFrame()
    for pair in category_list:
        try:
            parent = pair.split("/")[0].strip()
            children = pair.split("/")[1].strip()
        except:
            children = None
        finally:
            parent_child_df = parent_child_df.append(
                {"parent": parent, "children": children},
                ignore_index=True
            )
    # get root
    root_category = set([
        cate.split("/")[0].strip()
        for index, cate in enumerate(category_list)
    ])

    def get_dmtp_cha(name: str) -> int:
        parent_cate_name = parent_child_df[parent_child_df["children"] == name].to_dict(
            'records')[0]["parent"]

        for index, dmtp_ten in enumerate(root_category):
            if str(parent_cate_name) == str(dmtp_ten):
                return index + 1
        return None

    # get leaf
    sub_category = set()
    for cate in category_list:
        try:
            sub_category.add(cate.split("/")[1].strip())
        except:
            pass

    for index, category_name in enumerate(root_category):
        DMTP_MA = next(get_dmtp_ma)
        sql.append(
            re.sub(
                r"\s+", " ",
                f"""
                    INSERT INTO DANH_MUC_THUC_PHAM (DMTP_MA, DMTP_TEN, DMTP_MA_DMTM_CHA)
                    VALUES ({next(get_dmtp_ma)}, '{category_name}', NULL)
                """.strip()
            )
        )

        TABLE_DANH_MUC_THUC_PHAM.append({
            "DMTP_MA": DMTP_MA, "DMTP_TEN": category_name, "DMTP_MA_DMTM_CHA": None,
        })

    for category_name in sub_category:
        DMTP_MA = next(get_dmtp_ma)
        DMTP_MA_DMTM_CHA = get_dmtp_cha(category_name)

        sql.append(
            re.sub(
                r"\s+", " ",
                f"""
                    INSERT INTO DANH_MUC_THUC_PHAM (DMTP_MA, DMTP_TEN, DMTP_MA_DMTM_CHA)
                    VALUES ({DMTP_MA}, '{category_name}', {DMTP_MA_DMTM_CHA})
                """.strip()
            )
        )
        TABLE_DANH_MUC_THUC_PHAM.append({
            "DMTP_MA": DMTP_MA, "DMTP_TEN": category_name, "DMTP_MA_DMTM_CHA": DMTP_MA_DMTM_CHA,
        })

    with open("./DMTP.sql", "w", encoding="utf-8") as fp:
        fp.write("\n".join(sql))


def generate_TP():
    global TABLE_THUC_PHAM

    def id_gen():
        i = 1
        while True:
            yield i
            i += 1

    def user_id_gen():
        i = 0
        while True:
            i += 1
            if i == len(TABLE_NGUOI_DUNG):
                i = 0
            yield i

    get_tp_ma = id_gen()
    get_nd_ma = user_id_gen()
    get_geo_info = generate_geo()

    food_df = pd.read_excel("./products.xlsx")
    food_df['description'] = food_df['description'].fillna("")
    sql = []

    for _, food in food_df[:3].iterrows():
        try:
            TP_MA = next(get_tp_ma)

            unit_name = food["unit"]
            if ">" in unit_name:
                unit_name = "Kg"
            DMDVT_MA = [*filter(
                lambda dmdvt: str(dmdvt["DMDVT_TEN"]).lower() == str(
                    unit_name).lower(),
                TABLE_DANH_MUC_DON_VI_TINH
            )][0]["DMDVT_MA"]

            ND_MA = next(get_nd_ma)

            DMTP_MA = [*filter(
                lambda dmtp: dmtp["DMTP_TEN"] == food["category"].split(
                    "/")[-1].strip(),
                TABLE_DANH_MUC_THUC_PHAM
            )][0]["DMTP_MA"]

            TP_TEN = food["title"]
            TP_MO_TA = food["description"]

            # handle for image here
            filename = str(uuid4())

            # download file
            urllib.request.urlretrieve(
                food["url"],
                os.path.abspath(f"./crawl_images/{filename}")
            )

            TP_HINH_ANH = f"static/images/{filename}.jpg"
            TP_DON_GIA = f"""{food["price"]}0"""[:-6]
            TP_SO_LUONG = 500
            TP_NGAY_BAN = datetime.datetime.now().strftime("%Y-%m-%d")

            geo_info = next(get_geo_info)
            TP_VI_TRI_BAN_DO = f"""{geo_info["kinh_do"]}|{geo_info["vi_do"]}"""
            TP_DIA_CHI = geo_info["address"]
            TP_SUAT_BAN = "NULL"

            sql.append(
                re.sub(
                    r"\s+", " ",
                    f"""
                        INSERT INTO THUC_PHAM (TP_MA, DMDVT_MA, ND_MA, DMTP_MA, TP_TEN, TP_MO_TA, TP_HINH_ANH, TP_DON_GIA, TP_SO_LUONG, TP_NGAY_BAN, TP_VI_TRI_BAN_DO, TP_DIA_CHI, TP_SUAT_BAN)
                        VALUES ({TP_MA}, {DMDVT_MA}, {ND_MA}, {DMTP_MA}, '{TP_TEN}', '{TP_MO_TA}', '{TP_HINH_ANH}', {
                                TP_DON_GIA}, {TP_SO_LUONG}, '{TP_NGAY_BAN}', '{TP_VI_TRI_BAN_DO}', '{TP_DIA_CHI}', {TP_SUAT_BAN})
                    """.strip()
                )
            )
            TABLE_THUC_PHAM.append(
                {
                    "TP_MA": TP_MA, "DMTP_MA": DMTP_MA, "ND_MA": ND_MA,
                    "DMTP_MA": DMTP_MA, "TP_TEN": TP_TEN, "TP_MO_TA": TP_MO_TA,
                    "TP_HINH_ANH": TP_HINH_ANH, "TP_DON_GIA": TP_DON_GIA, "TP_SO_LUONG": TP_SO_LUONG,
                    "TP_NGAY_BAN": TP_NGAY_BAN, "TP_VI_TRI_BAN_DO": TP_VI_TRI_BAN_DO, "TP_DIA_CHI": TP_DIA_CHI,
                    "TP_SUAT_BAN": TP_SUAT_BAN,
                }
            )
            print(sql[-1])
        except:
            print(food)
            exit()

    with open("./TP.sql", "w", encoding="utf-8") as fp:
        fp.write("\n".join(sql))


def generate_DMDVT():
    global TABLE_DANH_MUC_DON_VI_TINH

    def gen():
        i = 1
        while True:
            yield i
            i += 1
    get_dmdvt_ma = gen()

    food_df = pd.read_excel("./products.xlsx")

    # temp col for del duplicate
    food_df["unit_lower"] = food_df['unit'].str.lower()

    # drop with insensitive
    food_df.drop_duplicates(subset=["unit_lower"], inplace=True)

    sql = []

    for unit_name in food_df["unit"].unique():
        if ">" in unit_name:
            continue

        DMTP_MA = next(get_dmdvt_ma)
        sql.append(
            re.sub(
                r"\s+", " ",
                f"""
                    INSERT INTO danh_muc_don_vi_tinh (DMDVT_MA, DMDVT_TEN)
                    VALUES ({DMTP_MA}, '{unit_name}')
                """.strip()
            )
        )
        TABLE_DANH_MUC_DON_VI_TINH.append(
            {"DMDVT_MA": DMTP_MA, "DMDVT_TEN": unit_name}
        )

    with open("./DMDVT.sql", "w", encoding="utf-8") as fp:
        fp.write("\n".join(sql))


def main():
    global TABLE_DANH_MUC_THUC_PHAM
    generate_DMTP()

    global TABLE_DANH_MUC_DON_VI_TINH
    generate_DMDVT()

    global TABLE_NGUOI_DUNG
    generate_ND()

    global TABLE_THUC_PHAM
    generate_TP()


if __name__ == "__main__":
    main()
