from app import create_app
from config import DevConfig

app = create_app(DevConfig)


# @app.shell_context_processor
# def make_shell_context():
#     return {"RECIPE": Recipe}


if __name__ == "__main__":
    app.run()
