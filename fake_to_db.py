from sqlalchemy import create_engine

engine = create_engine('sqlite:///app.db')
conn = engine.connect()

# e = conn.execute("insert into user values (1, 'admin', 'pbkdf2:sha256:260000$pxghoNJ8gBuLY7B3$714c91e95b5dc1c738d62ae5b9fc9e274e7f43caa3a7b2bbdad38ff684475a97')")
# e = conn.execute("insert into country values (1, 'Россия')")
# e = conn.execute("insert into country values (2, 'Америка')")
# e = conn.execute("insert into country values (3, 'Германия')")
# e = conn.execute("insert into category values (1, 'Плитка')")
# e = conn.execute("insert into category values (2, 'Обои')")
# e = conn.execute("insert into category values (3, 'Посуда')")
# e = conn.execute("insert into category values (4, 'Свет')")
# e = conn.execute("insert into category values (5, 'Напольные покрытия')")
# e = conn.execute("insert into category values (6, 'Мебель')")
# e = conn.execute("insert into category values (7, 'Текстиль')")
# e = conn.execute("insert into currency values (1, 'Рубль')")
# e = conn.execute("insert into currency values (2, 'Евро')")
# e = conn.execute("insert into currency values (3, 'Доллар')")
# e = conn.execute("insert into price_v values (1, 'шт')")
# e = conn.execute("insert into price_v values (2, 'м2')")
# e = conn.execute("insert into product values (1, 'Люстра', 4,'l.jpg','ab0001-4', 'Завод Люстр', 2, 'Нега', '30см', 25, 1, 2, 10, 1)")
# e = conn.execute("insert into product values (2, 'Коврик в ванную', 5,'k.jpg','ac0002-5', 'Завод ковриков', 3, 'Восторг', 'Полметра', 125, 1, 2, 10, 1)")
# e = conn.execute("insert into product values (3, 'Плитка белая', 1,'p.jpg','rt0003-1','Завод плитки', 1, 'Закат', '90x60x90', 525, 2, 3, 10, 20)")
for i in range(100):
    e = conn.execute(f"insert into product values ({i}, 'Плитка белая{i}', 1,'big_default.png', 'sm_default.png', 'rt000{i}-1','Завод плитки{i%6}', 1, 'Закат{i%2}','90x60x90',525, 2, 3, 10, 20)")

