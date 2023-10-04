from flask import Flask, jsonify, request, Blueprint, abort
from entity.Pilha import Pilha
from entity.Lista import Lista

app = Flask(__name__)

# Pilha
pilha = Pilha()


@app.route('/api/pilha', methods=['GET'])
def get_pilha():
    return jsonify({'Pilha': pilha.getPilha()})


@app.route('/api/pilha', methods=['POST'])
def insert_api():
    data = request.get_json()
    numero = data.get('numero')
    pilha.insert(numero)
    return jsonify({'message': 'Número adicionado à pilha'}), 201


@app.route('/api/pilha', methods=['DELETE'])
def remove_api():
    numero = pilha.remove()

    if numero is None:
        return jsonify({'message': 'A pilha está vazia'}), 404

    return jsonify({'message': f'Número {numero} removido com sucesso'}), 200


# Lista
lista = Lista()


@app.route('/api/lista', methods=['GET'])
def get_lista():
    return jsonify({'Lista': lista.getLista()})


@app.route('/api/lista', methods=['POST'])
def insert_lista():
    data = request.get_json()
    numero = data.get('numero')
    lista.insert(numero)
    return jsonify({'message': 'Número adicionado à lista'}), 201


@app.route('/api/lista', methods=['DELETE'])
def remove_lista():
    data = request.get_json()
    numero = data.get('numero')
    lista.remove(numero)

    return jsonify({'message': f'Número {numero} removido com sucesso'}), 200


app.run(debug=True)
