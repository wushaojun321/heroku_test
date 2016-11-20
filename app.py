#encoding:utf8

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>你好！</h1>'

if __name__ == '__main__':
	app.run()