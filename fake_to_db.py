from sqlalchemy import create_engine

engine = create_engine('sqlite:///app.db')
conn = engine.connect()

e = conn.execute("insert  into user values (1, 'admin', 'pbkdf2:sha256:260000$pxghoNJ8gBuLY7B3$714c91e95b5dc1c738d62ae5b9fc9e274e7f43caa3a7b2bbdad38ff684475a97')")
e = conn.execute("insert  into country values (1, 'rus')")
e = conn.execute("insert  into country values (2, 'eng')")
e = conn.execute("insert  into country values (3, 'ger')")
e = conn.execute("insert  into category values (1, 'Плитка')")
e = conn.execute("insert  into category values (2, 'Обои')")
e = conn.execute("insert  into category values (3, 'Посуда')")
e = conn.execute("insert  into category values (4, 'Свет')")
e = conn.execute("insert  into category values (5, 'Напольные покрытия')")
e = conn.execute("insert  into category values (6, 'Мебель')")
e = conn.execute("insert  into factory values (1, 'Heiniken', 'h.jpg')")
e = conn.execute("insert  into factory values (2, 'ZGBI2', 'zb.jpg')")
e = conn.execute("insert  into currency values (1, 'r')")
e = conn.execute("insert  into currency values (2, 'e')")
e = conn.execute("insert  into currency values (3, 'd')")
e = conn.execute("insert  into price_v values (1, '')")
e = conn.execute("insert  into price_v values (2, 'уп.')")
e = conn.execute("insert  into product values (1, 'Люстра', 4,'l.jpg','ab0001-4', 2,2,'Blur', 25, 1,2, 10, 1)")
e = conn.execute("insert  into product values (2, 'Коврик в ванную', 5,'k.jpg','ac0002-5', 1,3,'Elegia', 125, 1,2, 10, 1)")
e = conn.execute("insert  into product values (3, 'Плитка белая', 1,'p.jpg','rt0003-1',2,1,'Bagami', 525, 2,3, 10, 20)")
print(e)

