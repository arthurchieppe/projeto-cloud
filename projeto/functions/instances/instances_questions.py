name_of_instances = {
    "type": "input",
    "name": "name_of_instances",
    "message": "What is the name of the IAM user?"
}

actions_instances = {
    "type": "list",
    "name": "actions_instances",
    "message": "What action do you want to perform?",
    "choices": [
        "Create new Instances",
        "Delete Instance",

        "Exit",
    ],
}