import os
import json
from flask import Blueprint, request
from app.models.contestants import Contestant

HELLO_BP = Blueprint('hello_bp', __name__, url_prefix='/')


@HELLO_BP.route('/')
def hello():
    return 'Hello World!'


@HELLO_BP.route('/populate_db')
def populate_db():
    print(os.getcwd())
    with open('data.json') as json_file:
        data = json.load(json_file)

        for contestant in data:
            new_contestant = Contestant(
                name=contestant['name'],
                age=contestant['age'],
                occupation=contestant['occupation'],
                location=contestant['location'],
                detail=contestant['detail'],
                facts=contestant['facts'],
                image=contestant['image'],
                active=True
            )
            new_contestant.save()
        
    return 'Success'