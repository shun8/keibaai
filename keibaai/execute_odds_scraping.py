import argparse
import time

import model.odds as odds
from model.settings import Session
import netkeiba_scraper

# args
parser = argparse.ArgumentParser(description="odds scraping by race_id")
parser.add_argument("race_id")
args = parser.parse_args( )
race_id = args.race_id

scraper = netkeiba_scraper.NetkeibaScraper()

sleep_sec = 1

# win_odds = scraper.request_win_odds(race_id)
# time.sleep(sleep_sec)
# place_odds = scraper.request_place_odds(race_id)
# time.sleep(sleep_sec)
# quinella_place_odds = scraper.request_quinella_place_odds(race_id)
# time.sleep(sleep_sec)
# bracket_quinella_odds = scraper.request_bracket_quinella_odds(race_id)
# time.sleep(sleep_sec)
# exacta_odds = scraper.request_exacta_odds(race_id)
# time.sleep(sleep_sec)
# quinella_odds = scraper.request_quinella_odds(race_id)
# time.sleep(sleep_sec)
# trifecta_odds = scraper.request_trifecta_odds(race_id)
# time.sleep(sleep_sec)
trio_odds = scraper.request_trio_odds(race_id)

session = Session()
# del_sql = "DELETE FROM win_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(win_odds)
# session.commit()

# del_sql = "DELETE FROM place_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(place_odds)
# session.commit()

# del_sql = "DELETE FROM quinella_place_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(quinella_place_odds)
# session.commit()

# del_sql = "DELETE FROM bracket_quinella_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(bracket_quinella_odds)
# session.commit()

# del_sql = "DELETE FROM exacta_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(exacta_odds)
# session.commit()

# del_sql = "DELETE FROM quinella_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(quinella_odds)
# session.commit()

# del_sql = "DELETE FROM trifecta_odds WHERE race_id = " + race_id
# session.execute(del_sql)
# session.add_all(trifecta_odds)
# session.commit()

del_sql = "DELETE FROM trio_odds WHERE race_id = " + race_id
session.execute(del_sql)
session.add_all(trio_odds)
session.commit()

session.close()
