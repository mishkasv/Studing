from app import app, api, db
from flask import render_template, request, Response
from config import Config, articles
from flask_restful import Resource, Api
from models.models import Article, User


@app.route('/', methods=["GET"])
def homepage():
    articles = Article.query.all()
    return render_template('blog/index.html', config=Config, articles=articles)


@app.route('/article/<string:slug>')
def article_details(slug):
    article = Article.query.filter_by(slug=slug).first()
    user = User.query.filter_by(id=article.author_id).one().username
    print(user)
    return render_template('blog/details.html', article=article, username = user)


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }


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


class Users(Resource):
    def get(self):
        users = User.query
        if request.args.get("sort_by"):
            users = users.order_by(request.args.get("sort_by"))

        users = users.all()
        serialized_users = []
        for user in users:
            serialized_users.append(user.serialize)

        return serialized_users

    def post(self):
        data = request.json
        user = User(
            username=data.get('username'),
            email=data.get('email'),
            created=data.get('created'),
            bio=data.get('bio'),
            admin=data.get('admin')
        )
        db.session.add(user)
        db.session.commit()
        return user.serialize

    # def get(self):
    #   user = User.query.get(1)
    #  serialized_articles = []
    # for article in user.articles:
    #    print(article)
    #   serialized_articles.append(article.serialize)
    # return serialized_articles


class UpdateUser(Resource):
    def delete(self, username):
        user = User.query.filter_by(username=username).one()
        db.session.delete(user)
        db.session.commit()
        return Response(status=204)

    def put(self, username):
        data = request.json
        user = User.query.filter_by(username=username).one()
        try:
            if data.get("username"):
                user.username = data.get("username")
        except KeyError:
            pass
        try:
            if data.get("email"):
                user.email = data.get("email")
        except KeyError:
            pass
        try:
            if data.get("bio"):
                user.bio = data.get("bio")
        except KeyError:
            pass
        try:
            if data.get("admin") or data.get("admin") == 0:
                user.admin = data.get("admin")
        except KeyError:
            pass
        db.session.commit()
        return user.serialize


api.add_resource(MenuItem, '/menu-items')
api.add_resource(Articles, '/articles')
api.add_resource(Users, '/users')
api.add_resource(UpdateUser, '/users/<string:username>')
api.add_resource(ArticlesEntity, '/articles/<int:id>')
