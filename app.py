from flask import Flask, request, render_template, redirect
import sqlite3
import datetime

app = Flask(__name__, static_folder='.', static_url_path='')

# 获取数据库连接
def get_db():
    db = sqlite3.connect('memo.db')
    db.row_factory = sqlite3.Row
    return db

# 初始化数据库
def init_db():
    with app.app_context():
        try:
            db = get_db()
            with db:
                db.execute('CREATE TABLE IF NOT EXISTS task (id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT, category_id INTEGER, custom_time TEXT)')
            #with db:
            #    db.execute('ALTER TABLE task ADD COLUMN custom_time TEXT')

        finally:
            db.close()

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        db = get_db()
        with db:
            tasks = db.execute('SELECT * FROM task').fetchall()
            categories = db.execute('SELECT * FROM category').fetchall()
            custom_time = None
        
        if request.method == 'POST':
            task = request.form['task']
            category_id = request.form['category_id']
            current_time = datetime.datetime.now()
            custom_time = request.form['custom_time']
            
            with db:
                db.execute('INSERT INTO task (task_name, category_id, custom_time) VALUES (?, ?, ?)',
                           (task, category_id, custom_time))
            return redirect('/')
        
        return render_template('index.html', tasks=tasks, categories=categories, custom_time=custom_time)
    finally:
        db.close()

@app.route('/finish', methods=['POST'])
def finish():
    try:
        db = get_db()
        task_id = float(request.form['task_id'])
        with db:
            db.execute('DELETE FROM task WHERE id = ?', (task_id,))
        return redirect('/')
    finally:
        db.close()

@app.route('/edit', methods=['POST'])
def edit():
    try:
        db = get_db()
        task_id = float(request.form['task_id'])
        task_name = request.form['task_name']
        category_id = request.form['category_id']

        with db:
            db.execute('UPDATE task SET task_name = ?, category_id = ? WHERE id = ?',
                       (task_name, category_id, task_id))
        return redirect('/')
    finally:
        db.close()
