main_menu = {
    "type": "list",
    "name": "main_menu",
    "message": "What action do you want to perform?",
    "choices": [
        "Create whole new infrastructure",
        "Destroy whole infrastructure",
        "List resources",
        "Manage IAM users",
        "Exit",
    ],
}

number_of_micro_instances = {
    "type": "input",
    "name": "number_of_instances",
    "message": "How many micro instances do you want to create?\n (You will be able to create medium instances later)",
}

number_of_medium_instances = {
    "type": "input",
    "name": "number_of_instances",
    "message": "How many medium instances do you want to create?",
}

