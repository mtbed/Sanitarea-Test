# from flask import Blueprint, render_template





# views = Blueprint(__name__, "views")



# @views.route("/")
# def home():
#     email = dict(session).get('email', None)
#     return f'Hello, {email}!'
   #return render_template("index.html", name = "Joe")


# @views.route("/profile/<username>")
# def profile(username):
#     return render_template("index.html", name = username)

# @views.route('/login')
# def login():
#     google = oauth.create_client('google')
#     redirect_uri = url_for('authorize', _external=True)
#     return google.authorize_redirect(redirect_uri)

# @views.route('/authorize')
# def authorize():
#     google = oauth.create_client('google')
#     token = google.authorize_access_token()
#     resp = google.get('userinfo')
#     resp.raise_for_status()
#     user_info = resp.json()
#     # do something with the token and profile
#     session['email'] = user_info['email']
#     return redirect('/')