from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta

app = Flask(__name__, static_url_path='/static')

lista_usuarios = ['saul1','saul2','saul3','saul4']

app.config['SECRET_KEY'] = '7e7fca40778a914195d999409f9b6f14'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    form_criarconta = FormCriarConta()
    return render_template('signup.html', form_criarconta = form_criarconta)

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios = lista_usuarios)

if __name__ == '__main__':
    app.run(debug=True)