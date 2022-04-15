from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class ChangeImageForm(FlaskForm):
    filename = FileField('Изменить изображение', validators=[FileRequired()], render_kw={'aria-describedby':'FileAddon', 'aria-label':'Upload'})
    submit = SubmitField('Изменить')


class AddProductForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    category = SelectField('Категория')
    image_url = FileField('Изображение')
    factory = StringField('Фабрика', validators=[DataRequired()])
    provider = StringField('Поставщик', validators=[DataRequired()])
    country = SelectField('Страна')
    collection = StringField('Коллекция', validators=[DataRequired()])
    size = StringField('Размер', validators=[DataRequired()])
    price = StringField('Цена', validators=[DataRequired()])
    currency = SelectField('Валюта')
    price_v = SelectField('Ед.изм.')
    percent = StringField('Наценка(%)', validators=[DataRequired()])
    count = StringField('Кол-во в упаковке', validators=[DataRequired()])
    notes = StringField('Примечания', widget=TextArea())
    submit = SubmitField('Сохранить')

class ChangeCurrency(FlaskForm):
    dollar = StringField('Доллар', validators=[DataRequired()])
    euro = StringField('Евро', validators=[DataRequired()])
    submit = SubmitField('Сохранить')


class ChangePasswordForm(FlaskForm):
    password = StringField('New Password', validators=[DataRequired()])
    submit = SubmitField('Изменить')

