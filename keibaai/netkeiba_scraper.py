#!/usr/bin/env python3
import os
import logging.config
import requests
from bs4 import BeautifulSoup
import re
import sys
import time
import datetime
import pytz
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib
from keibaai.model.race import Race

import model.odds as odds
import model.race as race

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
        # ?kaisai_date=20210131
        self.race_list_url="https://race.netkeiba.com/top/race_list.html"
        # ?race_id=202110010611&type=b1
        self.race_odds_url = "https://race.netkeiba.com/odds/index.html"
        # ?race_id=202110010611
        self.race_result_url = "https://race.netkeiba.com/race/result.html"

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(options=options, service=service)

    @logging
    def request_kaisai_dates(self, year, month):
        payload = {"year": year, "month": month}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_calendar_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        race_links = soup.find_all("a", attrs={"target": "_parent"})
        hrefs = [x.attrs["href"] for x in race_links if "kaisai_date" in x.attrs["href"]]
        kaisai_dates = []
        for href in hrefs:
            kaisai_dates.append(re.search(r"\d{8}", href).group())

        return kaisai_dates

    @logging
    def request_race_ids(self, kaisai_date):
        payload = {"kaisai_date": kaisai_date}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_list_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        all_links = soup.find_all("a")
        race_ids =  [re.search(r"\d+", x.attrs["href"]).group() for x in all_links if "result.html" in x.attrs.get("href", "no href")]
        return race_ids

    @logging
    def request_race_data(self, race_id):
        payload = {"race_id": race_id}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_result_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        race_data, race_lap_times, race_umas = NetkeibaScraper._get_race_data(race_id, soup)
        return race_data, race_lap_times, race_umas

    @logging
    def request_win_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b1"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

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
            m.odds = float(o) if self._is_float(o) else 0.0
            m.last_updated = last_updated
            odds_list.append(m)

        return odds_list

    @logging
    def request_place_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b2"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

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
            m.odds_min = float(o_list[0]) if self._is_float(o_list[0]) else 0.0
            m.odds_max = float(o_list[1]) if self._is_float(o_list[1]) else 0.0
            m.last_updated = last_updated
            odds_list.append(m)

        return odds_list

    @logging
    def request_quinella_place_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b5"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u1 in range(1, 30):
            for u2 in range(u1 + 1, 30):
                odds_tag = soup.select_one(f"#odds-5-{u1:02}{u2:02}")
                oddsmin_tag = soup.select_one(f"#oddsmin-5-{u1:02}{u2:02}")
                if odds_tag is None:
                    break
                m = odds.QuinellaPlaceOdds()
                m.race_id = race_id
                m.horse_number_1 = u1
                m.horse_number_2 = u2
                o_max = odds_tag.contents[0]
                m.odds_max = float(o_max) if self._is_float(o_max) else 0.0
                o_min = oddsmin_tag.contents[0]
                m.odds_min = float(o_min) if self._is_float(o_min) else 0.0
                m.last_updated = last_updated
                odds_list.append(m)

        return odds_list

    @logging
    def request_bracket_quinella_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b3"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for b1 in range(1, 10):
            for b2 in range(b1, 10):
                odds_tag = soup.select_one(f"#odds-3-{b1:02}{b2:02}")
                if odds_tag is None:
                    break
                m = odds.BracketQuinellaOdds()
                m.race_id = race_id
                m.bracket_number_1 = b1
                m.bracket_number_2 = b2
                o = odds_tag.contents[0]
                m.odds = float(o) if self._is_float(o) else 0.0
                m.last_updated = last_updated
                odds_list.append(m)

        return odds_list

    @logging
    def request_exacta_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b6"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u1 in range(1, 30):
            for u2 in range(1, 30):
                if u1 == u2:
                    continue
                odds_tag = soup.select_one(f"#odds-6-{u1:02}{u2:02}")
                if odds_tag is None:
                    break
                m = odds.ExactaOdds()
                m.race_id = race_id
                m.horse_number_1 = u1
                m.horse_number_2 = u2
                o = odds_tag.contents[0]
                m.odds = float(o) if self._is_float(o) else 0.0
                m.last_updated = last_updated
                odds_list.append(m)

        return odds_list

    @logging
    def request_quinella_odds(self, race_id):
        payload = {"race_id": race_id, "type": "b4"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u1 in range(1, 30):
            for u2 in range(u1 + 1, 30):
                odds_tag = soup.select_one(f"#odds-4-{u1:02}{u2:02}")
                if odds_tag is None:
                    break
                m = odds.QuinellaOdds()
                m.race_id = race_id
                m.horse_number_1 = u1
                m.horse_number_2 = u2
                o = odds_tag.contents[0]
                m.odds = float(o) if self._is_float(o) else 0.0
                m.last_updated = last_updated
                odds_list.append(m)

        return odds_list

    @logging
    def request_trifecta_odds(self, race_id, sleep_sec=1):
        payload = {"race_id": race_id, "type": "b8"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)

        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u1 in range(1, 30):
            select_element = self.driver.find_element(By.ID ,"list_select_horse")
            select_object = Select(select_element)
            try:
                select_object.select_by_value(str(u1))
            except selenium.common.exceptions.NoSuchElementException:
                break

            time.sleep(sleep_sec)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            for u2 in range(1, 30):
                if u1 == u2:
                    continue
                for u3 in range(1, 30):
                    if u1 == u3 or u2 == u3:
                        continue
                    odds_tag = soup.select_one(f"#odds-8-{u1:02}{u2:02}{u3:02}")
                    if odds_tag is None:
                        break
                    m = odds.TrifectaOdds()
                    m.race_id = race_id
                    m.horse_number_1 = u1
                    m.horse_number_2 = u2
                    m.horse_number_3 = u3
                    o = odds_tag.contents[0]
                    m.odds = float(o) if self._is_float(o) else 0.0
                    m.last_updated = last_updated
                    odds_list.append(m)

        return odds_list

    @logging
    def request_trio_odds(self, race_id, sleep_sec=1):
        payload = {"race_id": race_id, "type": "b7"}

        qs = urllib.parse.urlencode(payload)
        self.driver.get(self.race_odds_url + "?" + qs)

        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        last_updated = self._get_last_updated(soup)
        odds_list = []
        for u1 in range(1, 30):
            select_element = self.driver.find_element(By.ID, "list_select_horse")
            select_object = Select(select_element)
            try:
                select_object.select_by_value(str(u1))
            except selenium.common.exceptions.NoSuchElementException:
                break

            time.sleep(sleep_sec)
            html = self.driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            for u2 in range(u1 + 1, 30):
                for u3 in range(u2 + 1, 30):
                    odds_tag = soup.select_one(f"#odds-7-{u1:02}{u2:02}{u3:02}")
                    if odds_tag is None:
                        break
                    m = odds.TrioOdds()
                    m.race_id = race_id
                    m.horse_number_1 = u1
                    m.horse_number_2 = u2
                    m.horse_number_3 = u3
                    o = odds_tag.contents[0]
                    m.odds = float(o) if self._is_float(o) else 0.0
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
        last_updated = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))
        last_updated.replace(
                second=0, 
                microsecond=0)
        # official_time_tag = soup.select_one("#official_time")
        # if official_time_tag is not None:
        #     time_str = re.search(r"\d+:\d+", official_time_tag.contents[0]).group()
        #     l = time_str.split(":")
        #     last_updated.replace(
        #             hour=int(l[0]),
        #             minute=int(l[1]))
        return last_updated

    @staticmethod
    def _get_race_data(race_id, soup):
        race_data = race.Race()
        race_data.id = race_id
        race_data.name = soup.select_one(".RaceName").contents[0].strip()
        race_data.race_track_id = int(race_id[5:7])
        race_data.kai = int(race_id[7:9])
        race_data.nichi = int(race_id[9:11])
        race_data.race_no = int(race_id[11:13])

        mrbtn = soup.select_one(".MapRaceBtn")
        m = re.search(r"/([^ \t<>/]+)\.png", mrbtn.get("href"))
        race_data.course_id = m.group(1)

        race_data.grade_id, race_data.is_win5 = NetkeibaScraper._get_grade_id(soup)
        race_data.condition = NetkeibaScraper._get_race_condition(soup)
        race_data.handicap = NetkeibaScraper._get_handicap(soup)
        race_data.race_date = NetkeibaScraper._get_race_date(race_id, soup)
        race_data.race_start = NetkeibaScraper._get_race_start(soup)
        race_data.weather = NetkeibaScraper._get_weather(soup)
        race_data.going = NetkeibaScraper._get_going(soup)
        race_data.num_of_horses = NetkeibaScraper._get_num_of_horses(soup)

        corner_orders = NetkeibaScraper._get_corner_orders(soup)
        if len(corner_orders) > 0:
            race_data.corner_order_1 = corner_orders[0]
        if len(corner_orders) > 1:
            race_data.corner_order_2 = corner_orders[1]
        if len(corner_orders) > 2:
            race_data.corner_order_3 = corner_orders[2]
        if len(corner_orders) > 3:
            race_data.corner_order_4 = corner_orders[3]

        race_data.pace = NetkeibaScraper._get_pace(soup)

        race_lap_times = NetkeibaScraper._get_lap_times(race_id, soup)
        race_umas = NetkeibaScraper._get_race_umas(race_id, soup)

        return race_data, race_lap_times, race_umas

    @staticmethod
    def _get_race_date(race_id, soup):
        l = re.findall(r"\d+", soup.find("dd", class_="Active").text)
        return datetime.date(int(race_id[0:4]), int(l[0]), int(l[1]))

    @staticmethod
    def _get_grade_id(soup):
        grade_id = 99
        is_win5 = "0"
        gts = soup.select(".Icon_GradeType")
        for gt in gts:
            m = re.search(r"Icon_GradeType([0-9]+)", str(gt))
            if m:
                if m.group(1) == "13":
                    is_win5 = "1"
                else:
                    grade_id = int(m.group(1))
        rnm = soup.select_one(".RaceName").contents[0].strip()
        if grade_id == 99:
            grade_id = NetkeibaScraper._get_grade_id_by_name(rnm)
        return grade_id, is_win5

    @staticmethod
    def _get_grade_id_by_name(name):
        if "Jpn3" in name or "jpn3" in name or "JPN3" in name:
            return 21
        if "Jpn2" in name or "jpn2" in name or "JPN2" in name:
            return 20
        if "Jpn1" in name or "jpn1" in name or "JPN1" in name:
            return 19

        if "新馬" in name:
            return 31
        if "未勝利" in name:
            return 30
        if "1勝" in name or "１勝" in name:
            return 18
        if "500万" in name or "５００万" in name:
            return 9
        if "2勝" in name or "２勝" in name:
            return 17
        if "900万" in name or "９００万" in name:
            return 8
        if "1000万" in name or "１０００万" in name:
            return 7
        if "3勝" in name or "３勝" in name:
            return 16
        if "1600万" in name or "１６００万" in name:
            return 6
        if "OP" in name or "オープン" in name:
            return 5
        if "(L)" in name or "（L）" in name or "リステッド" in name:
            return 15
        if "重賞" in name:
            return 4
        if "JG3" in name or "ＪＧ３" in name:
            return 12
        if "G3" in name or "Ｇ３" in name:
            return 3
        if "JG2" in name or "ＪＧ２" in name:
            return 11
        if "G2" in name or "Ｇ２" in name:
            return 2
        if "JG1" in name or "ＪＧ１" in name:
            return 10
        if "G1" in name or "Ｇ１" in name:
            return 1
        return 99

    @staticmethod
    def _get_race_condition(soup):
        rd2 = soup.select_one(".RaceData02")
        for c in rd2.contents:
            m = re.search(r"[^ \t<>/]+歳[^ \t<>/]*", str(c))
            if m:
                return m.group()
        return None

    @staticmethod
    def _get_num_of_horses(soup):
        rd2 = soup.select_one(".RaceData02")
        for c in rd2.contents:
            m = re.search(r"(\d+)頭", str(c))
            if m:
                return m.group(1)
        return 99

    @staticmethod
    def _get_weather(soup):
        rd1 = soup.select_one(".RaceData01")
        for c in rd1.contents:
            m = re.search(r"天候:([^ \t/<]+)", str(c))
            if m:
                return m.group(1)
        return None

    @staticmethod
    def _get_race_start(soup):
        rd1 = soup.select_one(".RaceData01")
        for c in rd1.contents:
            m = re.search(r"\d+:\d+", str(c))
            if m:
                return m.group()
        return None

    @staticmethod
    def _get_going(soup):
        rd2 = soup.select_one(".RaceData01")
        for c in rd2.contents:
            m = re.search(r"馬場:([^ \t/<]+)", str(c))
            if m:
                return m.group(1)
        return None

    @staticmethod
    def _get_handicap(soup):
        rd2 = soup.select_one(".RaceData02")
        for c in rd2.contents:
            if "定量" in str(c):
                return "定量"
            if "馬齢" in str(c):
                return "馬齢"
            if "別定" in str(c):
                return "別定"
            if "ハンデ" in str(c):
                return "ハンデ"
        return None

    @staticmethod
    def _get_corner_orders(soup):
        if not soup.select_one(".Corner_Num"):
            return []
        l = []
        for td in soup.select_one(".Corner_Num").find_all("td"):
            l.append(td.text)
        return l

    @staticmethod
    def _get_pace(soup):
        if not soup.select_one(".RapPace_Title"):
            return None

        m = re.search(r"ペース:([^ \t/<]+)", soup.select_one(".RapPace_Title").text)
        if m:
            return m.group(1)
        return None

    @staticmethod
    def _get_lap_times(race_id, soup):
        if not soup.select_one(".Race_HaronTime"):
            return None

        l = []
        l_d = soup.select_one(".Race_HaronTime").select_one(".Header").find_all("th")
        l_t = soup.select_one(".Race_HaronTime").select(".HaronTime")[1].find_all("td")
        for (d, t) in zip(l_d, l_t):
            lap_time = race.RaceLapTimes()
            lap_time.race_id = race_id
            lap_time.lap_distance = re.sub(r"\D", "", d.text.strip())
            lap_time.lap_time = t.text.strip()
            l.append(lap_time)
        return l

    @staticmethod
    def _get_race_umas(race_id, soup):
        l = []
        for horse in soup.select(".HorseList"):
            uma = race.RaceUma()
            uma.race_id = race_id
            uma.uma_id = NetkeibaScraper._get_uma_id(horse)
            c = horse.find_all("td")
            result = c[0].text.strip()
            if "除" in result:
                uma.is_excluded = 1
            elif "中" in result:
                uma.is_demoted = 1
            else:
                uma.result = result
                uma.is_excluded = 0
                uma.is_demoted = 0
            uma.bracket_number = c[1].text.strip()
            uma.horse_number = c[2].text.strip()
            uma.gender = re.sub(r"[0-9]+", "", c[4].text.strip())
            uma.age = re.sub(r"\D", "", c[4].text.strip())
            w = c[5].text.strip()
            uma.weight_to_carry = w if w else None
            uma.jockey_id = NetkeibaScraper._get_jockey_id(horse)
            t = c[7].text.strip().split(":")
            if len(t) > 1:
                minute = t[0] if t[0] else "0"
                second = t[1] if t[1] else "0"
                uma.time = int(minute) * 60 + float(second)
            else:
                uma.time = None

            uma.margin = c[8].text.strip()
            uma.ninki = c[9].text.strip()
            uma.win_odds = c[10].text.strip()
            f = c[11].text.strip()
            uma.final_3_furlong = f if f else None
            uma.corner_order = c[12].text.strip()
            uma.trainer_id = NetkeibaScraper._get_trainer_id(horse)
            uma.horse_weight = re.sub(r"\(.*\)", "", c[14].text.strip())
            m = re.search(r"\(-?\+?[0-9]+\)", c[14].text.strip())
            if m:
                uma.gain_and_loss_weight = m.group().strip("(+)")

            l.append(uma)
        return l

    @staticmethod
    def _get_uma_id(horse_list_tag):
        m = re.search(r"[0-9]+", horse_list_tag.select_one(".Horse_Name a")["href"])
        if m:
            return m.group()
        return None

    @staticmethod
    def _get_jockey_id(horse_list_tag):
        if not horse_list_tag.select_one(".Jockey a"):
            return None

        m = re.search(r"[0-9]+", horse_list_tag.select_one(".Jockey a")["href"])
        if m:
            return m.group()
        return None

    @staticmethod
    def _get_trainer_id(horse_list_tag):
        if not horse_list_tag.select_one(".Trainer a"):
            return None

        m = re.search(r"[0-9]+", horse_list_tag.select_one(".Trainer a")["href"])
        if m:
            return m.group()
        return None

