from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Definir as configurações do banco de dados
db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "minha_senha",
    "host": "postgres",  # Nome do serviço do banco de dados definido no docker-compose.yml
    "port": "5432"  # Porta padrão do PostgreSQL
}

# Função para obter uma tarefa pelo ID


@app.route("/tarefas/<int:id>", methods=["GET"])
def obter_tarefa(id):
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
    tarefa = cur.fetchone()
    cur.close()
    conn.close()
    if tarefa:
        return jsonify({"id": tarefa[0], "titulo": tarefa[1], "descricao": tarefa[2]})
    else:
        return jsonify({"mensagem": "Tarefa não encontrada"}), 404

# Função para listar todas as tarefas


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tarefas")
    tarefas = cur.fetchall()
    cur.close()
    conn.close()
    tarefas_json = [{"id": t[0], "titulo": t[1], "descricao": t[2]}
                    for t in tarefas]
    return jsonify(tarefas_json)

# Função para criar uma nova tarefa


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    titulo = request.json["titulo"]
    descricao = request.json["descricao"]
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s) RETURNING id", (titulo, descricao))
    id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": id, "titulo": titulo, "descricao": descricao}), 201

# Função para atualizar uma tarefa existente


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    titulo = request.json["titulo"]
    descricao = request.json["descricao"]
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("UPDATE tarefas SET titulo = %s, descricao=%s WHERE id = %s", (titulo, descricao, id))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": id, "titulo": titulo, "descricao": descricao}), 200

# Função para excluir uma tarefa existente


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir_tarefa(id):
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    cur.execute("DELETE FROM tarefas WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return "", 204


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
