from flask import render_template, flash, redirect, g, url_for
from app import app, db, logMgr
from .forms import LoginForm
from flask_login import LoginManager, UserMixin, login_user, logout_user,current_user, login_required
from app.oauth import OAuthSignIn
from app.models import User

@logMgr.user_loader
def load_user(id):
    return User.query.get(int(id))

@login_required
@app.route('/blogs')
def blogs():
    user = {'username': 'Parvez'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'username': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'username': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("blogs.html",
                           title='Blogs Home',
                           user=user,
 
                           posts=posts)
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', 
                           title='Sign In')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('blogs'))
    oauth = OAuthSignIn.get_provider(provider)
    return oauth.authorize()


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('blogs'))
    oauth = OAuthSignIn.get_provider(provider)
    social_id, username, email = oauth.callback()
    if social_id is None:
        flash('Authentication failed.')
        return redirect(url_for('home'))
    user = User.query.filter_by(social_id=social_id).first()
    if not user:
        user = User(social_id=social_id, username=username, email=email)
        db.session.add(user)
        db.session.commit()
    login_user(user, True)
    return redirect(url_for('blogs'))