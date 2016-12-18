from flask import Flask, url_for, request, render_template, Markup

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# print(url_for('static', filename='style.css'))

print(Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>')
print(Markup(u'<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>'))
print(Markup.escape('<blink>hacker</blink>'))
print(Markup(u'&lt;blink&gt;hacker&lt;/blink&gt;'))
print(Markup('<em>Marked up</em> &raquo; HTML').striptags())


if __name__ == "__main__":
    app.run()