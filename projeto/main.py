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

