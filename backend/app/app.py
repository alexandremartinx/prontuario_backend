from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost:3306/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Atendimento(db.Model):
    __tablename__ = 'atendimento'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    queixa = db.Column(db.String(255))
    remedios = db.Column(db.String(255))
    atestado = db.Column(db.Boolean)
    data = db.Column(db.Date)

    def __init__(self, nome, queixa, remedios, atestado, data):
        self.nome = nome
        self.queixa = queixa
        self.remedios = remedios
        self.atestado = atestado
        self.data = data

# Definição do modelo Paciente
class Paciente(db.Model):
    __tablename__ = 'paciente'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    particular = db.Column(db.Boolean)
    prontuario = db.Column(db.String(255))

    def __init__(self, nome, particular, prontuario):
        self.nome = nome
        self.particular = particular
        self.prontuario = prontuario

# Definição do modelo Users
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    created_at = db.Column(db.Date)

    def __init__(self, nome, email, senha, created_at):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.created_at = created_at

# Definição do modelo Planos
class Planos(db.Model):
    __tablename__ = 'planos'
    id = db.Column(db.Integer, primary_key=True)
    particular = db.Column(db.Float)
    plano = db.Column(db.String(255))

    def __init__(self, particular, plano):
        self.particular = particular
        self.plano = plano

# Definição do modelo Prontuários
class Prontuarios(db.Model):
    __tablename__ = 'prontuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    queixa = db.Column(db.String(255))
    remedios = db.Column(db.String(255))
    ultima_data = db.Column(db.Date)

    def __init__(self, nome, queixa, remedios, ultima_data):
        self.nome = nome
        self.queixa = queixa
        self.remedios = remedios
        self.ultima_data = ultima_data

# Rota inicial da aplicação
@app.route('/')
def home():
    return "Bem-vindo à API Flask!"

class Atendimento(db.Model):
    __tablename__ = 'atendimento'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    queixa = db.Column(db.String(255))
    remedios = db.Column(db.String(255))
    atestado = db.Column(db.Boolean)
    data = db.Column(db.Date)

    def __init__(self, nome, queixa, remedios, atestado, data):
        self.nome = nome
        self.queixa = queixa
        self.remedios = remedios
        self.atestado = atestado
        self.data = data

    def __repr__(self):
        return f'<Atendimento {self.id}>'

# Definição do modelo Paciente
class Paciente(db.Model):
    __tablename__ = 'paciente'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    particular = db.Column(db.Boolean)
    prontuario = db.Column(db.String(255))

    def __init__(self, nome, particular, prontuario):
        self.nome = nome
        self.particular = particular
        self.prontuario = prontuario

# Definição do modelo Users
class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    senha = db.Column(db.String(255))
    created_at = db.Column(db.Date)

    def __init__(self, nome, email, senha, created_at):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.created_at = created_at

# Definição do modelo Planos
class Planos(db.Model):
    __tablename__ = 'planos'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    particular = db.Column(db.Float)
    plano = db.Column(db.String(255))

    def __init__(self, particular, plano):
        self.particular = particular
        self.plano = plano

# Definição do modelo Prontuários
class Prontuarios(db.Model):
    __tablename__ = 'prontuarios'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    queixa = db.Column(db.String(255))
    remedios = db.Column(db.String(255))
    ultima_data = db.Column(db.Date)

    def __init__(self, nome, queixa, remedios, ultima_data):
        self.nome = nome
        self.queixa = queixa
        self.remedios = remedios
        self.ultima_data = ultima_data

# Rotas para Atendimentos
@app.route('/atendimentos', methods=['POST'])
def criar_atendimento():
    try:
        nome = request.json['nome']
        queixa = request.json['queixa']
        remedios = request.json.get('remedios')  # Usando .get() para remedios opcional
        atestado = request.json.get('atestado')  # Usando .get() para atestado opcional
        data = datetime.strptime(request.json['data'], '%Y-%m-%d').date()

        novo_atendimento = Atendimento(nome, queixa, remedios, atestado, data)

        db.session.add(novo_atendimento)
        db.session.commit()

        return jsonify({'message': 'Atendimento criado com sucesso!', 'id': novo_atendimento.id}), 201
    except KeyError as e:
        return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
    except ValueError:
        return jsonify({"message": "Formato de data inválido. Use o formato YYYY-MM-DD."}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Erro ao inserir atendimento. Verifique os dados fornecidos."}), 400

@app.route('/atendimentos', methods=['GET'])
def obter_atendimentos():
    todos_atendimentos = Atendimento.query.all()
    return jsonify([{
        'id': atendimento.id,
        'nome': atendimento.nome,
        'queixa': atendimento.queixa,
        'remedios': atendimento.remedios,
        'atestado': atendimento.atestado,
        'data': atendimento.data.strftime('%Y-%m-%d')
    } for atendimento in todos_atendimentos])

@app.route('/atendimentos/<int:id>', methods=['GET'])
def obter_atendimento_por_id(id):
    atendimento = Atendimento.query.get(id)
    if atendimento:
        return jsonify({
            'id': atendimento.id,
            'nome': atendimento.nome,
            'queixa': atendimento.queixa,
            'remedios': atendimento.remedios,
            'atestado': atendimento.atestado,
            'data': atendimento.data.strftime('%Y-%m-%d')
        })
    else:
        return jsonify({"message": "Atendimento não encontrado"}), 404

@app.route('/atendimentos/<int:id>', methods=['PUT'])
def atualizar_atendimento(id):
    atendimento = Atendimento.query.get(id)

    if atendimento:
        try:
            atendimento.nome = request.json.get('nome', atendimento.nome)
            atendimento.queixa = request.json.get('queixa', atendimento.queixa)
            atendimento.remedios = request.json.get('remedios', atendimento.remedios)
            atendimento.atestado = request.json.get('atestado', atendimento.atestado)
            atendimento.data = datetime.strptime(request.json['data'], '%Y-%m-%d').date() if 'data' in request.json else atendimento.data

            db.session.commit()
            return jsonify({'message': 'Atendimento atualizado com sucesso!'})
        except KeyError as e:
            return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro ao atualizar atendimento. Verifique os dados fornecidos."}), 400
    else:
        return jsonify({"message": "Atendimento não encontrado"}), 404

@app.route('/atendimentos/<int:id>', methods=['DELETE'])
def excluir_atendimento(id):
    atendimento = Atendimento.query.get(id)

    if atendimento:
        db.session.delete(atendimento)
        db.session.commit()
        return jsonify({"message": "Atendimento excluído com sucesso"}), 200
    else:
        return jsonify({"message": "Atendimento não encontrado"}), 404

# Rotas para Pacientes
@app.route('/pacientes', methods=['POST'])
def criar_paciente():
    try:
        nome = request.json['nome']
        particular = request.json['particular']
        prontuario = request.json['prontuario']

        novo_paciente = Paciente(nome, particular, prontuario)

        db.session.add(novo_paciente)
        db.session.commit()

        return jsonify({'message': 'Paciente criado com sucesso!', 'id': novo_paciente.id}), 201
    except KeyError as e:
        return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Erro ao inserir paciente. Verifique os dados fornecidos."}), 400

@app.route('/pacientes', methods=['GET'])
def obter_pacientes():
    todos_pacientes = Paciente.query.all()
    return jsonify([{
        'id': paciente.id,
        'nome': paciente.nome,
        'particular': paciente.particular,
        'prontuario': paciente.prontuario
    } for paciente in todos_pacientes])

@app.route('/pacientes/<int:id>', methods=['GET'])
def obter_paciente_por_id(id):
    paciente = Paciente.query.get(id)
    if paciente:
        return jsonify({
            'id': paciente.id,
            'nome': paciente.nome,
            'particular': paciente.particular,
            'prontuario': paciente.prontuario
        })
    else:
        return jsonify({"message": "Paciente não encontrado"}), 404

@app.route('/pacientes/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    paciente = Paciente.query.get(id)

    if paciente:
        try:
            paciente.nome = request.json.get('nome', paciente.nome)
            paciente.particular = request.json.get('particular', paciente.particular)
            paciente.prontuario = request.json.get('prontuario', paciente.prontuario)

            db.session.commit()
            return jsonify({'message': 'Paciente atualizado com sucesso!'})
        except KeyError as e:
            return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro ao atualizar paciente. Verifique os dados fornecidos."}), 400
    else:
        return jsonify({"message": "Paciente não encontrado"}), 404

@app.route('/pacientes/<int:id>', methods=['DELETE'])
def excluir_paciente(id):
    paciente = Paciente.query.get(id)

    if paciente:
        db.session.delete(paciente)
        db.session.commit()
        return jsonify({"message": "Paciente excluído com sucesso"}), 200
    else:
        return jsonify({"message": "Paciente não encontrado"}), 404

# Rotas para Users
@app.route('/users', methods=['POST'])
def criar_usuario():
    try:
        nome = request.json['nome']
        email = request.json['email']
        senha = request.json['senha']
        created_at = datetime.strptime(request.json['created_at'], '%Y-%m-%d').date()

        novo_usuario = Users(nome, email, senha, created_at)

        db.session.add(novo_usuario)
        db.session.commit()

        return jsonify({'message': 'Usuário criado com sucesso!', 'id': novo_usuario.id}), 201
    except KeyError as e:
        return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Erro ao inserir usuário. Verifique os dados fornecidos."}), 400

@app.route('/users', methods=['GET'])
def obter_usuarios():
    todos_usuarios = Users.query.all()
    return jsonify([{
        'id': usuario.id,
        'nome': usuario.nome,
        'email': usuario.email,
        'senha': usuario.senha,
        'created_at': usuario.created_at.strftime('%Y-%m-%d')
    } for usuario in todos_usuarios])

@app.route('/users/<int:id>', methods=['GET'])
def obter_usuario_por_id(id):
    usuario = Users.query.get(id)
    if usuario:
        return jsonify({
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'senha': usuario.senha,
            'created_at': usuario.created_at.strftime('%Y-%m-%d')
        })
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404

@app.route('/users/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    usuario = Users.query.get(id)

    if usuario:
        try:
            usuario.nome = request.json.get('nome', usuario.nome)
            usuario.email = request.json.get('email', usuario.email)
            usuario.senha = request.json.get('senha', usuario.senha)
            usuario.created_at = datetime.strptime(request.json['created_at'], '%Y-%m-%d').date() if 'created_at' in request.json else usuario.created_at

            db.session.commit()
            return jsonify({'message': 'Usuário atualizado com sucesso!'})
        except KeyError as e:
            return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro ao atualizar usuário. Verifique os dados fornecidos."}), 400
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404

@app.route('/users/<int:id>', methods=['DELETE'])
def excluir_usuario(id):
    usuario = Users.query.get(id)

    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({"message": "Usuário excluído com sucesso"}), 200
    else:
        return jsonify({"message": "Usuário não encontrado"}), 404

# Rotas para Planos
@app.route('/planos', methods=['POST'])
def criar_plano():
    try:
        particular = request.json['particular']
        plano = request.json['plano']

        novo_plano = Planos(particular, plano)

        db.session.add(novo_plano)
        db.session.commit()

        return jsonify({'message': 'Plano criado com sucesso!', 'id': novo_plano.id}), 201
    except KeyError as e:
        return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Erro ao inserir plano. Verifique os dados fornecidos."}), 400

@app.route('/planos', methods=['GET'])
def obter_planos():
    todos_planos = Planos.query.all()
    return jsonify([{
        'id': plano.id,
        'particular': plano.particular,
        'plano': plano.plano
    } for plano in todos_planos])

@app.route('/planos/<int:id>', methods=['GET'])
def obter_plano_por_id(id):
    plano = Planos.query.get(id)
    if plano:
        return jsonify({
            'id': plano.id,
            'particular': plano.particular,
            'plano': plano.plano
        })
    else:
        return jsonify({"message": "Plano não encontrado"}), 404

@app.route('/planos/<int:id>', methods=['PUT'])
def atualizar_plano(id):
    plano = Planos.query.get(id)

    if plano:
        try:
            plano.particular = request.json.get('particular', plano.particular)
            plano.plano = request.json.get('plano', plano.plano)

            db.session.commit()
            return jsonify({'message': 'Plano atualizado com sucesso!'})
        except KeyError as e:
            return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro ao atualizar plano. Verifique os dados fornecidos."}), 400
    else:
        return jsonify({"message": "Plano não encontrado"}), 404

@app.route('/planos/<int:id>', methods=['DELETE'])
def excluir_plano(id):
    plano = Planos.query.get(id)

    if plano:
        db.session.delete(plano)
        db.session.commit()
        return jsonify({"message": "Plano excluído com sucesso"}), 200
    else:
        return jsonify({"message": "Plano não encontrado"}), 404

# Rotas para Prontuários
@app.route('/prontuarios', methods=['POST'])
def criar_prontuario():
    try:
        nome = request.json['nome']
        queixa = request.json['queixa']
        remedios = request.json['remedios']
        ultima_data = datetime.strptime(request.json['ultima_data'], '%Y-%m-%d').date()

        novo_prontuario = Prontuarios(nome, queixa, remedios, ultima_data)

        db.session.add(novo_prontuario)
        db.session.commit()

        return jsonify({'message': 'Prontuário criado com sucesso!', 'id': novo_prontuario.id}), 201
    except KeyError as e:
        return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Erro ao inserir prontuário. Verifique os dados fornecidos."}), 400

@app.route('/prontuarios', methods=['GET'])
def obter_prontuarios():
    todos_prontuarios = Prontuarios.query.all()
    return jsonify([{
        'id': prontuario.id,
        'nome': prontuario.nome,
        'queixa': prontuario.queixa,
        'remedios': prontuario.remedios,
        'ultima_data': prontuario.ultima_data.strftime('%Y-%m-%d')
    } for prontuario in todos_prontuarios])

@app.route('/prontuarios/<int:id>', methods=['GET'])
def obter_prontuario_por_id(id):
    prontuario = Prontuarios.query.get(id)
    if prontuario:
        return jsonify({
            'id': prontuario.id,
            'nome': prontuario.nome,
            'queixa': prontuario.queixa,
            'remedios': prontuario.remedios,
            'ultima_data': prontuario.ultima_data.strftime('%Y-%m-%d')
        })
    else:
        return jsonify({"message": "Prontuário não encontrado"}), 404

@app.route('/prontuarios/<int:id>', methods=['PUT'])
def atualizar_prontuario(id):
    prontuario = Prontuarios.query.get(id)

    if prontuario:
        try:
            prontuario.nome = request.json.get('nome', prontuario.nome)
            prontuario.queixa = request.json.get('queixa', prontuario.queixa)
            prontuario.remedios = request.json.get('remedios', prontuario.remedios)
            prontuario.ultima_data = datetime.strptime(request.json['ultima_data'], '%Y-%m-%d').date() if 'ultima_data' in request.json else prontuario.ultima_data

            db.session.commit()
            return jsonify({'message': 'Prontuário atualizado com sucesso!'})
        except KeyError as e:
            return jsonify({"message": f"Campo obrigatório não fornecido: {e}"}), 400
        except IntegrityError:
            db.session.rollback()
            return jsonify({"message": "Erro ao atualizar prontuário. Verifique os dados fornecidos."}), 400
    else:
        return jsonify({"message": "Prontuário não encontrado"}), 404

@app.route('/prontuarios/<int:id>', methods=['DELETE'])
def excluir_prontuario(id):
    prontuario = Prontuarios.query.get(id)

    if prontuario:
        db.session.delete(prontuario)
        db.session.commit()
        return jsonify({"message": "Prontuário excluído com sucesso"}), 200
    else:
        return jsonify({"message": "Prontuário não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
