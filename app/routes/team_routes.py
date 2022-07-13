from http import HTTPStatus
from flask import Blueprint, request, make_response, jsonify
from app.services import team_services
import logging

TEAM_BP = Blueprint("team_bp", __name__, url_prefix="/team")


@TEAM_BP.route("/", methods=["GET"])
def get_teams():
    try:
        teams = team_services.get_all_teams()
        team_dicts = [team.to_json() for team in teams]
        return make_response({"data": team_dicts}, HTTPStatus.OK)
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@TEAM_BP.route("/<team_id>", methods=["GET"])
def get_team(team_id):
    try:
        team = team_services.get_team(team_id)
        team_dict = team.to_json()
        return team_dict, HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@TEAM_BP.route("/new", methods=["POST"])
def new_team():
    try:
        team_name = request.json.get("name", None)
        owner = request.json.get("owner", None)
        if not team_name:
            return jsonify({"msg": "Missing team name"}), HTTPStatus.BAD_REQUEST
        if not owner:
            return jsonify({"msg": "Missing team owner"}), HTTPStatus.BAD_REQUEST
        new_team = team_services.create_team(team_name, owner)
        new_team_dict = new_team.to_json()
        return new_team_dict, HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@TEAM_BP.route("/shuffle", methods=["PUT"])
def shuffle_teams():
    try:
        team_services.shuffle_teams()
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@TEAM_BP.route("/draft/<team_id>", methods=["PUT"])
def draft(team_id):
    try:
        contestant_id = request.json.get("contestant_id", None)
        if not contestant_id:
            return jsonify({"message": "Missing contestant id"}), HTTPStatus.BAD_REQUEST
        team_services.draft_contestant(team_id, contestant_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@TEAM_BP.route("/remove/<team_id>", methods=["DELETE"])
def remove_team(team_id):
    try:
        team_services.remove_team(team_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST
