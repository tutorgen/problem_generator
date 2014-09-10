import json
from flask import Flask, render_template, jsonify
app = Flask(__name__)

app_data = None
with open('data.json') as f:
    json.loads(f.read())

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/subject/list")
def subject_list():
    return jsonify({})

@app.route("/<subject>/new")
def subject_new():
    return jsonify({})

@app.route("/<subject>/category/list")
def subject_category_list():
    return jsonify({})

@app.route("/<subject>/<category>/new")
def subject_category_new():
    return jsonify({})

@app.route("/<subject>/<category>/skill/list")
def subject_category_skill_list():
    return jsonify({})

@app.route("/<subject>/<category>/<skill>/new")
def subject_category_skill_new():
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)