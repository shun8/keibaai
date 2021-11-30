import cx_Oracle
import os
import yaml

base = os.path.dirname(os.path.abspath(__file__))
db_conf_file = os.path.normpath(os.path.join(base, "../conf/db_connection.yaml"))
with open(db_conf_file, "r", encoding="utf-8") as l_file:
    db_conf_all = yaml.safe_load(l_file)

ora_conf = db_conf_all["oracle"]
conn=cx_Oracle.connect(user=ora_conf["username"],password=ora_conf["password"],dsn=ora_conf["dsn"])

from pathlib import Path

pathlist = Path(os.path.join(base, "../ddl_oracle")).glob('**/*.ddl')
for path in pathlist:
    with open(path) as f:
        sql = f.read()
        cur = conn.cursor()
        l_sql = sql.replace('\n','').rstrip(';')
        # ; 入ってるとエラー
        # 複数SQL文の書いてあるファイルに未対応。やるなら;で文字列分割してループ
        cur.execute(l_sql)
        cur.close()
conn.close()
