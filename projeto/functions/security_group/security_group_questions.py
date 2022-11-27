actions_security_group = {
    "type": "list",
    "name": "actions_security_group",
    "message": "What action do you want to perform?",
    "choices": [
        "Create new security group",
        "Delete security group",
        "List security groups",
        "Assign security group to instance",
        "Previous menu",
    ],
}

create_security_group_questions = [
    {
        "type": "input",
        "name": "security_group_name",
        "message": "What is the name of the security group?",
    },
    {
        "type": "input",
        "name": "ingress_from_port",
        "message": "What port do you want to open for ingress? (From port)",
    },
    {
        "type": "input",
        "name": "ingress_to_port",
        "message": "What port do you want to open for ingress? (To port)",
    }
]

assign_security_group_to_instance_questions = [
    {
        "type": "input",
        "name": "instance_name",
        "message": "What is the name of ending of the instance module? (Ex: micro_0, medium_1, etc)",
    },
    {
        "type": "input",
        "name": "security_group_id",
        "message": "What is the security group module name that you want to assign to the instance? (Ex: ssh)",
    }
]
