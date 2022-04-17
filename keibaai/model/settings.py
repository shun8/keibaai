from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import yaml

import cx_Oracle
from pathlib import Path
base = Path().resolve()
db_conf_file = os.path.normpath(os.path.join(base, "./conf/db_connection.yaml"))
with open(db_conf_file, "r", encoding="utf-8") as l_file:
    db_conf_all = yaml.safe_load(l_file)

ora_conf = db_conf_all["oracle"]
conn=cx_Oracle.connect(user=ora_conf["username"],password=ora_conf["password"],dsn=ora_conf["dsn"])

engine = create_engine(f"oracle://{ora_conf['username']}:{ora_conf['password']}@{ora_conf['dsn']}/?encoding=UTF-8&nencoding=UTF-8")
Session = sessionmaker(bind=engine)
