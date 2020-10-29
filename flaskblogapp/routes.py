from flask import render_template,url_for,flash,redirect
from flaskblogapp import app
from flaskblogapp.forms import RegistrationForm,LoginForm
from flaskblogapp.models import User,Post

posts=[
    {
        'author':'Avishek',
        'title':'First Post',
        'content':'First Content',
        'date_posted':'October 28,2020'
    },
    {
        'author':'Bubai',
        'title':'Second Post',
        'content':'Second Content',
        'date_posted':'October 29,2020'
    }
]

@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html',posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title="About")

@app.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('index'))
    return render_template('register.html',title="Register",form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='test@test.com' and form.password.data=='1995':
            flash('You have been logged in successfully','success')
            return redirect(url_for('index'))
        else:
            flash('Login unsucessful,Please check your credentials','danger')
    return render_template('login.html',title="Login",form=form)