import os
import pkgutil
import importlib
import json
import problems
import types
from markdown import markdown

def load_problem_data():
    app_data = None
    with open('data.json') as f:
        app_data = json.loads(f.read())

    for sub_name, subject in app_data.items():
        sub_en = False
        for category in subject['categories'].values():
            category['enabled'] = cat_en = any([sk['enabled'] for sk in category['skills'].values()])

            if cat_en:
                sub_en = True

        subject['enabled'] = sub_en

    return app_data


def load_readme():
    readme = None
    with open('README.md') as f:
        readme = markdown(f.read(), extensions=['tables'])

    return readme


def load_problem_library():
    problem_library = {}
    root_directory = os.path.dirname(problems.__file__)

    for dirpath, dirnames, filenames in os.walk(root_directory):
        if dirpath.endswith('__pycache__'):
            continue

        filenames = [fn for fn in filenames if fn != '__init__.py']

        if not filenames:
            continue

        problem_module_name, subject_name = dirpath.replace(os.getcwd(),'')[1:].split('/')

        for fn in filenames:
            category_name = fn.split('.')[0]
            import_name = '.'.join([problem_module_name, subject_name, category_name])
            imported = importlib.import_module(import_name)

            functions = {
                attr: getattr(imported, attr, None) 
                    for attr in dir(imported) 
                        if isinstance(getattr(imported, attr, None), types.FunctionType)
            }

            if subject_name not in problem_library:
                problem_library[subject_name] = {}

            subject_dict = problem_library[subject_name]
            subject_dict[category_name] = functions

    return problem_library


def calculated_enabled_data(app_data, problem_library):
    calculated_subjects = {}
    for sub_name, subject in app_data.items():
        if sub_name not in problem_library:
            continue

        problem_categories = problem_library[sub_name]
        calculated_categories = {}
        for cat_name, category in subject['categories'].items():
            if cat_name not in problem_categories:
                continue

            problem_skills = problem_categories[cat_name]
            calculated_skills = {}
            for skill_name, skill in category['skills'].items():
                if skill_name in problem_skills:
                    calculated_skills[skill_name] = {
                        'short_name': skill['short_name'],
                        'options': {
                        }
                    }

            if calculated_skills:
                calculated_categories[cat_name] = {
                    'short_name': category['short_name'],
                    'skills': calculated_skills
                }

        if calculated_categories:
            calculated_subjects[sub_name] = {
                'short_name': subject['short_name'],
                'categories': calculated_categories
            }

    return calculated_subjects
