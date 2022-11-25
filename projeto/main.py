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

if __name__ == '__main__':
    while True:
        answers = prompt(main_menu)
        if answers['main_menu'] == 'Create new infrastructure':
            create()
        if answers['main_menu'] == 'Destroy whole infrastructure':
            destroy()
        elif answers['main_menu'] == 'Exit':
            break

