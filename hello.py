from flask import Flask, render_template, url_for
from forms import Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'qwerty'
dict1 = {'prashant': 'prashants71195@gmail.com'}


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = Login()
    print(form.username)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
