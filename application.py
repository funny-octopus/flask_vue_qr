from app import create_app, db
from app.models import *

print('1111111111111111111')
app = create_app()

@app.shell_context_processor
def make_shell_contex():
    return {'db':db,
            'User':User,
            'Prod':Product,
            'Cat':Category,
            'Coun':Country,
            'Cur':Currency,
            'Prv':Price_v,
            'Rub':Ruble_course,
             }

