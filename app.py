from flask import Flask, jsonify, render_template, request, send_from_directory

from utils import count_down, new_year, bangkok_zone

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", year=new_year)


@app.route("/time")
def lapse():
    tz = request.args.get("tz")
    if tz is None:
        return jsonify(count_down(bangkok_zone))
    else:
        return jsonify(count_down(tz))

@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static\\images\\favicon.ico")

if __name__ == "__main__":
    app.run(port=80,debug=True)
