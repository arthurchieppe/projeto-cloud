from templates import *
from PyInquirer import prompt
import os
import json
from json_templates import JsonTemplates
from questions import *

from functions.instances.instances_questions import *



def create_instances():
    with open("main.tf.json", "r") as f:
        tf = json.load(f)
    micro_count = 0
    medium_count = 0
    for i, resource in enumerate(tf['module']):
        if f"aws_instance_micro_" in list(resource.keys())[0]:
            micro_count += 1
        if f"aws_instance_medium_" in list(resource.keys())[0]:
            medium_count += 1
    answers = prompt([number_of_micro_instances])
    # Prompt micro instances
    for i in range(int(answers['number_of_instances'])):
        tf["module"].append(json.loads(instance.substitute(count=micro_count, instance_type="t2.micro", type="micro")))
    # Prompt medium instances
    answers = prompt([number_of_medium_instances])
    for i in range(int(answers['number_of_instances'])):
        tf["module"].append(json.loads(instance.substitute(count=medium_count, instance_type="t2.medium", type="medium")))
    
    with open('main.tf.json', 'w') as file:
        json.dump(tf, file, indent=2)
    os.system('terraform init')
    os.system('terraform apply -auto-approve')

def manage_instances():
    answers = prompt(actions_instances)
    if answers['actions_instances'] == 'Create new Instances':
        create_instances()
    if answers['actions_instances'] == 'Delete Instance':
        delete_instances()
    if answers['actions_instances'] == 'Exit':
        return

