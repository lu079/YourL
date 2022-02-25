from app import app

from app.models import ProductCategory,Product,Order,OrderProduct,UserAddress,Payment
from flask_marshmallow import Marshmallow

ma=Marshmallow(app)

class ProductCategorySerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=ProductCategory
        fields=('id','name','description')
productCategory_schema=ProductCategorySerializer()
productCategorys_schema=ProductCategorySerializer(many=True)

class ProductSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Product
        fields=('id','name','presentation','description','posology','management','stock_code','category_id','category','price','discount_price')
product_schema=ProductSerializer()
products_schema=ProductSerializer(many=True)

class OrderSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Order
        fields=('id','user_id','user','order_num','delivery_date')
order_schema=OrderSerializer()

class OrderProductSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=OrderProduct
        fields=('id','order_id','order','product_id','product','quantity')
orderProduct_schema=OrderSerializer()

class UserAddressSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=UserAddress
        fields=('id','user_id','user','address1','address2','zipcode','country','city','phone')
userAddress_schema=OrderSerializer()

class PaymentSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model=Payment
        fields=('id','order_id','order','paymant_date','payment_type')
payment_schema=OrderSerializer()



