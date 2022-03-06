import re
from config.Config import Config
from config.Database import Database
from dao.UsuarioDao import UsuarioDao
from flask import Flask, request, render_template
from model.Usuario import Usuario

app = Flask(__name__)


dao = UsuarioDao(Database(Config().config).conn)

@app.route('/usuario/novo', methods=["GET"])
def novo():
    return render_template("inserir.html")

@app.route('/usuario', methods=["POST"])
def inserir():
    usuario = usuario()
    usuario.nome = request.form.get("nome")
    usuario.email = request.form.get("email")
    usuario.senha = request.form.get("senha")

    dao.inserirUsuario()

    lista = dao.selecionarUsuario()
    return render_template(
        "listagem.html",
        lista=lista
    ) 

    

@app.route('/usuario', methods=["GET"])
def listar():
    lista = dao.selecionarUsuario()
    return render_template(
        "listagem.html",
        lista=lista
    ) 

@app.route('/usuario/<id>', methods=["GET"])
def editarPagina(id):
    usuario = dao.selecionarUsuario(id)
    return render_template("editar.html", usuario=usuario)

@app.route('/usuario/editar', methods=["POST"])
def editar():
    usuario = Usuario()
    usuario.id = request.form.get("id")
    usuario.nome = request.form.get("nome")
    usuario.email = request.form.get("email")
    usuario.senha = request.form.get("senha")
    usuario = dao.alterarUsuario1(usuario)
    
    lista = dao.selecionarUsuario()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/usuario/remover<id>', methods=["GET"])
def remover(id):
    usuario = Usuario()
    usuario = usuario
    usuario.id = id 
    dao.apagarUsuario1(usuario)
    
    lista = dao.selecionarUsuario()
    return render_template(
        "listagem.html",
        lista=lista
    )


if __name__ == '__main__':
    app.run()

#Nome: Ana Cecília Bettecher de Paula

