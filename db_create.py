from project import db
from project.models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("Good", "I\'m good."))
db.session.add(BlogPost("Well", "I\'m well."))
db.session.add(BlogPost("Flask", "Learning Flask"))
db.session.add(BlogPost("postgres", "We setup a local postgres instance!"))

# commit the changes
db.session.commit()