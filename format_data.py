import json
from data import PROBLEM_SUBJECTS

from slugify import Slugify

slug = Slugify(to_lower=True)
slug.separator = '_'

problems = {
   k : {
        'short_name': v['short_name'],
        'categories': {
            slug(kc): {
                'short_name': kc,
                'skills': {
                    slug(skill): { 
                        'short_name': skill, 
                    } for skill in vc 
                }
            } for kc, vc in v['categories'].items()
        }
    } for k, v in PROBLEM_SUBJECTS.items()
}

with open('data.json', 'w') as f:
    f.write(json.dumps(problems, indent=4))