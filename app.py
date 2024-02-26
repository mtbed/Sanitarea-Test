from flask import Flask, url_for, redirect, session
from views import views
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = 'secret'

# oauth config
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='567957499957-6606sfh4orcme321shuidk5kvi6mp3as.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)


app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def home():
    email = dict(session).get('email', None)
    return f'Hello, {email}!'


@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    # do something with the token and profile
    return redirect('/')