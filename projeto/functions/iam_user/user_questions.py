name_of_iam_user = {
    "type": "input",
    "name": "name_of_iam_user",
    "message": "What is the name of the IAM user?"
}

actions_iam_user = {
    "type": "list",
    "name": "actions_iam_user",
    "message": "What action do you want to perform?",
    "choices": [
        "Create new IAM user",
        "Delete IAM user",
        "List IAM user",
        "Exit",
    ],
}