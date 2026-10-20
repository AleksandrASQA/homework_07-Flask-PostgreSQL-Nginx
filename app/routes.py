from . import app, db
from .models import Task
from flask import render_template, request, redirect, url_for


@app.route('/')
def index():
    # Получаем все записи из БД
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('index.html', tasks=tasks)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if title:
            new_task = Task(title=title, description=description)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('create.html')