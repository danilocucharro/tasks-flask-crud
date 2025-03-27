from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "About Page"

@app.route("/orders")
def orders():
    return "Orders page"

if __name__ == "__main__": #o app so vai ser executado com os logs do debug quando ele for iniciado manualmente (fora do ambiente de prod)
    app.run(debug=True)