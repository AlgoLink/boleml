from flask import Flask
import os
from flask import Blueprint, render_template

blueprint = Blueprint("ui", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html")

app = Flask(__name__,static_url_path="")
app.register_blueprint(blueprint, url_prefix="/")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001)
