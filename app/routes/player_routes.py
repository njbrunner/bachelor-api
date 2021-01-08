from app.models.player import Player
from http import HTTPStatus
from flask import Blueprint, request, make_response, jsonify
from app.services import player_services
import logging

PLAYER_BP = Blueprint("player_bp", __name__, url_prefix="/player")


@PLAYER_BP.route("/", methods=["GET"])
def get_players():
    try:
        players = player_services.get_all_players()
        player_dicts = list()
        for player in players:
            player_dict = player.to_mongo()
            player_dict["_id"] = str(player_dict["_id"])
            contestant_dicts = []
            for contestant in player["team"]:
                contestant_dict = contestant.to_mongo()
                contestant_dict["_id"] = str(contestant_dict["_id"])
                contestant_dicts.append(contestant_dict)
            player_dict["team"] = contestant_dicts
            player_dicts.append(player_dict)
        return make_response({"data": player_dicts}, HTTPStatus.OK)
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@PLAYER_BP.route("/<player_id>", methods=["GET"])
def get_player(player_id):
    try:
        player = player_services.get_player(player_id)
        player_dict = player.to_mongo()
        player_dict["_id"] = str(player_dict["_id"])
        contestant_dicts = []
        for contestant in player["team"]:
            contestant_dict = contestant.to_mongo()
            contestant_dict["_id"] = str(contestant_dict["_id"])
            contestant_dicts.append(contestant_dict)
        player_dict["team"] = contestant_dicts
        return player_dict
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@PLAYER_BP.route("/new", methods=["POST"])
def new_player():
    try:
        player_name = request.json.get("name", None)
        if not player_name:
            return jsonify({"msg": "Missing player name"}), HTTPStatus.BAD_REQUEST
        new_player = player_services.create_player(player_name)
        new_player_dict = new_player.to_mongo()
        new_player_dict["_id"] = str(new_player_dict["_id"])
        return new_player_dict
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@PLAYER_BP.route("/shuffle", methods=["PUT"])
def shuffle_players():
    try:
        player_services.shuffle_players()
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@PLAYER_BP.route("/draft/<player_id>", methods=["PUT"])
def draft(player_id):
    try:
        contestant_id = request.json.get("contestant_id", None)
        if not contestant_id:
            return jsonify({"message": "Missing contestant id"}), HTTPStatus.BAD_REQUEST
        player_services.draft_contestant(player_id, contestant_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@PLAYER_BP.route("/remove/<player_id>", methods=["DELETE"])
def remove_player(player_id):
    try:
        logging.warning(player_id)
        player_services.remove_player(player_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST
