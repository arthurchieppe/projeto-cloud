from templates import *
from PyInquirer import prompt
import os
import json
import hcl2


from questions import *
from templates import *
from functions.iam_user.iam_user import *
from functions.security_group.security_group import *
from functions.instances.instances import *


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
    with open('main.tf', 'r') as f:
        temp_dict = hcl2.load(f)
        # Json dumps to main.tf.json
        with open('main.tf.json', 'w') as file:
            json.dump(temp_dict, file, indent=2)
    os.remove("main.tf")
    os.system('terraform init')
    os.system('terraform apply -auto-approve')

def destroy():
    os.system('terraform destroy -auto-approve')

# def create_security_group():


def list_modules():
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
        if answers['main_menu'] == 'Create whole new infrastructure':
            create()
        if answers['main_menu'] == 'List resources':
            list_modules()
        if answers['main_menu'] == 'Manage security groups':
            manage_security_group()
        if answers['main_menu'] == 'Manage instances':
            manage_instances()
        if answers['main_menu'] == 'Destroy whole infrastructure':
            destroy()
        if answers['main_menu'] == 'Manage IAM users':
            manage_iam_user()
        
        elif answers['main_menu'] == 'Exit':
            break

