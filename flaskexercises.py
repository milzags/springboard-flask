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