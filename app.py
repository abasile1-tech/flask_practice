from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1>Hello World!</h1>"

@app.route('/<name>')
def greet(name):
	return f"Hello {name}"

@app.route('/iwant/<food>')
def get_food(food):
	return f"I want {food}"