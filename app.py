from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)

# Modelo Tarefa
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(500), nullable=True)

# Lista de tarefas (pode ser substituída por um banco de dados)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', title='Gerenciador de Tarefas')

@app.route('/tasks', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
    return render_template('task_list.html', title='Lista de Tarefas', tasks=tasks)

@app.route('/tasks/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)
        return redirect(url_for('task_list'))
    return render_template('add_task.html', title='Adicionar Tarefa')

@app.route('/tasks/remove/<int:task_id>')
def remove_task(task_id):
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        return f'Tarefa removida: {removed_task}'
    return 'Tarefa não encontrada'

# Rota para a página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Lógica de autenticação aqui (para fins demonstrativos, vamos considerar login bem-sucedido)
        # Substitua a lógica de autenticação real aqui

        # Redirecionar para a página de adicionar tarefas após o login
        return redirect(url_for('crud_tarefas'))

    return render_template('login.html', title='Login')

# Rota para a página de adicionar tarefas
@app.route('/crud_tarefas')
def crud_tarefas():
    return render_template('crud_tarefas.html', title='Adicionar Tarefas')

if __name__ == '__main__':
    # Criação das tabelas no banco de dados
    with app.app_context():
        db.create_all()

    app.run(debug=True)
