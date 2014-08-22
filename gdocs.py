import gspread
from config import Configuration


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
    

"""
The /etc/supervisor/rqworker.ini file will look like this:

[program:rqworker]
; Point the command to the specific rqworker command you want to run.
; If you use virtualenv, be sure to point it to
; /var/www/envs/bikessites/bin/rqworker
; Also, you probably want to include a settings module to configure this
; worker.  For more info on that, see http://python-rq.org/docs/workers/
command=/var/www/envs/bikessites/bin/rqworker
process_name=%(program_name)s

; If you want to run more than one worker instance, increase this
numprocs=1

; This is the directory from which RQ is ran. Be sure to point this to the
; directory where your source code is importable from
directory=/var/www/envs/bikessites/

; RQ requires the TERM signal to perform a warm shutdown. If RQ does not die
; within 10 seconds, supervisor will forcefully kill it
stopsignal=TERM

; These are up to you
autostart=true
autorestart=true

"""