WTF_CSRF_ENABLED = True
SECRET_KEY = 'ssas232%445232332@121'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:12345@localhost/db_user'
SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# https://code.google.com/apis/console
GOOGLE_CLIENT_ID = '136891786115-l33cs8j73f6mh48scj265puil1utk4v4.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'FRUJnsi438Ua0oJJReO4BH6R'
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'

SECRET_KEY = 'asas#@32adsaPafcs#1dsds'

OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '915248948619380',
        'secret': '3e949096668b37b032ddb473c65c884c'
    }
}