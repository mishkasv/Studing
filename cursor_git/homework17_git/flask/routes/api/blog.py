import json

from app import app, api, db, mail
from flask import render_template, request, Response, session
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User, Category, article_categories
from flask_mail import Message
import datetime
from flask_sqlalchemy import SessionBase
from helpers.additional_functions import check_password


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }


class User_store(Resource):
    def post(self):
        data = request.json
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),
            bio=data.get('bio'),
            country=data.get('country'),
            city=data.get('city'),
            created=datetime.datetime.now(),
            admin=0,
        )

        db.session.add(user)
        db.session.commit()
        session['user'] = user.serialize
        return Response(status=200)


class Articles(Resource):
    def post(self):
        data = request.json
        article = Article(
            title=data.get('title'),
            slug=data.get('slug'),
            author_id=data.get('author_id'),
            description=data.get('description'),
            short_description=data.get('short_description'),
            img=data.get('img')
        )
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def get(self):
        articles = Article.query
        if request.args.get('title'):
            articles = articles.filter_by(title=request.args.get('title'))

        # articles = articles.filter(Article.title.startswith('A'))

        if request.args.get("sort_by"):
            articles = articles.order_by(request.args.get("sort_by"))

        articles = articles.all()
        serialized_articles = []
        for article in articles:
            serialized_articles.append(article.serialize)

        return serialized_articles


class ArticlesEntity(Resource):
    def get(self, id):
        article = Article.query.get(id)
        if article == None:
            return Response(status=404)
        return article.serialize

    def delete(self, id):
        article = Article.query.get(id)

        if article == None:
            return Response(status=404)

        db.session.delete(article)
        db.session.commit()

        return Response(status=204)


class Users(Resource):
    def get(self):
        users = User.query.all()
        serialized_users = []
        for user in users:
            serialized_users.append(user.serialize)
        return serialized_users


class Contact(Resource):
    def post(self):
        data = request.json
        msg = Message('Contact form alert!', sender='alish.floud@gmail.com', recipients=['misha.savcuk@gmail.com'])
        msg.html = "Contact Email: " + data['email'] + "<br>" + "Contact Title: " + data[
            'title'] + "<br>" + "Contact Description: " + data['description']
        mail.send(msg)
        client_msg = Message('Dear Client!', sender='turupuru8@gmail.com', recipients=[data['email']])
        client_msg.html = render_template('blog/emails/contact.html', email=data['email'])
        mail.send(client_msg)
        return Response(status=200)


class ContactData(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.FOOTER_ITEMS_CONTACT
        }


class Article_category(Resource):
    def get(self):
        articles = Article.query
        serialized_articles = []
        for article in articles:
            categories = article.categories
            article_serialize = article.serialize
            if categories != []:
                categories_article = []
                for category in categories:
                    categories_article.append(category.title)
                article_serialize['categories'] = categories_article
            serialized_articles.append(article_serialize)
        return serialized_articles


class Login_user(Resource):
    def post(self):
        data = request.json
        user = User.query.filter_by(email=data['username']).first()
        if not user:
            user = User.query.filter_by(username=data['username']).first()
        if check_password(user.password, data['password']):
            session['user'] = user.serialize
            return Response(status=200)
        return Response(status=400)


api.add_resource(User_store, '/api/user-register')
api.add_resource(MenuItem, '/api/menu-items')
api.add_resource(Articles, '/api/articles')
api.add_resource(Users, '/api/users')
api.add_resource(Login_user, '/api/login')
api.add_resource(ArticlesEntity, '/api/article/<int:id>')
api.add_resource(Contact, '/api/contact')
api.add_resource(ContactData, '/api/contacts')
api.add_resource(Article_category, '/api/artcat')

