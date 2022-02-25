from flask import redirect, render_template,request,flash,url_for,make_response,jsonify
from app import app,db
from app.models import ProductCategory,Product,Order,OrderProduct,UserAddress,Payment
from app.serializer import productCategory_schema,productCategorys_schema,product_schema,products_schema,order_schema,orderProduct_schema,userAddress_schema,payment_schema

from flask_cors import cross_origin

@cross_origin
@app.route("/listar_productos",methods=["GET"])
def listar_productos():
    productos=Product.query.all()
    result=products_schema.dump(productos)
    data={
        'message':'Todos mis productos',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

""" 
@cross_origin
@app.route('/autenticar/<uname>/<passw>',methods=["POST"])
def autenticar(uname,passw):
    login=Usuarios.query.filter_by(user_name=uname,password=passw).first()
    result=user_schema.dump(login)
    if login is not None:
        data ={
            'message':'Bienvenido',
            'status':200,
            'data':result
        }
    else:
        data ={
            'message':'Error',
            'status':200
        }
    return make_response(jsonify(data))

@cross_origin
@app.route('/category_product/<int:categoryid>', methods=['GET'])
def category_product(categoryid):
    category_product =ProductCategory.query.get(categoryid)
    return jsonify(id=category_product.id, name=category_product.name,
                description=category_product.description,
                items=[dict(id=item.id,
        name=item.name, price=item.price,stock_code=item.stock_code) for item in
        category_product.items]) """
