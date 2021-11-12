#!/usr/bin/env python3
import os
import logging.config
import requests
from bs4 import BeautifulSoup
import re
import sys

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
    def __init__(self, db_client, sql_dir):
        base_url = "https://db.netkeiba.com/"
        # ?year=2021&month=1
        race_calendar_url = "https://race.netkeiba.com/top/calendar.html"

    @logging
    def request_races_urls(self, year, month):
        payload = {"year": year, "month": month}
        r = requests.get(self.race_calendar_url, params=payload)

        r.text

        return r.text


    def 