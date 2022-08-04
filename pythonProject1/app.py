#
#
#
#
# app = flask(__name__)
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
# app.run()


mydict = {22:22, "strin":444,22:44}
print(type(mydict))

myset = {1, "aaa", (1,3)}
print(type(myset))