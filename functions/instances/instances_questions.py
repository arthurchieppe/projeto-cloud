delete_instance = {
    "type": "input",
    "name": "delete_instance",
    "message": "What is the module name ending of the instance you want to delete? (Ex: micro_0, medium_1) "
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

