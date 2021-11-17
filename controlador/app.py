from flask import Flask,render_template, request,flash
from flask_bootstrap import Bootstrap
from modelo.DAO import db, Productos

app = Flask(__name__, template_folder='../vista', static_folder='../static')
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://userShopitesz:Hola.123@localhost/shopitesz_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key='cl4v3'

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
    p = Productos()
    p.IDCATEGORIA=request.form['idCategoria']
    p.NOMBRE=request.form['nombre']
    p.DECRIPCION=request.form['descripcion']
    p.PRECIO=request.form['precioVenta']
    p.EXISTENCIA=request.form['existencia']
    p.COLOR=request.form['color']
    p.MARCA=request.form['marca']
    p.COSTOENVIO=request.form['costoEnvio']
    #p.ESTATUS=request.form['estatus']
    p.foto=request.files['foto'].read()
    p.insertar()
    flash('Se ha registrado un nuevo producto con éxito!!')
    return render_template('Productos/registrarProducto.html')

@app.route('/EliminarProducto')
def EliminarProducto():
    return render_template('Productos/eliminarProducto.html')

@app.route('/productos/ver/<int:id>')
def consultarProducto(id):
    p = Productos()
    return render_template('Productos/editarProducto.html', producto=p.consultaIndividual(id))

@app.route('/guardarDatosProducto',methods=['post'])
def guardarDatosProducto():
    p = Productos()
    p.IDPRODUCTO=request.form['idProducto']
    p.IDCATEGORIA=request.form['idCategoria']
    p.NOMBRE=request.form['nombre']
    p.DECRIPCION=request.form['descripcion']
    p.PRECIO=request.form['precioVenta']
    p.EXISTENCIA=request.form['existencia']
    p.COLOR=request.form['color']
    p.MARCA=request.form['marca']
    p.COSTOENVIO=request.form['costoEnvio']
    estatus=request.values.get('estatus',False)
    if estatus=="True":
        p.ESTATUS=True
    else:
        p.ESTATUS=False
    imagen=request.files['foto'].read()
    if imagen:
        p.foto=imagen
    p.actualizar()
    flash('Producto editado con éxito!!')
    return render_template('Productos/editarProducto.html',producto=p)

@app.route('/productos/imagen/<int:id>')
def consultarImagenProducto(id):
    p = Productos()
    return p.consultaIndividual(id).foto

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)