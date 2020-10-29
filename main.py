from datetime import datetime
import pytz
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm,LoginForm

app=Flask(__name__)
app.config['SECRET_KEY']='a1e824f498ef42682a1e81bce53cbd2db3'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

class User(db.Model):

    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),unique=True,nullable=False)
    email=db.Column(db.String(100),unique=True,nullable=False)
    image_file=db.Column(db.String(20),unique=True,nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User({'self.username'},{'self.email'},{'self.image_file'})"

class Post(db.Model):

    ist=pytz.timezone('Asia/Kolkata')
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    date_posted=db.Column(db.DateTime,nullable=False,default=datetime.now(ist))

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

if __name__=='__main__':
    app.run(debug=True)