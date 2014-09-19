import os
import json
from markdown import markdown

def load_problem_data():
    app_data = None
    with open('data.json') as f:
        app_data = json.loads(f.read())

    return app_data


def load_readme():
    readme = None
    with open('README.md') as f:
        readme = markdown(f.read(), extensions=['tables'])

    return readme


