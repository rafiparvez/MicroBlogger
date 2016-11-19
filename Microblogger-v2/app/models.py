from app import db
from app import logMgr
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class User(db.Model):
	__tablename__='users'
	id = db.Column('id',db.Integer, primary_key=True)
	social_id = db.Column('social_id',db.String(64), nullable=False, unique=True)
	username = db.Column('username',db.String(64), index=True, unique=True)
	email = db.Column('email',db.String(120), index=True, unique=True)
	posts = db.relationship('Post', backref='author', lazy='dynamic')

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def __repr__(self):
		return '<User %r>' % (self.username)

	def __init__(self,social_id,username,email):
		self.social_id=social_id
		self.username=username
		self.email=email

	def get_id(self):
		try:
			return str(self.id) # python 3
		except NameError:
			return unicode(self.id)  # python 2

class Post(db.Model):
	__tablename__='posts'
	id = db.Column(db.Integer, primary_key = True)
	body = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __repr__(self):
		return '<Post %r>' % (self.body)