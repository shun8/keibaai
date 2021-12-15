#!/usr/bin/env python3
import os
import logging.config
import requests
from bs4 import BeautifulSoup
import re
import sys
import datetime
import pytz
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib

import model.odds as odds

base = os.path.dirname(os.path.abspath(__file__))
LOGGING_CONF_FILE = os.path.normpath(os.path.join(base, "../conf/logging.ini"))

# loggerを初期化
if os.path.exists(LOGGING_CONF_FILE):
    # logging.iniファイルがある場合設定を読み込む
    logging.config.fileConfig(LOGGING_CONF_FILE)
    logger = logging.getLogger("nkscraper")
else:
    # logging.iniファイルがない場合すべてコンソールに出力
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

# logging
def logging(func):
    def wrapper(*args, **kwargs):
        try:
            logger.info("Start: " + func.__name__)
            logger.info("Args: " + str(args) + str(kwargs))
            retval = func(*args, **kwargs)
            logger.info("End: " + func.__name__)
            return retval
        except:
            exc_info = sys.exc_info()
            logger.error("Error: %s,%s" % (exc_info[0], exc_info[1]))
            raise
    return wrapper

class NetkeibaScraper:
    def __init__(self):
        self.base_url = "https://db.netkeiba.com/"
        # ?year=2021&month=1
        self.race_calendar_url = "https://race.netkeiba.com/top/calendar.html"
        # ?race_id=202110010611&type=b1
        self.race_odds_url = "https://race.netkeiba.com/odds/index.html"

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    @logging
    def request_races_urls(self, year, month):
        payload = {"year": year, "month": month}
        r = requests.get(self.race_calendar_url, params=payload)

        r.text

        return r.text

    @logging
    def request_win_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b1"}
        r = requests.get(self.race_odds_url, params=payload)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u in range(1, 30):
            odds_tag = soup.select_one(f"#odds-1_{u:02}")
            if odds_tag is None:
                break
            m = odds.WinOdds()
            m.race_id = race_id
            m.horse_number = u
            o = odds_tag.contents[0]
            m.odds = o if self._is_float(o) else '0'
            m.last_updated = last_updated
            odds_list.append(m)

        return odds_list

    @logging
    def request_place_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b2"}
        r = requests.get(self.race_odds_url, params=payload)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u in range(1, 30):
            odds_tag = soup.select_one(f"#odds-2_{u:02}")
            if odds_tag is None:
                break
            m = odds.PlaceOdds()
            m.race_id = race_id
            m.horse_number = u
            o_list = odds_tag.contents[0].split("-", 1)
            if len(o_list) != 2:
                continue
            m.odds_min = o_list[0].strip() if self._is_float(o_list[0]) else '0'
            m.odds_max = o_list[1].strip() if self._is_float(o_list[1]) else '0'
            m.last_updated = last_updated
            odds_list.append(m)

        return odds_list

    @logging
    def request_quinella_place_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b5"}
        r = requests.get(self.race_odds_url, params=payload)
        r.encoding = r.apparent_encoding
        soup = BeautifulSoup(r.text, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u in range(1, 30):
            odds_tag = soup.select_one(f"#odds-5-{u:02}")
            if odds_tag is None:
                break
            m = odds.WinOdds()
            m.race_id = race_id
            m.horse_number = u
            o = odds_tag.contents[0]
            m.odds = o if self._is_float(o) else '0'
            m.last_updated = last_updated
            odds_list.append(m)

        return odds_list

    @staticmethod
    def _is_float(s):
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True

    @staticmethod
    def _get_last_updated(soup):
        last_updated = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        last_updated.replace(
                second=0, 
                microsecond=0)
        official_time_tag = soup.select_one('#offical_time')
        if official_time_tag is not None:
            time_str = re.search(r"\d+:\d+", official_time_tag.contents[0]).match
            l = time_str.split(":")
            last_updated.replace(
                    hour=int(l[0]),
                    minute=int(l[1]))

    @staticmethod
    def _get_race_data(soup):


