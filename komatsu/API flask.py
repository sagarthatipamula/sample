from flask import Flask, request

# app = Flask(__name__)
#
#
# @app.route('/')
# def fun1():
#     return "sample app"
# app.run()
# #
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
app = Flask(__name__)
@app.route('/sub')
def sss():
    a = [1, 2, 3]
    b = [4, 5, 6]
    return tuple(a + b)
app.run()
#
# @app.route('/www')
# def eee():
#     return "sssss"
#
#
# app.run()

# app = Flask(__name__)
#
#
# @app.route('/sample')
#
#
#
#
# def fun3():
#     p = request.args.get('p')
#     q = request.args.get('q')
#     if p > q:
#         return str([1, 2, 3])
#     else:
#         return str([4, 5, 6])
#
#
# app.run()
#
# web = Flask(__name__)
#
#
# @web.route('/')
# def tsr():
#     return "flask frame web developing"
#
#
# @web.route('/forloop')
# def ysr():
#     a = [1, 2, 3, 5, 6]
#     for item in a:
#         return (str(item))
#
#
# web.run()

#
# app = Flask(__name__)
#
#
# @app.route('/')
# def yyy():
#     return "ufkdluyfgilydfiuflutfliyf"
#
#
# @app.route('/Tsunami')
# def fun():
#     a = request.args.get('a')
#     b = request.args.get('b')
#     return str(int(a) + int(b))
#
#
# app.run()
#


# app = Flask(__name__)
#
#
# @app.route('/webin')
# def ttt():
#     list = [item for item in range(20) if item % 2 == 0]
#     return str(list)
#
#
# app.run()


# app = Flask(__name__)
#
# @app.route('/website')
# def www():
#     return str("sagar")
#
# app.run()
