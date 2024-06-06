
from flask import render_template, Flask, request, redirect, url_for, session

app = Flask(__name__)

user_database = {
    "vova": "1234567",
    "ivan": "000000",
    "vasyl": "222222",
    "roman": "654321",

}
app.secret_key = 'ldss'

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return render_template('show_posts.html', post_id=post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in user_database and user_database[username] == password:
            session['username'] = username

            return redirect(url_for('user', username=username))

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/users')
def show_users_profile():
    users = [
        'kyznetsov',
        'arsen',
        'Sovyak'
    ]
    return render_template('user_list.html', users=users)

@app.route("/users/<string:username>")
def user(username):
    if 'username' in session and session['username'] == username:
        return render_template('user.html', username=username)

    return redirect(url_for('login'))



@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True, port=8080)