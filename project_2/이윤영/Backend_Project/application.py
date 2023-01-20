from flask import Flask, render_template, request
import sys
application = Flask(__name__)

@application.route("/")
def hello():
  return render_template("index.html")
@application.route("/applyhouse")
def apply():
  return render_template("applyhouse.html")
@application.route("/applyphoto")
def photo_apply():
  location = request.args.get("location")
  cleaness = request.args.get("clean")
  built_in = request.args.get("built")
  print(location, cleaness,built_in)
  return render_template("applyhouse.html")
@application.route("/findhouse")
def list():
  return render_template("findhouse.html")
  if __name__ == "__main__":
    application.run(host='0.0.0.0')