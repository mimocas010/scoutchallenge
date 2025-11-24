from flask import Flask, jsonify, request, abort
import os

app = Flask(__name__)

@app.route("/configuration", methods=["GET"])
def configuration():
    return jsonify({
        "activityName": "ScoutChallenge",
        "version": "1.0",
        "description": "Atividade inspirada em missões escutistas (ScoutChallenge)."
    })

@app.route("/parameters", methods=["GET"])
def parameters():
    return jsonify({
        "parameters": [
            {
                "name": "missionType",
                "type": "string",
                "label": "Tipo de missao",
                "values": ["orientacao", "ambiental", "primeiros_socorros", "sobrevivencia"],
                "default": "orientacao"
            },
            {
                "name": "numTasks",
                "type": "integer",
                "label": "Numero de tarefas",
                "min": 3,
                "max": 10,
                "default": 5
            },
            {
                "name": "teamMode",
                "type": "boolean",
                "label": "Modo patrulha (trabalho em grupo)",
                "default": True
            },
            {
                "name": "timeLimit",
                "type": "integer",
                "label": "Tempo limite (minutos)",
                "default": 30
            }
        ]
    })

@app.route("/deploy", methods=["POST"])
def deploy():
    if not request.is_json:
        abort(400, description="Expected application/json")
    payload = request.get_json()
    return jsonify({
        "status": "success",
        "message": "Deploy recebido com sucesso.",
        "received": payload
    })

@app.route("/available-analytics", methods=["GET"])
def available_analytics():
    return jsonify({
        "analytics": [
            {
                "name": "tasksCompleted",
                "type": "integer",
                "description": "Numero de tarefas concluídas pelo utilizador"
            },
            {
                "name": "correctAnswers",
                "type": "integer",
                "description": "Numero de respostas corretas nas tarefas"
            },
            {
                "name": "timeSpent",
                "type": "number",
                "unit": "seconds",
                "description": "Tempo total gasto na missão"
            },
            {
                "name": "teamParticipation",
                "type": "number",
                "unit": "percentage",
                "description": "Percentagem de participacao do grupo (caso em modo patrulha)"
            },
            {
                "name": "completionStatus",
                "type": "string",
                "values": ["not_started", "in_progress", "completed"],
                "description": "Estado da missão"
            }
        ]
    })

@app.route("/analytics", methods=["POST"])
def analytics():
    if not request.is_json:
        abort(400, description="Expected application/json")
    req = request.get_json()

    example_data = {
        "tasksCompleted": 5,
        "correctAnswers": 4,
        "timeSpent": 187,
        "teamParticipation": 78,
        "completionStatus": "completed"
    }

    return jsonify({
        "requestedAnalytics": req,
        "data": example_data
    })

@app.route("/", methods=["GET"])
def root():
    return jsonify({"status": "ok", "service": "ScoutChallenge Activity Provider"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
 # Para Render: não correr app.run()
# O Render usa o comando 'gunicorn main:app'


