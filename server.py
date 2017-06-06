from flask import Flask, jsonify, render_template, request,make_response
from functools import wraps
from mongodao import taskmodel

app = Flask(__name__)


def allow_cross_domain(fun):
    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst
    return wrapper_fun



@app.route('/')
@allow_cross_domain
def hello_world():
    return jsonify({'m':'Hello World!'})


@app.route('/addtask',method='POST')
@allow_cross_domain
def add_task():
    request.form['username']
    taskmodel.insert_one(request.form)

if __name__ == '__main__':
    app.run(debug=True)