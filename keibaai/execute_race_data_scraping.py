import argparse
import time

from model.settings import Session
import netkeiba_scraper

# args
parser = argparse.ArgumentParser(description="race_data scraping by race_id")
parser.add_argument("race_id")
args = parser.parse_args( )
race_id = args.race_id

scraper = netkeiba_scraper.NetkeibaScraper()

sleep_sec = 1

race_data, race_lap_times, race_umas = scraper.request_race_data(race_id)

session = Session()
del_races_sql = "DELETE FROM races WHERE id = " + race_id
session.execute(del_races_sql)
del_race_uma_sql = "DELETE FROM race_uma WHERE race_id = " + race_id
session.execute(del_race_uma_sql)
del_race_lap_times_sql = "DELETE FROM race_lap_times WHERE race_id = " + race_id
session.execute(del_race_lap_times_sql)
print(race_data)
print(race_lap_times)
print(race_umas)
session.add(race_data)
session.add_all(race_lap_times)
session.add_all(race_umas)
session.commit()
session.close()
