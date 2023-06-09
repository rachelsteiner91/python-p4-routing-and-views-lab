#!/usr/bin/env python3
## FYI Anything included in the route passed to the app.route decorator with angle brackets <> surrounding it will be passed to the decorated function as a parameter
from flask import Flask

app = Flask(__name__)

#Your index() view should be routed to at the base URL with /. 
# It should Contain an h1 element that contains the title of this application, "Python Operations with Flask Routing and Views".
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


###A print_string view should take one parameter, a STRING. It should print the string in the console and display it in the web browser. Its URL should be of the format /print/parameter.
@app.route('/print/<string:route>')
def print_string(route):
    print(route)
    return route

##A count() view should take one parameter, an INTEGER. 
# ##It should display all numbers in the range of that parameter on separate lines. Its URL should be of the format /count/parameter.
@app.route('/count/<int:number>')
def count(number):
    count = f''
    for n in range(number):
        count += f'{n}\n'
    return count

###math() view should take three parameters: num1, operation, and num2
##Its URL should be of the format /math/<num1>/<operation>/<num2>
##included operations should be: +, -, *, div and %
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return str(num1 + num2)
    
    elif operation == '-':
        return str(num1 - num2)

    elif operation == '*':
        return str(num1 * num2)

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'



if __name__ == '__main__':
    app.run(port=5555, debug=True)
