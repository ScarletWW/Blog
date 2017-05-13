from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    user = {'nickname': 'Mike'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)

@app.route('/author')
def author():
    return "Harry Wang"
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()#对LoginForm类初始化
    if form.validate_on_submit():
        flash('Login requested for OpenID"' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign in',
        form = form)