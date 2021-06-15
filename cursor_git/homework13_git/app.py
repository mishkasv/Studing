# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
import requests
from config import Config

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
        if response.status_code == 200:
            data = response.json()
            weather = data['list'][0]
            print(data)
        else:
            return Response(status=404)
        list_of_lists.append(weather)

    print(list_of_lists)
    return render_template("weather.html", weathers=list_of_lists)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)