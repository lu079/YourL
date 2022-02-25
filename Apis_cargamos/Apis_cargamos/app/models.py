from app import db

class ProductCategory(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    description=db.Column(db.String(250))

class Product(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(500))
    presentation=db.Column(db.String)
    description=db.Column(db.String)
    posology=db.Column(db.String)
    management=db.Column(db.String)
    stock_code=db.Column(db.String(100))
    category_id=db.Column(db.Integer, db.ForeignKey('ProductCategory.id'))
    category =db.Relationship('ProductCategory', backref='category_products')
    price=db.Column(db.FLoat)
    discount_price=db.Column(db.FLoat)

class Order(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    user =db.Relationship('Users', backref='users_orders')
    order_num = db.Column(db.String(50), unique=True)
    delivery_date = db.Column(db.Date)

    def __repr__(self):
        return self.order_num

class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
    order =db.Relationship('Orders', backref='order_order_products')
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
    product = db.Relationship('Products', backref='product_order_products')
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.order.user.username} - {self.product.name}'

class UserAddress(db.Model):
    id = db.Column(db.integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    user =db.Relationship('Users', backref='user_user_addresses')
    address1 = db.Column(db.String(150))
    address2 = db.Column(db.String(150))
    zipcode = db.Column(db.Integer)
    country = db.Column(db.String(50))
    city = db.Column(db.String(50))
    phone = db.Column(db.Integer)

    def __repr__(self):
        return self.user.username

class Payment(db.Model):
    id = db.Column(db.integer, primary_key= True)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.id'))
    order =db.Relationship('Orders', backref='order_payments')
    paymant_date = db.Column(db.Date)
    payment_type = db.Column(db.String(20))

    def __repr__(self):
        return self.order.order_id



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



