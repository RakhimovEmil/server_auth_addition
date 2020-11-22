from flask import Flask, request
import base64
import re

app = Flask(__name__)
d = {}
d['user'] = 'password'
d['lol'] = 'kek'
d['emil'] = 'how to use python?'
d['jack'] = 'sparrow'

@app.route("/<smth>")
def lol(smth):
    cur = request.headers['Authorization']
    cur = cur[6:]
    ans = base64.b64decode(cur).decode('utf-8')
    result = re.search(r'(\w+):(\w+)', ans)
    if d.get(result.group(1)) == result.group(2):
        return "", 200
    else:
        return "access is denied", 404


if __name__ == '__main__':
    app.run(port=5000)