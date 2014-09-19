import json
from markdown import markdown
from flask import Flask, render_template, jsonify, abort
from utils import load_problem_data, load_problem_library, calculated_enabled_data, load_readme
app = Flask(__name__)

APP_DATA = load_problem_data()
README = load_readme()
PROBLEM_LIBRARY = load_problem_library()
ENABLED_DATA = calculated_enabled_data(APP_DATA, PROBLEM_LIBRARY)

def generate_problem(subject=None, category=None, skill=None):
    pass


@app.route("/")
def index():
    return render_template('index.html', readme=README)


@app.route("/todo")
def todo():

    todo_data = []
    for sub_name, subject in APP_DATA.items():
        for cat_name, category in subject['categories'].items():
            if not all([sk['enabled'] for sk in category['skills'].values()]):
                todo_data.append({
                    'subject': sub_name, 
                    'category': cat_name, 
                    'points': len(category['skills']) * 2
                })

    return jsonify({'todo': todo_data})


@app.route("/list")
def all_list():
    return jsonify(ENABLED_DATA)


@app.route("/subject/list")
def subject_list():
    return jsonify({'subjects': [name for name in ENABLED_DATA.keys()]})


@app.route("/<subject>/new")
def subject_new(subject=None):
    if subject not in ENABLED_DATA or subject is None:
        abort(404)

    subject = ENABLED_DATA[subject]

    return jsonify({})


@app.route("/<subject>/category/list")
def subject_category_list(subject=None):
    if subject not in ENABLED_DATA or subject is None:
        abort(404)

    subject = ENABLED_DATA[subject]

    return jsonify({'categories': [name for name in subject['categories'].keys()]})


@app.route("/<subject>/<category>/new")
def subject_category_new(subject=None, category=None):
    return jsonify({})


@app.route("/<subject>/<category>/skill/list")
def subject_category_skill_list(subject=None, category=None):
    if subject not in ENABLED_DATA or subject is None or category is None:
        abort(404)

    subject = ENABLED_DATA[subject]

    if category not in subject['categories']:
        abort(404)

    category = subject['categories'][category]

    return jsonify({'skills': [name for name in category['skills'].keys()]})


@app.route("/<subject>/<category>/<skill>/new")
def subject_category_skill_new():
    if subject not in ENABLED_DATA or subject is None or category is None:
        abort(404)

    subject = ENABLED_DATA[subject]

    if category not in subject['categories']:
        abort(404)

    category = subject['categories'][category]

    return jsonify({})


if __name__ == "__main__":
    app.run(debug=True)