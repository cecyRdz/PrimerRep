from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    #return'<h1>HOLA CECY</h1>'
    return render_template('Comunes/index.html')

if __name__ == '__main__':
    app.run(debug=True)