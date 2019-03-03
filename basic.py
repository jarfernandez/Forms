from flask import Flask, render_template, redirect, session, flash, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'


class InfoForm(FlaskForm):

    breed = StringField("What breed are you?")
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash(f"You just changed your breed to: {session['breed']}")
        return redirect(url_for('index'))

    return render_template('index.html', form=form)


if __name__ == "__main___":
    app.run()
