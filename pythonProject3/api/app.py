from flask import Flask, request

#
# app = Flask(__name__)
#
#
# @app.route('/')
# def fun1():
#     return "sample app"
#
#
# @app.route('/get-student-mobile-num')
# def fun2():
#     return "89787675435"
#
#
# myJson = '[1,2,3,4,5,6]'
#
#
# @app.route('/sample-json')
# def fun3():
#     return myJson
#
#
# @app.route('/add')
# def fun4():
#     a = request.args.get('a')
#     b = request.args.get('b')
#     return str(int(a) + int(b))
#
#
# @app.route('/multiplication')
# def fun5():
#     a = request.args.get('a')
#     b = request.args.get('b')
#     return str(int(a) * int(b))
#
#
# @app.route('/division')
# def func6():
#     a = request.args.get('a')
#     b = request.args.get('b')
#     return str(int(a) / int(b))
#
#
# app.run()


# app = Flask(__name__)
#
#
# @app.route('/')
# def fun1():
#     return "app sample"
#
#
# @app.route('/multiplication')
# def fun2():
#     p = request.args.get('p')
#     q = request.args.get('q')
#     return str(int(p) * int(q))
#
#
# app.run()
#


app = Flask(__name__)


@app.route('/')
def fun1():
    return "website"


@app.route('/substraction')
def fun2():
    p = request.args.get('p')
    q = request.args.get('q')
    return str(int(p)-int(q))


app.run()
