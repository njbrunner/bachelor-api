from http import HTTPStatus
from flask import Blueprint, request, make_response, jsonify
from app.models.player import Player

PLAYER_BP = Blueprint('player_bp', __name__, url_prefix='/player')


@PLAYER_BP.route('/', methods=['GET'])
def get_players():
    players = Player.objects
    player_dicts = list()
    for player in players:
        player_dict = player.to_mongo()
        player_dict['_id'] = str(player_dict['_id'])
        player_dicts.append(player_dict)
    return make_response({'data': player_dicts}, HTTPStatus.OK)

@PLAYER_BP.route('/new', methods=['POST'])
def new_player():
    player_data = request.json
    new_player = Player(
        name=player_data['name'],
        team=[]
    )
    new_player.save()
    new_player_dict = new_player.to_mongo()
    new_player_dict['_id'] = str(new_player_dict['_id'])
    return new_player_dict

@PLAYER_BP('/remove/<player_id>', methods=['DELETE'])
def remove_player(player_id):
    player = Player.objects.delete(_id=player_id)
    player_dict = player.to_mongo()
    player_dict['_id'] = str(player_dict['_id'])
    return player_dict