import gspread
from config import Configuration

gc = gspread.login(Configuration.GDOCS_USER,Configuration.GDOCS_PASS)

def _save_gdocs(obj):
    wks = gc.open("bikeshare").sheet1
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
    

