from flask import Flask, render_template, redirect, request

from flask_login import LoginManager, login_required, login_user, logout_user, current_user

import db.db_session

import models.form

import db.users

import db.ALLtovars

import db.tovars

import os


my_first_app = Flask(__name__)
my_first_app.config.from_object("config")

login_manager = LoginManager()
login_manager.init_app(my_first_app)
login_manager.login_view = 'login'

import db.db_session

db.db_session.global_init("my_db.db")

@my_first_app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    form = models.form.RegistrationForm()
    db_session = db.db_session.create_session()
    if form.validate_on_submit():
        if db_session.query(db.users.User).filter_by(email=form.email.data).count() < 1:
            user = db.users.User(
                email=form.email.data,
                password=form.password.data
            )

            db_session.add(user)
            db_session.commit()
            return login()
        else:
            return render_template('auth.html', message="Пользователь с таким email уже существует", form=form)
    return render_template("auth.html", form=form)

@my_first_app.route('/login', methods=['GET', 'POST'])
def login():
    form = models.form.LoginForm()
    if form.validate_on_submit():
        db_session = db.db_session.create_session()
        user = db_session.query(db.users.User).filter(db.users.User.email == form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return home()
        else:
            return render_template('signin.html', message="Неправильный логин или пароль", form=form)
    return render_template("signin.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db.db_session.create_session()
    return db_sess.query(db.users.User).get(user_id)


@my_first_app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@my_first_app.route('/')
def home():
    db_ses = db.db_session.create_session()
    tovars = db_ses.query(db.ALLtovars.ALLtovars)

    return render_template("home.html", alltovars=tovars)

@my_first_app.route('/buy')
def trash():
    db_ses = db.db_session.create_session()
    tovar_in_trash_user = db_ses.query(db.tovars.Tovars)
    aLLtovars = db_ses.query(db.ALLtovars.ALLtovars)
    return render_template("buy.html", tovar_in_trash_user=tovar_in_trash_user, aLLtovars=aLLtovars)


@my_first_app.route("/buy-tovar", methods=['GET', 'POST'])
def buy_tovar():
    tovar_id = request.args.get('values')
    print(tovar_id)
    db_ses = db.db_session.create_session()
    tovars = db.tovars.Tovars(
        user_id=current_user.id,
        tovar_id=tovar_id
    )

    db_ses.add(tovars)
    db_ses.commit()

    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    my_first_app.run(debug=True, host='0.0.0.0', port=port)




