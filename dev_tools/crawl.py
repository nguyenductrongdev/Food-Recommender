from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import re
from time import sleep
from unidecode import unidecode
import json
import os
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())

BASE_URL = "https://thucphamnhanh.com/"
CRAWL_RESULT_FOLDER = "crawl_result"


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
    for category in categories:
        path = category["path"]
        max_page = category["max_page"]
        categories_page_urls += [
            f"https://thucphamnhanh.com/{path}/page/{page}/" for page in range(1, max_page+1)
        ]

    for url in categories_page_urls:
        # get url in self tab
        browser.execute_script(f"""window.open("{url}", "_self")""")
        # sleep for load page
        sleep(3)
        # get detail pages
        a_tags = browser.find_elements_by_css_selector(
            ".image-fade_in_back > a")
        for tag in a_tags:
            detail_page += [tag.get_attribute("href")]

    df = pd.DataFrame({
        "url": detail_page,
    })

    df.to_excel("result.xlsx")

    browser.close()


def remove_html_tags(txt):
    p = re.compile(r'<.*?>')
    return p.sub('', txt)


def build_products_data():
    browser.get(BASE_URL)

    df = pd.read_excel(EXCEL)

    products = []

    for _, row in df.iterrows():
        detail_page_url = row["url"]
        # get detail page
        browser.execute_script(
            f"""window.open("{detail_page_url}", "_self")"""
        )

        product = {}
        try:
            # get information
            # get title
            product["title"] = browser.find_element_by_css_selector(
                ".product_title").get_attribute('innerHTML').replace("\n", "")

            # raw data, include price and unit
            raw_data = browser.find_element_by_xpath(
                """/html/body/div[1]/main/div/div[2]/div/div[2]/div[1]/div/div[2]/p[1]"""
            ).get_attribute("innerHTML")

            # get price
            product["price"] = str(
                re.search(
                    r"[\d\.]+", remove_html_tags(raw_data)
                )[0].replace(".", "")
            )

            # get unit
            product["unit"] = str(raw_data[raw_data.rindex("/")+1:])

            # get image url
            product["img_url"] = str(browser.find_element_by_css_selector(
                ".container + .product > div > div.col.large-9 > div.product-main > div > div.large-6.col > div.row.row-small > div > div > figure > div > div > div > a > img"
            ).get_attribute("src"))

            # get description (keep html because suitable for CKEDITOR)
            try:
                product["description"] = str(
                    remove_html_tags(
                        browser.find_element_by_css_selector(
                            "#tab-description"
                        ).get_attribute("innerHTML")
                    )
                )
            except Exception as e:
                product["description"] = ""

            products.append(product)
        except Exception as e:
            print(f"[ERROR] {detail_page_url} {e}")

    pd.DataFrame(products).to_excel("products.xlsx")

    browser.close()


if __name__ == "__main__":
    EXCEL = "result.xlsx"
    if not os.path.exists(EXCEL):
        print(f"[INFO]: not exist raw file")
        build_xlsx()
    if not os.path.exists("products.xlsx"):
        print(f"[INFO]: not exist products.xlsx")
        build_products_data()
    if not os.path.exists("db.sql"):
        df = pd.read_excel("products.xlsx")
        print(df)
