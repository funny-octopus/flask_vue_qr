from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class ChangeImageForm(FlaskForm):
    filename = FileField('Изменить изображение', validators=[FileRequired()], render_kw={'aria-describedby':'FileAddon', 'aria-label':'Upload'})
    submit = SubmitField('Изменить')

