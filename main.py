from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
import email_validator
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from flask_bootstrap import Bootstrap

email = "admin@email.com"
password = "12345678"

app = Flask(__name__)
Bootstrap(app)

app.secret_key = "scooter159"
validator = DataRequired()


class LoginForm(FlaskForm):
    email = StringField(label=('Email'),
                        validators=[DataRequired(),
                                    Email(check_deliverability=True),
                                    Length(max=120)])

    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                         Length(min=8, message='Password should be at least %(min)d characters long')])

    submit = SubmitField(label="Log in")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == email and login_form.password.data == password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    else:
        return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
