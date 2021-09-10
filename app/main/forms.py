from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
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

    # class Meta:
    #     csrf = False

    name = StringField('Название', validators=[DataRequired()])
    category = SelectField('Категория')
    image_url = FileField('Изображение')
    # factory = SelectField('Фабрика', render_kw={'@change':'get_collections()', 'id':'factory'})
    factory = StringField('Фабрика')
    country = SelectField('Страна')
    # collection = SelectField('Коллекция', render_kw={'v-model':'collections',})
    collection = StringField('Коллекция')
    price = StringField('Цена', validators=[DataRequired()])
    price_v = SelectField('Ед.изм.')
    currency = SelectField('Валюта')
    percent = StringField('Наценка(%)', validators=[DataRequired()])
    count = StringField('Кол-во в упаковке', validators=[DataRequired()])
    submit = SubmitField('Сохранить')

