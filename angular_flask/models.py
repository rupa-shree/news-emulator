from datetime import datetime

from angular_flask.core import db
from angular_flask import app


# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(80))
#     body = db.Column(db.Text)
#     pub_date = db.Column(db.DateTime)

#     def __init__(self, title, body, pub_date=None):
#         self.title = title
#         self.body = body
#         if pub_date is None:
#             pub_date = datetime.utcnow()
#         self.pub_date = pub_date

#     def __repr__(self):
#         return "<Post '{}' : '{}' : '{}'>".format(self.title, self.body, self.pub_date)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    avatar = db.Column(db.String(100))
    user_age = db.Column(db.Integer)
    user_type = db.Column(db.Integer)
    created_date = db.Column(db.DateTime)
    preferred_category = db.Column(db.String(20))
    last_visit = db.Column(db.DateTime)
    status = db.Column(db.Boolean)
    verification_code=db.Column(db.String(100))

    def __init__(self, name, email, password, avatar , user_age , user_type , created_date , preferred_category , last_visit , status,verification_code):
        self.name = name
        self.email = email
        self.passowrd = password
        self.avatar = avatar
        self.user_age = user_age
        self.user_type = user_type
        if created_date is None:
            created_date = datetime.utcnow()
        self.created_date = created_date
        self.preferred_category = preferred_category
        self.status= status
        self.verification_code=verification_code

    def __repr__(self):
        return "<User '{}' : '{}' : '{}' : '{}' : '{}' : '{}' : '{}'>".format(self.name, self.email, self.password, self.avatar , self.user_age ,self.created_date , self.user_type)

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.String())
    author = db.Column(db.String(50))
    tag = db.Column(db.String(50))
    pub_date = db.Column(db.DateTime)
    banner_img_url = db.Column(db.String())
    video_url = db.Column(db.String())
    user_type = db.Column(db.String(20))
    status = db.Column(db.String(20))
    verification_code = db.Column(db.String(20))

    def __init__(self, title, body, author, tag , pub_date , banner_img_url , video_url , user_type , status , verification_code):
        self.title = title
        self.body = body
        self.author = author
        self.tag = tag
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.banner_img_url = banner_img_url
        self.video_url = video_url
        self.user_type = user_type
        self.status = status
        self.verification_code = verification_code

    def __repr__(self):
        return "<Content '{}' : '{}' : '{}' : '{}' : '{}' : '{}'>".format(self.title, self.body, self.author, self.tag , self.pub_date , self.banner_img_url)

class User_history(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20))
    viewed_category = db.Column(db.String(20))

    def __init__(self, user_id , viewed_category):
        self.user_id = user_id
        self.viewed_category = viewed_category

    def __repr__(self):
        return "<User_history '{}' : '{}'>".format(self.user_id, self.viewed_category)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(20))

    def __init__(self, category_name):
        self.category_name = category_name

    def __repr__(self):
        return "<Category '{}' >".format(self.category_name)

class Sub_category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_category_name = db.Column(db.String(20))
    category_id = db.Column(db.String(20))

    def __init__(self, sub_category_name , category_id):
        self.sub_category_name = sub_category_name
        self.category_id = category_id

    def __repr__(self):
        return "<Sub_category '{}' : '{}'>".format(self.sub_category_name , self.category_id)

class Suggestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20))
    feedback = db.Column(db.String())

    def __init__(self, user_id , feedback):
        self.user_id = user_id
        self.feedback = feedback

    def __repr__(self):
        return "<Suggestion '{}' : '{}'>".format(self.user_id, self.feedback)

class User_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_type = db.Column(db.String(20))

    def __init__(self, user_type):
        self.user_type = user_type

    def __repr__(self):
        return "<User_type '{}' >".format(self.user_type)

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100))
    name = db.Column(db.String(100))
    access_type = db.Column(db.String(10))


    def __init__(self, url , name , access_type):
        self.url = url
        self.name = name
        self.access_type = access_type

    def __repr__(self):
        return "<Settings '{}' : '{}' : '{}'>".format(self.url, self.name , self.access_type)

# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20))
#     tag = db.Column(db.String(50))
#     pub_date = db.column(Datetime)

#     def __init__(self, title, body, author, tag , pub_date):
#         self.title = title
#         self.body = body
#         self.author = author
#         self.tag = tag
#         if pub_date is None:
#             pub_date = datetime.utcnow()
#         self.pub_date = pub_date

#     def __repr__(self):
#         return "<Content '{}' : '{}' : '{}' : '{}' : '{}'>".format(self.title, self.body, self.author, self.tag , self.pub_date)

# models for which we want to create API endpoints
# app.config['API_MODELS'] = {'post': Post}

# models for which we want to create CRUD-style URL endpoints,
# and pass the routing onto our AngularJS application
# app.config['CRUD_URL_MODELS'] = {'post': Post}
