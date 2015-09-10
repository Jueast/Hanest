import os
import webapp2
import jinja2
import Handler

from google.appengine.ext import db


class Post(db.Model):

    username = db.StringProperty(required=True)
    content = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    up = db.IntegerProperty(required=True)
    down = db.IntegerProperty(required=True)

    def getScore(self):
        # calculate the post score from ups, downs and created time
        # TODO
        return 0


class FrontHandler(Handler.Handler):

    def get(self):
        self.render("front.html")


app = webapp2.WSGIApplication([('/', FrontHandler)
                               ],
                              debug=True)

