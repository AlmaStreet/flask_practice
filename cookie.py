from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie is set")
    resp.set_cookie('your_cookie', 'cookie_value')
    return resp

@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('your_cookie')
    return 'The value of your_cookie is: ' + cookie_value

if __name__ == '__main__':
    app.run(debug=True)
