from flask import Flask

#  executa de forma manual : __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello word!"

@app.route("/about")
def about ():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True) # modo de executar o servidor apenas recomedando de forma local / pro desevolvimento local
