from flask import Flask, Response, request, render_template, jsonify
import pymongo
import json
import covid
from utils import insert
import mongodb
from utils import list_to_string
from utils import state_list


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/admin')
def admin():
    return render_template('scrap.html')


@app.route('/table')
def dashboardTab():
    return render_template('dashboardTable.html')


@app.route('/state')
def dashboardSpec():
    return render_template('dashboardState.html')


@app.route('/api/v1/scrap', methods=['GET'])
def scrap():
    try:
        insert.insert()

        return("Inserted the value")

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")


@app.route('/api/v1/states', methods=['POST'])
def get_states():
    try:
        req = request.get_json()
        from_date = req['fromDate']
        to_date = req['toDate']

        fin_res = covid.get_state_table(from_date, to_date)

        return jsonify(fin_res)

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")


@app.route('/api/v1/states/<string:stateName>', methods=['POST'])
def get_specific_state(stateName):
    try:
        req = request.get_json()
        from_date = req['fromDate']
        to_date = req['toDate']

        final_res = covid.get_specific_state(from_date, to_date, stateName)

        str_res = list_to_string.list_to_string_func(final_res)

        return str_res

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")


@app.route('/api/v1/statelist', methods=['GET'])
def statelist():
    try:
        state_list = state_list.state_list_func()

        return jsonify(state_list)

    except Exception as ex:
        print("*******************")
        print(ex)
        print("*******************")


if __name__ == "__main__":
    app.run(debug=True)
