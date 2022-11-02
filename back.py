from flask import Flask, render_template, url_for, abort, request, session, redirect

app = Flask(__name__)

@app.route("/login") # главная страница
def index():
    #print(url_for('login'))
    return  render_template('log.html') # отображение страницы из файла

@app.route("/register") # главная страница
def about():
    #print(url_for('about'))
    return render_template('reglog.html')

@app.route("/profile/<username>") # <username> - переменная с именем пользователя  path: - все, что после profile записать в username даже с символом /
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Пользователь: {username}"

@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == "POST" and request.form['username'] == "selfedu" and request.form['password']=="123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username = session['userLogged']))

    return render_template('log.html', title="Авторизация")


@app.errorhandler(404)
def pageNotFound(error):
    return "<h1>Страница не найдена</h1>"

# with app.test_request_context(): # тестовый контекст запросы (нужно закомментить run)
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username = "selfedu"))

if __name__ == "__main__":  #back.py потом на удаленке
    app.secret_key = 'super secret key'
    app.run(debug=True) # поставить False потом

