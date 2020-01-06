from http import HTTPStatus
from flask import Blueprint, request, make_response, jsonify
from app.models.player import Player
from app.models.contestants import Contestant

PLAYER_BP = Blueprint('player_bp', __name__, url_prefix='/player')


@PLAYER_BP.route('/', methods=['GET'])
def get_players():
    players = Player.objects
    player_dicts = list()
    for player in players:
        player_dict = player.to_mongo()
        player_dict['_id'] = str(player_dict['_id'])
        contestant_dicts = []
        for contestant in player['team']:
            contestant_dict = contestant.to_mongo()
            contestant_dict['_id'] = str(contestant_dict['_id'])
            contestant_dicts.append(contestant_dict)
        player_dict['team'] = contestant_dicts
        player_dicts.append(player_dict)
    return make_response({'data': player_dicts}, HTTPStatus.OK)

@PLAYER_BP.route('/<player_id>', methods=['GET'])
def get_player(player_id):
    player = Player.objects.get(id=player_id)
    player_dict = player.to_mongo()
    player_dict['_id'] = str(player_dict['_id'])
    contestant_dicts = []
    for contestant in player['team']:
        contestant_dict = contestant.to_mongo()
        contestant_dict['_id'] = str(contestant_dict['_id'])
        contestant_dicts.append(contestant_dict)
    player_dict['team'] = contestant_dicts
    return player_dict

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

@PLAYER_BP.route('/draft/<player_id>', methods=['POST'])
def draft(player_id):
    draft_data = request.json
    contestant = Contestant.objects.get(id=draft_data['contestant_id'])
    player = Player.objects.get(id=player_id)

    player.team.append(contestant)
    player.save()
    player_dict = player.to_mongo()
    player_dict['_id'] = str(player_dict['_id'])
    contestant_dicts = []
    for contestant in player['team']:
        contestant_dict = contestant.to_mongo()
        contestant_dict['_id'] = str(contestant_dict['_id'])
        contestant_dicts.append(contestant_dict)
    player_dict['team'] = contestant_dicts
    return player_dict

@PLAYER_BP.route('/remove/<player_id>', methods=['DELETE'])
def remove_player(player_id):
    player = Player.objects.get(id=player_id)
    player.delete()
    return 'Success'
    # player_dict = player.to_mongo()
    # player_dict['_id'] = str(player_dict['_id'])
    # return player_dict