from app import db
""" clave foranea:
Crea la clave foranea- 
item = db.relationship('classe_de_ellos', backref='clase_nosotros', lazy='dynamic')
es la referencia de la clave foranea
referencia_de_ellos_id=db.Column(db.Integer,db.ForeignKey('clase ellos.id')) """

class product_category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    description=db.Column(db.String(250))
    # product2_id=db.Column(db.Integer,db.ForeignKey('products.id'))


class products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(500))
    presentation=db.Column(db.String)
    description=db.Column(db.String)
    posology=db.Column(db.String)
    management=db.Column(db.String)
    stock_code=db.Column(db.String(100))
    category_id=db.Column(db.Integer, db.ForeignKey('product_category.id'))
    inventory_id=db.Column(db.Integer)
    price=db.Column(db.FLoat)
    discount_id=db.Column(db.Integer)
    orders_id=db.Column(db.Integer,db.ForeignKey('orders.id'))
    # orders_id=db.Column(db.Integer,db.ForeignKey('orders.id'))
    # order_destails_id=db.Column(db.Integer,db.ForeignKey('order_destails.id'))
    # item3 = db.relationship('products', backref='product_category', lazy='dynamic')
    # item4 = db.relationship('products', backref='discount', lazy='dynamic')
    # item5 = db.relationship('products', backref='inventoryt', lazy='dynamic')



""" 
class users(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(25))
    password=db.Column(db.String(25))
    first_name=db.Column(db.String(25))
    last_name=db.Column(db.String(25))
    phone_number=db.Column(db.String(20))
    email=db.Column(db.String(50))
    user_address_id=db.Column(db.Integer,db.ForeignKey('user_address.id'))
    user_payment_id=db.Column(db.Integer,db.ForeignKey('user_payment.id'))

class discount(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    discount=db.Column(db.Float)
    discount_f_id=db.Column(db.Integer,db.ForeignKey('products.id'))

class inventory(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    quantity=db.Column(db.Integer)

class order_destails(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_id=db.Column(db.Integer)
    quantity=db.Column(db.Integer)
    item6= db.relationship('products', backref='order_destails', lazy='dynamic')

class user_address(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer)
    adres_line1=db.Column(db.String(200))
    adres_line2=db.Column(db.String(100))
    zipcode=db.Column(db.String(1))
    country=db.Column(db.String)
    phone=db.Column(db.Integer)
        # modificar en la base de datos
    email=db.Column(db.String)
    adres_id=db.Column(db.Integer,db.ForeignKey('orders.id'))
    item7 = db.relationship('users', backref='user_address', lazy='dynamic')

class orders(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    product_id=db.Column(db.Integer)
    adres_id=db.Column(db.Integer)
    user_phone_number=db.Column(db.String(20))
    delivery_date=db.Column(db.String)
    items = db.relationship('user_address', backref='orders', lazy='dynamic')
    item2 = db.relationship('products', backref='orders', lazy='dynamic')

class user_payment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer)
    payment_type=db.Column(db.String(200))
    provider=db.Column(db.String(200))
    account_no=db.Column(db.String(200))
    payment_date=db.Column(db.String)
    payment_detail=db.Column(db.String(500))
    item8 = db.relationship('users', backref='user_payment', lazy='dynamic')
 """



