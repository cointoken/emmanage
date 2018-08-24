from app import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import Members
from .models import Transfer
from .mydb import MyDb
from . import myconfig
from werkzeug.security import check_password_hash
from sqlalchemy import update
from datetime import datetime
from sqlalchemy import create_engine



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/transfer')
@login_required
def transfer():
    engine = create_engine(myconfig.SQLALCHEMY_DATABASE_URI)
    db = MyDb(engine)
 
    page = int(request.args.get('p', '1'))
    if not page:
        page = 1
    limit = int(request.args.get('limit', '10'))
    if not limit:
        limit = 10
    
    trans = db.transfer_query_from_page(0,limit,page)
    print(trans.count)
    pager = {'total': 30, 'limit':limit, 'curr_page': page}
    return render_template('transfer.html', trans=trans,p=pager)


@app.route('/transfer_record')
@login_required
def transfer_record():
    """Render a secure page on our website that only logged in users can access."""
    return render_template('transfer_record.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('transfer'))

   
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
    
        email = form.email.data
        password = form.password.data

        user = Members.query.filter_by(email=email).first()

        if user is not None and check_password_hash(user.password, password):
            remember_me = False

            if 'remember_me' in request.form:
                remember_me = True
            login_user(user, remember=remember_me)

            flash('Logged in successfully.', 'success')

            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Username or Password is incorrect.', 'danger')

    flash_errors(form)
    return render_template('login.html', form=form)
    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(id):
    return Members.query.get(int(id))


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')



@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
   
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
