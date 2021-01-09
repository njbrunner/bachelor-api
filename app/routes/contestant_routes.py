import logging
from http import HTTPStatus
from flask import Blueprint, make_response
from flask_jwt_extended import jwt_required
from app.services import contestant_services, player_services

CONTESTANT_BP = Blueprint("contestant_bp", __name__, url_prefix="/contestant")


@CONTESTANT_BP.route("/")
def get_contestants():
    try:
        contestants = contestant_services.get_all_contestants()
        contestant_dicts = [contestant.to_json() for contestant in contestants]
        return make_response({"data": contestant_dicts}, HTTPStatus.OK)
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@CONTESTANT_BP.route("/norose/<contestant_id>", methods=["PUT"])
@jwt_required
def no_rose(contestant_id):
    try:
        contestant_services.deactivate_contestant(contestant_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@CONTESTANT_BP.route("/rose/add/<contestant_id>", methods=["PUT"])
@jwt_required
def add_rose(contestant_id):
    try:
        contestant_services.add_rose(contestant_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@CONTESTANT_BP.route("/rose/add/all", methods=["PUT"])
@jwt_required
def add_rose_all():
    try:
        contestant_services.add_rose_to_all_active()
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@CONTESTANT_BP.route("/rose/subtract/<contestant_id>", methods=["PUT"])
@jwt_required
def subtract_rose(contestant_id):
    try:
        contestant_services.subtract_rose(contestant_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@CONTESTANT_BP.route("/draft/reset/<contestant_id>", methods=["PUT"])
@jwt_required
def reset_draft_status(contestant_id):
    try:
        contestant_services.reset_draft_status(contestant_id)
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST


@CONTESTANT_BP.route("/draft/reset/all", methods=["PUT"])
@jwt_required
def reset_draft_all():
    try:
        contestant_services.reset_all_draft_statuses()
        player_services.remove_all_drafted_contestants()
        return "Success", HTTPStatus.OK
    except Exception as exception:
        logging.error(str(exception))
        return str(exception), HTTPStatus.BAD_REQUEST
