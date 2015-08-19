from os import rename
import shutil
from bikessites import app as application, auth
from bikessites.models import Comment

def flushDB():
    bikeStations = application.config['BIKESTATIONS']

    # let's get rid of the old data.db file
    dbfile = application.config['DBFILE']
    delme='%s_' %(dbfile)
    try:
        shutil.move(dbfile,delme)
    except:
        # no data.db file here!
        pass

    # set up the admin user
    auth.User.create_table(fail_silently=True)
    admin = auth.User(username='admin', email='', admin=True, active=True)
    admin.set_password('admin')
    admin.save()

    # add the default bikestations
    Comment.create_table(fail_silently=True)
    for bs in bikeStations:
        # {'lat':'34.0334882847','lon':'-118.480816291','comment':'Santa Monica','approved':True},
        Comment.create(
            lat=bs['lat'],
            lon=bs['lon'],
            comment=bs['comment'],
            reply=bs['reply'],
            approved=bs['approved'],
            name=bs['name'],
            email=bs['email'],
            zipcode=bs['zipcode'],
            likes=bs['likes'],
            category=bs['category'],
            )


if __name__ == "__main__":
    if application.config['DEBUG']:
        flushDB()

    application.run()
