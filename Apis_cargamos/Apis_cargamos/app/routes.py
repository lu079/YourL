from flask import redirect, render_template,request,flash,url_for,make_response,jsonify
from app import app,db
from app.models import ProductCategory,Product,Order,OrderProduct,UserAddress,Payment
from app.serializer import productCategory_schema,productCategorys_schema,product_schema,products_schema,order_schema,orderProduct_schema,userAddress_schema,payment_schema

from flask_cors import cross_origin

/*renombrar carpeta routes > routers*/

@cross_origin
@app.route("/listar_producto",methods=["GET"])
def listar_producto():
    #todo seleccionado todos los objetos de la clase grupos
    products=Product.query.all()
    #todo serializando y seleccionado los atributos a cast en json
    #todo dump nos permite serializar los objetos de PYTHON
    result=products_schema.dump(products)
    #todo creando el documento de salida
    data={
        'message':'Todos mis productos',
        'status':200,
        'data':result
    }
    return make_response(jsonify(data))

