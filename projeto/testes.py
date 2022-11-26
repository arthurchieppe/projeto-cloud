
from templates import *
from PyInquirer import prompt
import os
import json
from json_templates import JsonTemplates


from functions.user_questions import *
print("Type the name of the user you want to delete (without quotes)")
answers = prompt(name_of_iam_user)
with open("main.tf.json", "r") as f:
    tf = json.load(f)
    for i, resource in enumerate(tf['module']):
        print(resource.keys())
        if f"aws_iam_user_{answers['name_of_iam_user']}" in resource.keys():
            del tf['module'][i]
            return
    print("User not found")
