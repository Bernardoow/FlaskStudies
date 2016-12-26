from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def index():
    return redirect("http://www.uol.com.br")

@app.route('/user/<id>')
def get_user(id):
    user = None
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user)

if __name__ == '__main__':
    app.run(debug=True)