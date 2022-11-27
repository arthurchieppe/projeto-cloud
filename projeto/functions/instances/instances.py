from templates import *
from PyInquirer import prompt
import os
import json
from json_templates import JsonTemplates
from questions import *

from functions.instances.instances_questions import *
from main import list_modules



def create_instances():
    with open("main.tf.json", "r") as f:
        tf = json.load(f)
    micro_count = []
    medium_count = []
    for i, resource in enumerate(tf['module']):
        if f"aws_instance_micro_" in list(resource.keys())[0]:
            micro_count.append(int(list(resource.keys())[0][-1]))
        if f"aws_instance_medium_" in list(resource.keys())[0]:
            medium_count.append(int(list(resource.keys())[0][-1]))

    if len(micro_count) > 0:
        micro_count = max(micro_count) + 1
    else:
        micro_count = 0

    if len(medium_count) > 0:
        medium_count = max(medium_count) + 1
    else:
        medium_count = 0

    defaults ={ "subnet_id": "${module.aws_subnet.subnet_id}",
     "security_group_id" : "${module.aws_security_group_ssh.security_group_id}"
    }
    answers = prompt([number_of_micro_instances])
    # Prompt micro instances
    for i in range(int(answers['number_of_instances'])):
        tf["module"].append(json.loads(instance_json.substitute(defaults, count=micro_count+i, instance_type="t2.micro", type="micro")))
    # Prompt medium instances
    answers = prompt([number_of_medium_instances])
    for i in range(int(answers['number_of_instances'])):
        tf["module"].append(json.loads(instance_json.substitute(defaults, count=medium_count+i, instance_type="t2.medium", type="medium")))
    # print(tf)
    with open('main.tf.json', 'w') as file:
        json.dump(tf, file, indent=2)
    os.system('terraform init')
    os.system('terraform apply -auto-approve')

def delete_instances():
    list_modules()
    answers = prompt(delete_instance)
    with open("main.tf.json", "r") as f:
        tf = json.load(f)
    for i, resource in enumerate(tf['module']):
        if f"aws_instance_{answers['delete_instance']}" in list(resource.keys())[0]:
            del tf['module'][i]
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

