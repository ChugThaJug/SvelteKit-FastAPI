from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Create an initial empty to-do list
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    new_task = request.form.get('task')
    if new_task:
        tasks.append(new_task)
    return redirect(url_for('index'))

@app.route('/remove_task/<int:index>')
def remove_task(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
