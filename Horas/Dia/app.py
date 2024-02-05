from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///horas_trabalhadas.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Registro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(19), default=datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'), nullable=False)
    entrada_manha = db.Column(db.String(5), nullable=False)
    saida_almoco = db.Column(db.String(5), default='12:00', nullable=False)
    entrada_tarde = db.Column(db.String(5), default='13:00', nullable=False)
    saida_noite = db.Column(db.String(5), nullable=False)
    total_horas = db.Column(db.String(5), nullable=True)

def calcular_horas_trabalhadas(entrada_manha, saida_noite):
    formato_hora = "%H:%M"

    # Valores fixos para saída almoço e entrada tarde
    saida_almoco = "12:00"
    entrada_tarde = "13:00"

    entrada_manha = datetime.strptime(entrada_manha, formato_hora)
    saida_almoco = datetime.strptime(saida_almoco, formato_hora)
    entrada_tarde = datetime.strptime(entrada_tarde, formato_hora)
    saida_noite = datetime.strptime(saida_noite, formato_hora)

    horas_manha = (saida_almoco - entrada_manha).total_seconds() / 3600
    horas_almoco = 0
    horas_tarde = (saida_noite - entrada_tarde).total_seconds() / 3600

    total_horas_trabalhadas = horas_manha + horas_almoco + horas_tarde

    return total_horas_trabalhadas

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        entrada_manha = request.form["entrada_manha"]
        saida_noite = request.form["saida_noite"]

        try:
            horas_trabalhadas = calcular_horas_trabalhadas(entrada_manha, saida_noite)
        except Exception as e:
            # Trate o erro aqui (pode ser um print, log, etc.)
            print(f"Erro ao calcular horas trabalhadas: {e}")
            horas_trabalhadas = None

        novo_registro = Registro(entrada_manha=entrada_manha, saida_noite=saida_noite, total_horas=horas_trabalhadas)
        db.session.add(novo_registro)
        db.session.commit()

        # Defina os valores fixos antes de renderizar o template
        saida_almoco = "12:00"
        entrada_tarde = "13:00"

        return render_template("index.html", horas_trabalhadas=horas_trabalhadas,
                               saida_almoco=saida_almoco, entrada_tarde=entrada_tarde)

    return new_func()

def new_func():
    return render_template("index.html", horas_trabalhadas=None)

if __name__ == "__main__":
    app.run(debug=True)
