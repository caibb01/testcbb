from flask import Flask, request, make_response
from myweb.tools.db_base_operation import *

app = Flask(__name__)


@app.route("/execute/case", methods=["POST"])
def execute_case():
    # server_id = request.json.get("server_id")
    # listv = request.json.get("listv")
    # db_info = {"host": "10.10.4.53", "port": 3306, "user": "test", "password": "test1234", "db": "qfsoft_db_atmp"}
    #
    #
    # response = make_response(tc_id[0])
    # return response
    pass


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=False)
