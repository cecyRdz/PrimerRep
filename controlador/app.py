from flask import Flask, render_template
app = Flask(__name__,template_folder='../vista')

@app.route('/')
def inicio():
    #return'<h1>HOLA CECY</h1>'
    return render_template('Comunes/index.html')

@app.route('/Categorias')
def listarCategorias():
    return render_template('categorias/ListarCategorias.html')

@app.route('/ModificarProductos')
def ModificarProductos():
    return render_template('Productos/ModificarProductos.html')

@app.route('/ListadoProductos')
def ListadoProductos():
    return render_template('Productos/ListadoProductos.html')

if __name__ == '__main__':
    app.run(debug=True)