from bikessites import app, auth
from bikessites.models import Comment

if __name__ == "__main__":
    auth.User.create_table(fail_silently=True)
    Comment.create_table(fail_silently=True)

    app.run()

