import json
from markdown import markdown
from flask import Flask, render_template, jsonify, abort
app = Flask(__name__)

APP_DATA = None
ENABLED_DATA = None

with open('data.json') as f:
    APP_DATA = json.loads(f.read())

for sub_name, subject in APP_DATA.items():
    sub_en = False
    for category in subject['categories'].values():
        category['enabled'] = cat_en = any([sk['enabled'] for sk in category['skills'].values()])

        if cat_en:
            sub_en = True

    subject['enabled'] = sub_en

ENABLED_DATA = {
    sub_name: {
        'short_name': subject['short_name'],
        'categories': {
            cat_name: {
                'short_name': category['short_name'],
                'skills': {
                    sk_name: {
                        'short_name': skill['short_name'] 
                    } for sk_name, skill in category['skills'].items() if skill['enabled']
                }
            } for cat_name, category in subject['categories'].items() if category['enabled']
        }
    } for sub_name, subject in APP_DATA.items() if subject['enabled']
}

README = None
with open('README.md') as f:
    README = markdown(f.read(), extensions=['tables'])

@app.route("/")
def index():
    return render_template('index.html', readme=README)


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