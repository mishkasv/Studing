from tests.conftest import client
from config import Config
from pytest_mock import mocker



querystring = {"q": 'London', "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
               "units": "metric"}

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200


def test_search_weather(client):
    Config.WEATHER_API_KEY = "95d643c076msh3e0d8681b534b6ep1f2705jsn31417c1ba41b"
    Config.WEATHER_API_URL = "https://community-open-weather-map.p.rapidapi.com/find"
    Config.WEATHER_API_HOST = "community-open-weather-map.p.rapidapi.com"
    response = client.post("/search", data={"mycity": "kharkiv","lon": "","lat": ""})
    assert response.status_code == 200
    print(response.data)
    assert b"Kharkiv" in response.data

    response = client.post("/search", data={"mycity": "","lon": 37,"lat": 20,"mycity1": "london","lon1": "","lat1": ""})
    assert response.status_code == 200
    print(response.data)
    assert b"Port" in response.data
    assert b"London" in response.data

def test_search_weather_mock(client, mocker):
    mocker.patch("requests.request", side_effect=[ApiMock(0),ApiMock(1)])
    response = client.post("/search", data={"mycity": "london","lon": "","lat": "","mycity1": "kharkiv","lon1": "","lat1": ""})
    print(response.data)
    assert response.status_code == 200
    assert b"Weather for London" in response.data
    assert b"Kharkiv" in response.data

class ApiMock:
    def __init__(self, req,*args, **kwargs):
        self.req = req
        self.jsondata = [{"list":[{'name': 'London', 'coord': {'lat': 0, 'lon': 0}, 'main': {'temp': 25}}]},
                         {"list":[{'name': 'Kharkiv', 'coord': {'lat': 0, 'lon': 0}, 'main': {'temp': 25}}]}]
        self.status_code = 200

    def json(self):
        return self.jsondata[self.req]