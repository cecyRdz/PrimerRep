from flask import Flask,render_template, request
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Productos

app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userShopitesz:Hola.123@localhost/shopitesz_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

@app.route('/')
def inicio():
    return render_template('comunes/Index.html')

@app.route('/consultarProductos')
def consultarProductos():
    p = Productos()
    productos = p.consultaGeneral()
    return render_template('Productos/consultarProductos.html', productos=productos)

@app.route('/registrarProducto')
def registrarProducto():
    return render_template('Productos/registrarProducto.html')

@app.route('/registrarNuevoProducto',methods=['post'])
def registrarNuevoProducto():
    nombre = request.form['nombre']
    return 'Se ha registrado el producto: '+nombre

@app.route('/ModificarProducto')
def ModificarProducto():
    return render_template('Productos/editarProducto.html')

@app.route('/recopilarDatosEditados',methods=['post'])
def recopilarDatosEditados():
    nombre = request.form['nombre']
    return 'Se guardaron los cambios del producto: '+nombre

@app.route('/EliminarProducto')
def EliminarProducto():
    return render_template('Productos//eliminarProducto.html')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)