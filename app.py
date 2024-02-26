from flask import Flask
from views import views
from authlib.integrations.flask_client import OAuth

oauth = OAuth(app)

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/login')
def login():
    redirect_uri = url_for('authorize', _external=True)
    return oauth.twitter.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    token = oauth.twitter.authorize_access_token()
    resp = oauth.twitter.get('account/verify_credentials.json')
    resp.raise_for_status()
    profile = resp.json()
    # do something with the token and profile
    return redirect('/')