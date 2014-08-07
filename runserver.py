from os import rename
from bikessites import app, auth
from bikessites.models import Comment

def flushDB():
    bikeStations = app.config['BIKESTATIONS']

    # let's get rid of the old data.db file
    dbfile = app.config['DBFILE']
    delme='/tmp/%s' %(dbfile)
    try:
        rename(dbfile,delme)
    except:
        # no data.db file here!
        pass
    
    # set up the admin user
    auth.User.create_table(fail_silently=True)  # make sure table created.
    admin = auth.User(username='admin', email='', admin=True, active=True)
    admin.set_password('admin')
    admin.save()

    # add the default bikestations
    Comment.create_table(fail_silently=True)
    for bs in bikeStations:
        # {'lat': '34.12927', 'comment': 'Pilot', 'lon': '-118.14949'}
        Comment.create(lat=bs['lat'],lon=bs['lon'],comment=bs['comment'],)


if __name__ == "__main__":
    if app.config['DEBUG']:
        flushDB()

    app.run()

