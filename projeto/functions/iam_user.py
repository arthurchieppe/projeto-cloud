from templates import *
from PyInquirer import prompt
import os
import json
from json_templates import JsonTemplates


from functions.user_questions import *

def create_iam_user():
    answers = prompt(name_of_iam_user)
    if answers["name_of_iam_user"] == "":
        print("You must provide a name for the IAM user")
        return
    user_json = json.loads(iam_user.substitute(username=answers["name_of_iam_user"]))
    # Check if new_dict is list
    with open("main.tf.json", "r") as f:
        tf = json.load(f)
    tf["module"].append(user_json)
    print(tf)
    with open("main.tf.json", "w") as f:
        json.dump(tf, f, indent=2)
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
    # print("IAM users:\n")
    # list_iam_users()
    # print("Type the name of the user you want to delete")
    # answers = prompt(name_of_iam_user)
    # with open("main.tf", "r") as f:
    pass

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

