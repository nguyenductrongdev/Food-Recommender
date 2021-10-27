from selenium import webdriver
from time import sleep
import re
from unidecode import unidecode
import json
import os
import requests
import werkzeug
import pandas as pd


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser = webdriver.Chrome(options=options)

BASE_URL = "https://thucphamnhanh.com/"
CRAWL_RESULT_FOLDER = "crawl_result"

if not os.path.exists(CRAWL_RESULT_FOLDER):
    os.mkdir(CRAWL_RESULT_FOLDER)

browser.get(BASE_URL)
sleep(3)

large_url = []
schema_url = {}

dropdown_title_tags = browser.find_elements_by_css_selector(".sf-with-ul")
for dropdown_title_tag in dropdown_title_tags:
    link_text = dropdown_title_tag.get_attribute('innerHTML')
    link_url = dropdown_title_tag.get_attribute('href')

    schema_url[link_text] = []
    large_url += [link_url]

    print(link_text, "-"*200)

    child_title_tags = browser.find_elements_by_css_selector(
        f"a.sf-with-ul[href='{link_url}'] + ul > li a")

    for child_title_tag in child_title_tags:
        link_text_child = child_title_tag.get_attribute('innerHTML')
        link_url_child = child_title_tag.get_attribute('href')

        print(link_text_child, "-"*50)

        schema_url[link_text] += [link_url_child]

print(schema_url)
print("-"*500, "setup schema complete", "-"*500)

# for url_name, url_childrens in schema_url.items():
#     if not os.path.exists(f"{CRAWL_RESULT_FOLDER}/{url_name}"):
#         os.mkdir(f"{CRAWL_RESULT_FOLDER}/{url_name}")
#     browser.execute_script(f"window.open('{url_name}', '_self')")
#     df = pd.DataFrame()


# simple
for url in large_url:
    browser.execute_script(f"window.open('{url}', '_self')")

browser.close()
