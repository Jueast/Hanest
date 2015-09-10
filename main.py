import os
import webapp2
import jinja2
import time

from lib.utils import *
from Handler import *
# import all handlers

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

    def render(self):
        self._render_text = self.content.replace('\n', '<br>')
        return render_str("post.html", p=self)


class FrontHandler(Handler):

    def get(self):
        posts = db.GqlQuery("select * from Post \
            order by created limit 10")
        self.render("front.html", posts=posts)

    def post(self):
        username = self.request.get('username')
        content = self.request.get('content')

        if username and content:
            if validName(username):
                p = Post(username=username, content=content, up=0, down=0)
                p.put()
                self.redirect("/thanks")
            else:
                error = "Your fake name is not nice!"
                self.render("front.html", username=username, content=content,
                            error=error)
        else:
            error = "Your fake name and content, please!"
            self.render("front.html", username=username, content=content,
                        error=error)


# all in Handler
app = webapp2.WSGIApplication([('/', FrontHandler),
                               ('/introduction', IntroHandler),
                               ('/([0-9]+)', PostHandler),
                               ('/thanks', ThanksHandler)
                               ],
                              debug=True)
