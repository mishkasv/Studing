import unittest
import requests
import os


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = requests

    def test_form(self):
        data = {
            "title": "Dog",
            "slug": 'dog',
            'description': "dddddddddddooooooooooooooooooooooggggggggggggggggggggggggyyyyyyyyyyyyyyyyeeeeeeeeeeeeeeeellllllllss",
            "short_description": "dddddoooooooogggggggggyyyyyyy"
        }
        response = self.client.post(url='http://localhost:5000/article/store', data=data,
                                    files={"img": open(os.path.abspath(
                                        r'C:\Users\Gazik\PycharmProjects\Cursor education\flask2\Python-Martian-Manhunter-adv-\lectures\flask\static\uploads\Screenshot from 2021-03-26 16-44-13.png'),
                                                       'rb')})
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get(url='http://localhost:5000/article/dogaaa').status_code, 200)
        self.assertIn("ddoooooooooooooooooooooo", self.client.get(url='http://localhost:5000/article/dogaaa').text,
                      "NOT")

    def test_delapi(self):
        id = 1  # id of article in database that you want to delete
        resp = self.client.delete(f'http://localhost:5000/api/articles/{id}')
        self.assertEqual(resp.status_code, 204)


if __name__ == '__main__':
    unittest.main()
