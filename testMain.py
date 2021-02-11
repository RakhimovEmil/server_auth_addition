import unittest
from flask import Flask
import base64
import requests

app = Flask(__name__)


class Test(unittest.TestCase):
    def test(self):
        url = 'http://localhost:5000/file42'
        str = "user:password"
        str = str.encode("UTF-8")
        str = base64.b64encode(str)
        str = str.decode("UTF-8")
        cur = 'Basic ' + str
        headers = {'Authorization': cur}
        ans = requests.get(url, headers=headers)
        self.assertEqual(ans.status_code, 200)

        url = 'http://localhost:5000/file42'
        str = "lol:kek"
        str = str.encode("UTF-8")
        str = base64.b64encode(str)
        str = str.decode("UTF-8")
        cur = 'Basic ' + str
        headers = {'Authorization': cur}
        ans = requests.get(url, headers=headers)
        self.assertEqual(ans.status_code, 200)

        url = 'http://localhost:5000/file42'
        str = "kek:lel"
        str = str.encode("UTF-8")
        str = base64.b64encode(str)
        str = str.decode("UTF-8")
        cur = 'Basic ' + str
        headers = {'Authorization': cur}
        ans = requests.get(url, headers=headers)
        self.assertEqual(ans.status_code, 403)

        url = 'http://localhost:5000/file42'
        str = "jack:sparrow"
        str = str.encode("UTF-8")
        str = base64.b64encode(str)
        str = str.decode("UTF-8")
        cur = 'Basic ' + str
        headers = {'Authorization': cur}
        ans = requests.get(url, headers=headers)
        self.assertEqual(ans.status_code, 200)


if __name__ == '__main__':
    app.run()
    unittest.main()
