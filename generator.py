import os
import inspect
import importlib
import pkgutil
import types
import random
import problems


class ProblemGenerator:

    def __init__(self, app_data):
        self.app_data = app_data
        self.load_problem_library()
        self.initialize_enabled_data()


    def load_problem_library(self):
        self.problem_library = {}
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

                if subject_name not in self.problem_library:
                    self.problem_library[subject_name] = {}

                subject_dict = self.problem_library[subject_name]
                subject_dict[category_name] = functions


    def initialize_enabled_data(self):
        self.enabled_data = {}
        for sub_name, subject in self.app_data.items():
            if sub_name not in self.problem_library:
                continue

            problem_categories = self.problem_library[sub_name]
            calculated_categories = {}
            for cat_name, category in subject['categories'].items():
                if cat_name not in problem_categories:
                    continue

                problem_skills = problem_categories[cat_name]
                calculated_skills = {}
                for skill_name, skill in category['skills'].items():
                    if skill_name in problem_skills:
                        skill_function = problem_skills[skill_name]
                        sk_in = inspect.getargspec(skill_function)
                        skill_options = []

                        for idx in range(0, len(sk_in.args)):
                            if idx >= len(sk_in.defaults):
                                skill_options.append({
                                    'parameter': sk_in.args[idx],
                                })
                            else:
                                skill_options.append({
                                    'parameter': sk_in.args[idx],
                                    'default': sk_in.defaults[idx]
                                })

                        calculated_skills[skill_name] = {
                            'short_name': skill['short_name'],
                            'options': skill_options
                        }

                if calculated_skills:
                    calculated_categories[cat_name] = {
                        'short_name': category['short_name'],
                        'skills': calculated_skills
                    }

            if calculated_categories:
                self.enabled_data[sub_name] = {
                    'short_name': subject['short_name'],
                    'categories': calculated_categories
                }


    def generate_problem(subject=None, category=None, skill=None):
        if subject is None:
            subject = random.choice(self.problem_library.keys())
        elif subject not in self.problem_library:
            raise Exception("Subject is invalid.")

        subject_obj = self.problem_library[subject]

        if category is None:
            category = random.choice(subject_obj['categories'].keys())
        elif category not in subject_obj['categories']:
            raise Exception("Category is invalid.")

        category_obj = subject_obj['categories'][category]

        if skill is None:
            skill = random.choice(category_obj['skills'].keys())
        elif skill not in category_obj['skills']:
            raise Exception("Skill is invalid.")

        skill_obj = category['skills'][skill]

        problem_text, answer_text = skill()

        return {
            'subject': subject,
            'subject_description': subject_obj['short_name'],
            'category': category,
            'category_description': category_obj['short_name'],
            'skill': skill,
            'skill_description': skill_obj['short_name'],
            'problem_text': problem_text,
            'answer_text': answer_text
        }
