import gspread
from flask.ext.rq import job
from config import Configuration


@job
def _save_gdocs(obj):
    gc = gspread.login(Configuration.GDOCS_USER,Configuration.GDOCS_PASS)
    wks = gc.open("bikeshare").sheet1
    print "{{{{{{{{{{{ _save_gdocs }}}}}}}}}}}"
    print obj
    objl = [obj.lat,
        obj.lon,
        obj.comment,
        obj.reply,
        obj.likes,
        obj.name,
        obj.email,
        obj.zipcode,
        obj.category,
        obj.pub_date,
        ]
    wks.append_row(objl)
    

import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())