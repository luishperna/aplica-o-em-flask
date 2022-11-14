# Importando o Flask e render_template
from flask import Flask, render_template, request, jsonify

# Iniciando o Flask
app = Flask(__name__)

# Rota homepage da aplicação
@app.route("/")
def homepage():
    return render_template('index.html')

# Rota para obter o remetente e sua mensagem, além de retornar os dados via JSON
@app.route("/mensagens", methods=['GET'])
def get_message():
    remetente = request.args.get('remetente')
    mensagem = request.args.get('mensagem')
    mensagem_completa = jsonify(Remetente=f'{remetente}', Mensagem=f'{mensagem}')
    return mensagem_completa

# Tratrando rotas não existentes 
@app.route("/<string:error>")
def error(error):
    return render_template('error.html', error=error)

# Rodando a aplicação
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)