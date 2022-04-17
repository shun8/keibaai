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

win_odds = scraper.request_win_odds(race_id)
time.sleep(5)
place_odds = scraper.request_place_odds(race_id)
time.sleep(5)

session = Session()
del_sql = "DELETE FROM win_odds WHERE race_id = " + race_id
session.execute(del_sql)
session.add_all(win_odds)
session.commit()

del_sql = "DELETE FROM place_odds WHERE race_id = " + race_id
session.execute(del_sql)
session.add_all(place_odds)
session.commit()

session.close()
