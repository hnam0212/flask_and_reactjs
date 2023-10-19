from config import DevConfig
from flask import Flask
from flask_restx import Api

app = Flask(__name__)
app.config.from_object(DevConfig)
api = Api(app, doc="/docs")


@app.route("/hello")
def get():
    return {"message": "hello"}


if __name__ == "__main__":
    app.run()
    # run_simple("localhost", 5000, app)
