from templates import *
from PyInquirer import prompt
import os
import json

from questions import *
from templates import *

def create():
    tf = terraform_config
    tf += aws_provider
    tf += vpc_subnet.substitute()
    tf += security_group_only_ssh.substitute()
    answers = prompt([number_of_micro_instances])
    # Prompt micro instances
    for i in range(int(answers['number_of_instances'])):
        tf += instance.substitute(count=i, instance_type="t2.micro", type="micro")
    # Prompt medium instances
    answers = prompt([number_of_medium_instances])
    for i in range(int(answers['number_of_instances'])):
        tf += instance.substitute(count=i, instance_type="t2.medium", type="medium")

    with open('main.tf', 'w') as f:
        f.write(tf)
        
    os.system('terraform init')
    os.system('terraform plan')
    os.system('terraform apply -auto-approve')

def destroy():
    os.system('terraform destroy -auto-approve')

# def create_security_group():


def list():
    print("Resources allocated:\n")
    with open("terraform.tfstate", "r") as f:
        show = json.load(f)
    #Print pretty json
    # print(json.dumps(json.loads(show), indent=2, sort_keys=True))
    for i, resource in enumerate(show['resources']):
        print()
        print("Module %s" % i)
        print(f"Module: {resource['module']}")
        if "aws_instance" in resource['module']:
            print(f"Type: {resource['type']}")
            print(f"Name: {resource['name']}")
            print(f"Region: {resource['instances'][0]['attributes']['availability_zone']}")
            print(f"Security Group: {resource['instances'][0]['attributes']['vpc_security_group_ids']}")
            print(f"ID: {resource['instances'][0]['attributes']['id']}")

        if "aws_security_group" in resource['module']:
            print(f"Type: {resource['type']}")
            print(f"Id: {resource['instances'][0]['attributes']['id']}")
            print(f"Egress rules: {resource['instances'][0]['attributes']['egress']}")
            print(f"Ingress rules: {resource['instances'][0]['attributes']['ingress']}")


            





if __name__ == '__main__':
    while True:
        answers = prompt(main_menu)
        if answers['main_menu'] == 'Create new infrastructure':
            create()
        if answers['main_menu'] == 'List resources':
            list()
        if answers['main_menu'] == 'Destroy whole infrastructure':
            destroy()
        elif answers['main_menu'] == 'Exit':
            break

