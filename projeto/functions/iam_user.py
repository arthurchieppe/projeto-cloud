from templates import *
from PyInquirer import prompt
import os
import json

from functions.user_questions import *

def create_iam_user():
    answers = prompt(name_of_iam_user)
    with open("main.tf", "r") as f:
        tf = f.read()
    tf += iam_user.substitute(name=str(answers['name_of_iam_user']))
    with open("main.tf", "w") as f:
        f.write(tf)
    os.system('terraform init')
    os.system('terraform apply -auto-approve')

def list_iam_users():
    print("IAM users:\n")
    with open("terraform.tfstate", "r") as f:
        show = json.load(f)
    #Print pretty json
    # print(json.dumps(json.loads(show), indent=2, sort_keys=True))
    for i, resource in enumerate(show['resources']):
        if "aws_iam_user" in resource['module']:
            print(f"Module: {resource['module']}")
            print(f"Type: {resource['type']}")
            print(f"Name: {resource['name']}")
            print(f"ID: {resource['instances'][0]['attributes']['id']}")
            print(f"ARN: {resource['instances'][0]['attributes']['arn']}")

def delete_iam_users():
    print("IAM users:\n")
    list_iam_users()

def manage_iam_user():
    answers = prompt(actions_iam_user)
    if answers['actions_iam_user'] == 'Create new IAM user':
        create_iam_user()
    if answers['actions_iam_user'] == 'Delete IAM user':
        delete_iam_user()
    if answers['actions_iam_user'] == 'List IAM user':
        list_iam_users()
    if answers['actions_iam_user'] == 'Exit':
        return