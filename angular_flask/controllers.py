import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort, jsonify

from angular_flask import app

# routing for API endpoints, generated from the models designated as API_MODELS
from angular_flask.core import api_manager
from angular_flask.models import  User, Content , User_history , Category , Sub_category , Suggestion , User_type , Settings
from angular_flask.core import db

# for model_name in app.config['API_MODELS']:
#     model_class = app.config['API_MODELS'][model_name]
#     api_manager.create_api(model_class, methods=['GET', 'POST'])

session = api_manager.session


# routing for basic pages (pass routing onto the Angular app)
@app.route('/')
@app.route('/post')
def basic_pages(**kwargs):
    return make_response(open('angular_flask/templates/index.html').read())

@app.route('/user',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()
        return render_template('login.html', error=error)

# @app.route('/getUser')
# def getUser():        
#     user = User.query.all()
#     for x in xrange(0, len(user)):
#         list = [
#                 {
#                 'id' : user.id,
#                 'name' : user.name,
#                 'email' : user.email,
#                 'avatar' : user.avatar
#                 }
#             ]
#     return jsonify(results=list)


@app.route('/getuser',methods=['GET','POST'])
def getUser():
    if request.method == 'POST':
        email = request.args['email']
        try:
            data = User.query.filter_by(email = email).first_or_404()
            # session.expire_all()
            print(data)
            list = [
                {
                'id' : data.id,
                'name' : data.name,
                'email' : data.email,
                'passowrd' : data.passowrd,
                'avatar' : data.avatar,
                'user_age' : data.user_age,
                'user_type' : data.user_type,
                'created_time' : data.created_time,
                'preferred_category' : data.preferred_category,
                'last_visit' : data.last_visit,
                'status' : data.status
                }
            ]
        except Exception as e:
            print e
    else:
        print("Resquest method is not GET")
    return jsonify(results=list)

@app.route('/adduser',methods=['GET','POST'])
def addUser():
    if request.method == 'POST':
        name = request.args['name']
        email = request.args['email']
        passowrd = request.args['password']
        avatar = request.args['avatar']
        user_age = request.args['user_age']
        user_type = request.args['user_type']
        preferred_category = request.args['preferred_category']
        status=request.args['status']
        verification_code=request.args['verification_code']

        try:
            data = User(name=name, email = email ,passowrd=passowrd , avatar= avatar,user_age=user_age,user_type=user_type,preferred_category= preferred_category,status=status,verification_code=verification_code)
            db.session.add(data)
            db.session.commit()
            # session.expire_all()
            print(data)
        except Exception as e:
            print e
    else:
        print("Resquest method is not GET")
    return jsonify(results=list)

@app.route('/updateuser',methods=['GET','POST'])
def updateUser():
    if request.method == 'POST':
        id = request.args['id']
        name = request.args['name']
        email = request.args['email']
        avatar = request.args['avatar']
        user_age = request.args['user_age']
        user_type = request.args['user_type']
        preferred_category = request.args['preferred_category']
        status=request.args['status']
        verification_code=request.args['verification_code']
        try:
            db.session.query(User).filter(User.id == id).update({User.name: name,User.avatar:avatar,User.user_age:user_age ,User.user_type:user_type , User.preferred_category:preferred_category,user.status:status,user.verification_code:verification_code})
            db.session.commit()
            # session.expire_all()
            print "success"
            data = "Success"
        except Exception as e:
            print e
            data = e
    else:
        print("Request method is not GET")
    return data

@app.route('/getcontent',methods=['GET','POST'])
def getContent():
    if request.method == 'POST':
        content_id = request.args['content_id']
        try:
            data = Content.query.filter_by(id = content_id).first_or_404()
            # session.expire_all()
            print(data)
            list = [
                {
                'id' : content.id,
                'title' : content.title,
                'body' : content.body,
                'author' : content.author,
                'tag' : content.tag,
                'pub_date' : content.pub_date,
                'video_url' : content.video_url,
                'user_type' : content.user_type
                }
            ]
        except Exception as e:
            print e
    else:
        print("Resquest method is not GET")
    return jsonify(results=list)
    
@app.route('/addcontent',methods=['GET','POST'])
def addContent():
    if request.method == 'POST':
        title = request.args['title']
        body = request.args['body']
        author = request.args['author']
        tag = request.args['tag']

        try:
            data = Content(title=title, body=body, author=author, tag=tag)
            db.session.add(data)
            db.session.commit()
            # session.expire_all()
            data = "True"
        except Exception as e:
            data = e
    else:
        data = "Error"
    return data

@app.route('/updatecontent',methods=['GET','POST'])
def updateContent():
    if request.method == 'POST':
        content_id = request.args['content_id']
        title = request.args['title']
        body = request.args['body']
        author = request.args['author']
        tag = request.args['tag']
        try:
            # data = Content.query.filter_by(content_id = content_id).first_or_404()
            Content.query.filter(Content.id == content_id).update({Content.title : title, Content.body : body, Content.author : author, content.tag : tag})
            db.session.commit()
            # session.expire_all()
            data = "True"
        except Exception as e:
            data = e
    else:
        data = "Error"
    return data

# @app.route('/addContent')
#     def addcontent():

# @app.route('/updateContent')
#     def addcontent():


# routing for CRUD-style endpoints
# passes routing onto the angular frontend if the requested resource exists

@app.route('/<model_name>/')
@app.route('/<model_name>/<item_id>')
def rest_pages(model_name, item_id=None):
    if model_name in crud_url_models:
        model_class = crud_url_models[model_name]
        if item_id is None or session.query(exists().where(
                model_class.id == item_id)).scalar():
            return make_response(open(
                'angular_flask/templates/index.html').read())
    abort(404)


# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'img/favicon.ico')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
