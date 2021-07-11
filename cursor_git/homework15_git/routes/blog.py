from app import app, api
from flask import render_template, request
from config import Config, articles
from flask_restful import Resource, Api


@app.route('/', methods=["GET"])
def homepage():
    return render_template('blog/index.html', config=Config, articles=articles())


class MenuItem(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.MENU_ITEMS
        }

class ContactData(Resource):
    def get(self):
        return {
            'success': True,
            'items': Config.FOOTER_ITEMS_CONTACT
        }


api.add_resource(MenuItem, '/menu-items')
api.add_resource(ContactData, '/contacts')

