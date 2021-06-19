# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
import requests
from config import Config
from flask_restful import Resource, Api
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    list_of_lists = []
    for i in range(int(len(request.form)/3)):
        if i==0:
            city = request.form.get("mycity")
            lat = request.form["lat"]
            lon = request.form["lon"]
        else:
            city = request.form.get(f"mycity{i}")
            lat = request.form[f"lat{i}"]
            lon = request.form[f"lon{i}"]

        querystring = {"q": city, "cnt": "1", "mode": "null", "lon": lon, "type": "link, accurate", "lat": lat,
                   "units": "metric"}

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST
        }

        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
        print(response.status_code)
        if response.status_code == 200:
            data = response.json()
            weather = data['list'][0]
            print(data)
        else:
            return Response(status=404)
        list_of_lists.append(weather)

    print(list_of_lists)
    return render_template("weather.html", weathers=list_of_lists)

api = Api(app)


class Todo(Resource):

    def get(self, todo_id):
        try:
            with open("todos.txt", "r") as f:
                todos = json.load(f)
                data = {todo_id: todos[todo_id]}
                f.close()

        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        try:
            with open("todos.txt", "r") as f:
                todos = json.load(f)
                f.close()
        except FileNotFoundError:
            todos = dict()
        with open("todos.txt", "w") as f:
            todos[todo_id] = request.json.get('text')
            json.dump(todos, f, ensure_ascii=False)
            f.close()
        return {todo_id: todos[todo_id]}

    def delete(self, todo_id):
        try:
            with open("todos.txt", "r") as f:
                todos = json.load(f)
                del todos[str(todo_id)]
                f.close()
        except FileNotFoundError:
            todos = dict()
        with open("todos.txt", "w") as f:
            json.dump(todos, f, ensure_ascii=False)
            f.close()
        return Response(todos, status=204)


class TodoList(Resource):

    def get(self):
        try:
            with open("todos.txt", "r") as f:
                todos = json.load(f)
                f.close()
        except FileNotFoundError:
            todos = dict()
        return todos

    def post(self):
        try:
            with open("todos.txt", "r") as f:
                todos = json.load(f)
                f.close()
        except FileNotFoundError:
            todos = dict()
        with open("todos.txt", "w") as f:
            todos[request.json.get('todo_id', None)] = request.json.get('text', "")
            json.dump(todos,f,ensure_ascii=False)
            f.close()

        return todos


class Weather(Resource):

    def get(self):
        city = request.args["city"].split(",")
        data_json=dict()
        print(city)
        for cit in city:
            print(cit)
            querystring_2 = {"q": cit, "cnt": "1", "mode": "null", "lon": "", "type": "link, accurate", "lat": "",
                   "units": "metric"}

            headers = {
                'x-rapidapi-key': Config.WEATHER_API_KEY,
                'x-rapidapi-host': Config.WEATHER_API_HOST
            }

            response = requests.request("GET", Config.WEATHER_API_URL, headers = headers, params = querystring_2)
            print(response.status_code)

            if response.status_code ==200:
                data_json[cit]=response.json()


            else:Response("Not found", status=404)
        return data_json



api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')
api.add_resource(Weather, "/weather")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)