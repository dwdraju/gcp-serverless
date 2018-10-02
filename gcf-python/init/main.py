import flask
import requests

def getTodo(request):
    todo = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
    return flask.jsonify(todo)
