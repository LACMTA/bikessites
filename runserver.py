from os import rename
import shutil
from bikessites import app, auth
from bikessites.models import Comment

def flushDB():
    bikeStations = app.config['BIKESTATIONS']

    # let's get rid of the old data.db file
    dbfile = app.config['DBFILE']
    delme='%s_' %(dbfile)
    try:
        shutil.move(dbfile,delme)
    except:
        # no data.db file here!
        pass
    
    # set up the admin user
    auth.User.create_table(fail_silently=True)
    auth.User.create(username='admin', email='', password='admin', admin=True, active=True)

    # add the default bikestations
    Comment.create_table(fail_silently=True)
    for bs in bikeStations:
        # {'lat':'34.0334882847','lon':'-118.480816291','comment':'Santa Monica','approved':True},
        Comment.create(lat=bs['lat'],lon=bs['lon'],comment=bs['comment'],approved=bs['approved'],)


if __name__ == "__main__":
    if app.config['DEBUG']:
        flushDB()

    app.run()

