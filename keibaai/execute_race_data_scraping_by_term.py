import argparse
import datetime
from dateutil.relativedelta import relativedelta
import time

from model.settings import Session
from model.race import ErrorRace

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
            race_data, race_lap_times, race_umas = scraper.request_race_data(race_id)
            time.sleep(sleep_sec)

            try:
                session = Session()
                del_races_sql = "DELETE FROM races WHERE id = " + race_id
                session.execute(del_races_sql)
                del_race_uma_sql = "DELETE FROM race_uma WHERE race_id = " + race_id
                session.execute(del_race_uma_sql)
                del_race_lap_times_sql = "DELETE FROM race_lap_times WHERE race_id = " + race_id
                session.execute(del_race_lap_times_sql)
                session.add(race_data)
                if race_lap_times:
                    session.add_all(race_lap_times)
                session.add_all(race_umas)
                session.commit()
            except Exception as e:
                session.rollback()
                del_error_races_sql = "DELETE FROM error_races WHERE id = " + race_id
                session.execute(del_error_races_sql)
                error_race = ErrorRace()
                error_race.id = race_id
                session.add(error_race)
                session.commit()
            finally:
                session.close()


    ym = ym + relativedelta(months=1)
