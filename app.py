from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

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

@app.route('/old-home-page')
def redirect_to_home():
    """ re-direct to new home page """
    return redirect('/')

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
    num = randint(1,10)
    return render_template('lucky.html',lucky_num = num)

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

COMPLIMENTS = ['cool', 'clever', 'tenacious']

@app.route('/greet')
def greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment = nice_thing)

@app.route('/greet_2')
def greeting_two():
    username = request.args['username']
    wantscompliments = request.args.get('wantscompliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username = username,wantscompliments = wantscompliments, compliments=nice_things )

@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spellword.html', word = word)

MOVIES = ['Amadeus', 'Chicken Run', 'Dances with Wolves']

@app.route('/movies')
def show_all_movies():
    """ show list of all movies in fake DB """
    return render_template('movies.html', movies= MOVIES)