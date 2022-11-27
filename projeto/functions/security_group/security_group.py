from templates import *
from PyInquirer import prompt
import os
import json
from json_templates import JsonTemplates


from functions.security_group.security_group_questions import *

def create_security_group():
    answers = prompt(create_security_group_questions)
    with open("main.tf.json", "r") as f:
        tf = json.load(f)
        dict = json.loads(security_group_json.substitute(security_group_name=answers['security_group_name'], ingress_from_port=answers['ingress_from_port'], 
        ingress_to_port=answers['ingress_to_port'], vpc_id="${module.aws_vpc.vpc_id}"))
        tf['module'].append(dict)
    with open("main.tf.json", "w") as f:
        json.dump(tf, f, indent=2)
    os.system('terraform init')
    os.system('terraform apply -auto-approve')
    
def assign_security_group_to_instance():
    list_instances()
    answers = prompt(assign_security_group_to_instance_questions)
    
    with open("main.tf.json", "r") as f:
        tf = json.load(f)
    current_sg = []
    for i, resource in enumerate(tf['module']):
        if f"aws_instance_{answers['instance_name']}" in resource.keys():
            current_sg = list(resource[f"aws_instance_{answers['instance_name']}"]['vpc_security_group_ids'])
            string = "${"
            string += f"module.aws_security_group_{str(answers['security_group_id'])}.security_group_id"
            string += "}"
            current_sg.append(string)
            resource[f"aws_instance_{answers['instance_name']}"]['vpc_security_group_ids'] = current_sg
            print(tf)
            break
    with open("main.tf.json", "w") as f:
        json.dump(tf, f, indent=2)
    os.system('terraform init')
    os.system('terraform apply -auto-approve')


def list_security_groups():
    print("Security groups:\n")
    with open("terraform.tfstate", "r") as f:
        show = json.load(f)
    #Print pretty json
    # print(json.dumps(json.loads(show), indent=2, sort_keys=True))
    for i, resource in enumerate(show['resources']):
        if "aws_security_group" in resource['module']:
            print()
            print(f"Module: {resource['module']}")
            print(f"Type: {resource['type']}")
            print(f"Name: {resource['name']}")
            print(f"Security group ID: {resource['instances'][0]['attributes']['id']}")
            print(f"Security group name: {resource['instances'][0]['attributes']['name']}")
            print(f"Security group description: {resource['instances'][0]['attributes']['description']}")
            print(f"Security group ingress: {resource['instances'][0]['attributes']['ingress']}")
            print(f"Security group egress: {resource['instances'][0]['attributes']['egress']}")
            print(f"Security group vpc ID: {resource['instances'][0]['attributes']['vpc_id']}")
            print(f"Security group tags: {resource['instances'][0]['attributes']['tags']}")

def list_instances():
    print("Instances:\n")
    with open("terraform.tfstate", "r") as f:
        show = json.load(f)
    #Print pretty json
    # print(json.dumps(json.loads(show), indent=2, sort_keys=True))
    for i, resource in enumerate(show['resources']):
        if "aws_instance" in resource['module']:
            print()
            print(f"Module: {resource['module']}")
            print(f"Type: {resource['type']}")
            print(f"Name: {resource['name']}")
            print(f"Instance ID: {resource['instances'][0]['attributes']['id']}")
            print(f"Instance type: {resource['instances'][0]['attributes']['instance_type']}")
            print(f"Public IP: {resource['instances'][0]['attributes']['public_ip']}")
            print(f"Private IP: {resource['instances'][0]['attributes']['private_ip']}")
            print(f"Security groups: {resource['instances'][0]['attributes']['vpc_security_group_ids']}")
            print(f"AMI: {resource['instances'][0]['attributes']['ami']}")
            print(f"Availability zone: {resource['instances'][0]['attributes']['availability_zone']}")
            print(f"Subnet ID: {resource['instances'][0]['attributes']['subnet_id']}")

def manage_security_group():
    while True:
        answers = prompt(actions_security_group)
        if answers["actions_security_group"] == "Create new security group":
            create_security_group()
        # elif answers["actions_security_group"] == "Delete security group":
        #     delete_security_group()
        elif answers["actions_security_group"] == "List security groups":
            list_security_groups()
        elif answers["actions_security_group"] == "Assign security group to instance":
            assign_security_group_to_instance()
        elif answers["actions_security_group"] == "Previous menu":
            return