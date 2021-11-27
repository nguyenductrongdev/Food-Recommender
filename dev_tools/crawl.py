from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import re
from time import sleep
from unidecode import unidecode
import json
import os
import pandas as pd

import logging
from pythonjsonlogger import jsonlogger


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

hdlr = logging.FileHandler("crawl.log")
stream_hdr = logging.StreamHandler()

fmt = jsonlogger.JsonFormatter(
    "%(levelname)s %(asctime)s %(filename)s %(lineno)s %(message)s"
)
hdlr.setFormatter(fmt)
stream_hdr.setFormatter(fmt)

log.addHandler(hdlr)
log.addHandler(stream_hdr)

browser = webdriver.Chrome(ChromeDriverManager().install())

BASE_URL = "https://thucphamnhanh.com/"
CRAWL_RESULT_FOLDER = "crawl_result"

URLs_FILE = "urls.xlsx"
PRODUCTs_FILE = "products.xlsx"

categories = [
    {"path": "rau-cu-qua", "max_page": 7},
    {"path": "thuc-pham-che-bien", "max_page": 12},
    {"path": "thuc-pham-tuoi-song", "max_page": 11},
    {"path": "thuc-pham-gia-vi", "max_page": 4},
    {"path": "luong-thuc", "max_page": 4},
    {"path": "banh-keo-mut", "max_page": 1},
    {"path": "thuc-pham-dong-hop", "max_page": 2},
    {"path": "dac-san", "max_page": 2},
    {"path": "san-pham-khac", "max_page": 1},
]


def build_xlsx():
    browser.get(BASE_URL)

    categories_page_urls = []
    detail_page = []
    category_name_list = []

    for category in categories:
        path = category["path"]
        max_page = category["max_page"]
        categories_page_urls += [
            {
                "category_name": category["path"],
                "url": f"https://thucphamnhanh.com/{path}/page/{page}/"
            }
            for page in range(1, max_page+1)
        ]

    for item in categories_page_urls:
        # get url and category name of category page
        url = item["url"]
        category_name = item["category_name"]

        # get url in self tab
        browser.execute_script(f"""window.open("{url}", "_self")""")
        # sleep for load page
        sleep(3)
        # get detail pages
        a_tags = browser.find_elements_by_css_selector(
            ".image-fade_in_back > a")
        for tag in a_tags:
            detail_page += [tag.get_attribute("href")]
            category_name_list += [category_name]

    df = pd.DataFrame({
        "url": detail_page,
        "category_name": category_name_list,
    })

    df.to_excel(URLs_FILE)

    browser.close()


def remove_html_tags(txt):
    p = re.compile(r'<.*?>')
    return p.sub('', txt)


def build_products_data():
    browser.get(BASE_URL)

    df = pd.read_excel(URLs_FILE)
    products = []

    for index, row in df.iterrows():
        detail_page_url = row["url"]

        # get detail page
        browser.execute_script(
            f"""window.open("{detail_page_url}", "_self")"""
        )
        sleep(1.5)

        product = {}

        product["url"] = detail_page_url

        try:
            # get information
            try:
                category_path = browser.find_element_by_css_selector(
                    ".is-medium"
                ).get_attribute("innerHTML")

                product["category"] = remove_html_tags(category_path)
            except Exception as e:
                product["category"] = ""

            # get title
            try:
                product["title"] = browser.find_element_by_css_selector(
                    ".product_title").get_attribute('innerHTML').replace("\n", "")

                # raw data, include price and unit
                raw_data = browser.find_element_by_xpath(
                    """/html/body/div[1]/main/div/div[2]/div/div[2]/div[1]/div/div[2]/p[1]"""
                ).get_attribute("innerHTML")
            except Exception as e:
                product["title"] = None
                log.error(f"[crawl {index+1}] title failed")

            # get price
            try:
                product["price"] = str(
                    re.search(
                        r"[\d\.]+", remove_html_tags(raw_data)
                    )[0].replace(".", "")
                )
                log.info(f"[crawl {index+1}] price success")
            except Exception as e:
                product["price"] = None
                log.error(f"[crawl {index+1}] price failed")

            # get unit
            try:
                product["unit"] = str(raw_data[raw_data.rindex("/")+1:])
                log.info(f"[crawl {index+1}] unit success")
            except Exception as e:
                product["unit"] = None
                log.error(f"[crawl {index+1}] unit failed")

            # get image url
            try:
                product["img_url"] = str(browser.find_element_by_css_selector(
                    ".container + .product > div > div.col.large-9 > div.product-main > div > div.large-6.col > div.row.row-small > div > div > figure > div > div > div > a > img"
                ).get_attribute("src"))
                log.info(f"[crawl {index+1}] img_url success")
            except Exception as e:
                product["img_url"] = None
                log.error(f"[crawl {index+1}] img_url failed")

            # get description (keep html because suitable for CKEDITOR)
            try:
                product["description"] = str(
                    remove_html_tags(
                        browser.find_element_by_css_selector(
                            "#tab-description"
                        ).get_attribute("innerHTML")
                    )
                )
                log.info(f"[crawl {index+1}] description success")
            except Exception as e:
                product["description"] = ""
                log.error(f"[crawl {index+1}] description failed")

            products.append(product)

            log.info(
                f"[crawl {index+1}] price success",
                extra={"new_product_info": product}
            )

            log.info(f"Crawl succes {index+1}/{len(df)}")

        except Exception as e:
            log.exception(f"[ERROR] {detail_page_url} {e}")
            pass

    pd.DataFrame(products).to_excel(PRODUCTs_FILE)

    browser.close()


if __name__ == "__main__":
    if not os.path.exists(URLs_FILE):
        print(f"[INFO]: not exist {URLs_FILE}")
        build_xlsx()
    if not os.path.exists(PRODUCTs_FILE):
        print(f"[INFO]: not exist {PRODUCTs_FILE}")
        build_products_data()
