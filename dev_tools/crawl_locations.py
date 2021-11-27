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

browser = webdriver.Chrome(ChromeDriverManager().install())


def main():
    browser.get("https://www.google.com/maps/@9.779349,105.6189045,11z?hl=vi-VN")
    new_df = pd.DataFrame()

    with open(os.path.join("./fiho_locations.csv"), "r") as fp:
        rows = fp.readlines()[1:]

        for row in rows:
            row = row[:-1]
            vi_do, kinh_do = row.split(",")
            print(row.split(","))
            try:
                browser.execute_script(
                    f"document.querySelector('#searchboxinput').value = '{kinh_do},{vi_do}'"
                )

                # click to seach
                browser.find_element_by_css_selector(
                    "#searchbox-searchbutton").click()

                sleep(10)
                try:
                    address = browser.find_element_by_xpath(
                        "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div/div[1]/span[3]/span[3]"
                    ).get_attribute("innerHTML")
                except Exception as e:
                    # address = browser.find_element_by_xpath(
                    #     "/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[7]/div[1]/button/div[1]/div[2]/div[1]"
                    # ).get_attribute("innerHTML")
                    pass

                new_df = new_df.append({
                    "kinh_do": kinh_do,
                    "vi_do": vi_do,
                    "address": address,
                }, ignore_index=True)

                print(address, "-"*500)
            except Exception as e:
                browser.close()
                exit(e, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        new_df.to_excel("locations-plus.xlsx", index=None)
        browser.close()


if __name__ == "__main__":
    main()
