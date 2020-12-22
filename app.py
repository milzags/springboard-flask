from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
debug = DebugToolbarExtension(app)

@app.route('/my/route', methods =["POST"])
def handle_post_to_my_route():
    ...
    pass

@app.route('/add-comment')
def add_comment_form():
    return """
        <h1>Add Comment</h1>
        <form method="POST">
            <input type="text" placeholder="comment" name="comment"/>
            <input type="text" placeholder="username" name="username"/>
            <button>Submit</button>
        </form>
        """

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form['comment']
    username = request.form['username']
    return f"""
    <h1>Saved your comment</h1>
    <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
    </ul>
    """

@app.route('/hello')
def index():
    """ return homepage """
    return render_template('index.html')

@app.route('/lucky')
def show_lucky_num():
    """ example of simple dynamic template """
    num = randint(1,20)
    return render_template('lucky.html',lucky_num = num)

@app.route('/form')
def show_form():
    return render_template('form.html')

COMPLIMENTS = ['cool', 'clever', 'tenacious']

@app.route('/greet')
def greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment = nice_thing)