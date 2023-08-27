import argparse
import datetime
from dateutil.relativedelta import relativedelta
import time

import model.odds as odds
from model.settings import Session
import netkeiba_scraper

import netkeiba_scraper

tdatetime = datetime.datetime.now()
tstr = tdatetime.strftime("%Y%m")

# args
parser = argparse.ArgumentParser(description="race_data scraping by term")
parser.add_argument('--start', default=tstr)
parser.add_argument('--end', default=tstr)
args = parser.parse_args()
start_ym = datetime.datetime.strptime(args.start, "%Y%m")
end_ym = datetime.datetime.strptime(args.end, "%Y%m")

print(start_ym)
print(end_ym)

if start_ym > end_ym:
    print("ERROR: start > end")
    exit(1)

scraper = netkeiba_scraper.NetkeibaScraper()

sleep_sec = 1

ym = start_ym
while(end_ym >= ym):
    kaisai_dates = scraper.request_kaisai_dates(ym.year, ym.month)
    time.sleep(sleep_sec)
    for kaisai_date in kaisai_dates:
        race_ids = scraper.request_race_ids(kaisai_date)
        time.sleep(sleep_sec)
        for race_id in race_ids:
            win_odds = scraper.request_win_odds(race_id)
            time.sleep(sleep_sec)
            place_odds = scraper.request_place_odds(race_id)
            time.sleep(sleep_sec)
            quinella_place_odds = scraper.request_quinella_place_odds(race_id)
            time.sleep(sleep_sec)
            bracket_quinella_odds = scraper.request_bracket_quinella_odds(race_id)
            time.sleep(sleep_sec)
            exacta_odds = scraper.request_exacta_odds(race_id)
            time.sleep(sleep_sec)
            quinella_odds = scraper.request_quinella_odds(race_id)
            time.sleep(sleep_sec)
            trifecta_odds = scraper.request_trifecta_odds(race_id)
            time.sleep(sleep_sec)
            trio_odds = scraper.request_trio_odds(race_id)

            try:
                session = Session()
                del_sql = "DELETE FROM win_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(win_odds)

                del_sql = "DELETE FROM place_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(place_odds)

                del_sql = "DELETE FROM quinella_place_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(quinella_place_odds)

                del_sql = "DELETE FROM bracket_quinella_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(bracket_quinella_odds)

                del_sql = "DELETE FROM exacta_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(exacta_odds)

                del_sql = "DELETE FROM quinella_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(quinella_odds)

                del_sql = "DELETE FROM trifecta_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(trifecta_odds)

                del_sql = "DELETE FROM trio_odds WHERE race_id = " + race_id
                session.execute(del_sql)
                session.add_all(trio_odds)

                session.commit()
            except Exception as e:
                session.rollback()
            finally:
                session.close()

    ym = ym + relativedelta(months=1)
