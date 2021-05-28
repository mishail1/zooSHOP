from flask import Flask, render_template

import db.db_session

import models.form

import db.users

my_first_app = Flask(__name__)
my_first_app.config.from_object("config")

import db.db_session

db.db_session.global_init("my_db.db")

@my_first_app.route('/', methods=['GET', 'POST'])
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
            return home()
        else:
            return render_template('auth.html', message="Пользователь с таким email уже существует", form=form)
    return render_template("auth.html", form=form)

@my_first_app.route('/home')
def home():
    return render_template("home.html")


if __name__ == "__main__":
    my_first_app.run(debug=True)
