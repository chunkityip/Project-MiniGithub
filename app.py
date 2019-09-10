from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='templates')


info = [{'title': 'Mini-GitHit',
         'post': '2019/9/10'}]


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=info)


@app.route('/index', methods=['GET', 'POST'])
def lionel():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register")
def register():
    return render_template('register.html')


@app.route("/login")
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
