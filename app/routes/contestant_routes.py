from http import HTTPStatus
from flask import Blueprint, request, make_response, jsonify
from app.models.contestants import Contestant

CONTESTANT_BP = Blueprint('contestant_bp', __name__, url_prefix='/contestant')


@CONTESTANT_BP.route('/')
def get_contestants():
    contestants = Contestant.objects
    contestant_dicts = list()
    for contestant in contestants:
        contestant_dict = contestant.to_mongo()
        contestant_dict['_id'] = str(contestant_dict['_id'])
        contestant_dicts.append(contestant_dict)
    return make_response({'data': contestant_dicts}, HTTPStatus.OK)

@CONTESTANT_BP.route('/norose/<contestant_id>', methods=['POST'])
def no_rose(contestant_id):
    contestant = Contestant.objects.get(id=contestant_id)
    contestant['active'] = False
    contestant.save()

    return 'Success'