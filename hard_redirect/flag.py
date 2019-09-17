from flask import Flask, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    page = request.args.get('page')
    if(page == None):
        return "No flag :("
    return "Flag: " + page

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)
