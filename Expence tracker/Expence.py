from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#it is an example of expence
expenses = [
    [1, 100, 'Food', 'Lunch at restaurant', '2025-02-19'],
    [2, 50, 'Transport', 'Taxi fare', '2025-02-18']
]

@app.route('/')
def index():
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        new_id = len(expenses) + 1
        expenses.append([new_id, amount, category, description, date])
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    expense = next((e for e in expenses if e[0] == id), None)
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        date = request.form['date']
        expense[1] = amount
        expense[2] = category
        expense[3] = description
        expense[4] = date
        return redirect(url_for('index'))
    return render_template('edit.html', expense=expense)

@app.route('/delete/<int:id>')
def delete(id):
    global expenses
    expenses = [e for e in expenses if e[0] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
