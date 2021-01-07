from flask import Blueprint

HELLO_BP = Blueprint("hello_bp", __name__, url_prefix="/")


@HELLO_BP.route("/")
def hello():
    return "Hello World!"
