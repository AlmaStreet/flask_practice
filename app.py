from flask import Flask, Response, request, url_for
import logging
import os

def create_app():
    app = Flask(__name__)

    # Set the log level (e.g., INFO, DEBUG, etc.)
    app.logger.setLevel(logging.INFO)

    # Configure a file handler
    log_file = os.path.join(app.root_path, "app.log")  # Path to the log file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)  # Set the log level for the file handler
    # Configure a log message format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    # Add the file handler to the app's logger
    app.logger.addHandler(file_handler)

    @app.get("/")
    def hello_world():
        return hello_world_get()

    @app.get("/get")
    def hello_world_get():
        print("hello world GET")
        app.logger.debug("A value for DEBUG")
        app.logger.info("A value for INFO")

        return "<p>Hello, World!</p>"

    @app.get("/<name>")
    def hello(name):
        return f"Hello, {name}!"

    @app.post("/post")
    def hello_world_post():
        data = request
        print(f"data: {data}")
        print(f"name: {__name__}")
        print("hello world POST")
        return Response()

    with app.test_request_context():
        hello_world = url_for("hello_world")
        hello = url_for("hello", name="jason")

        print(hello_world)
        print(hello)

    return app


if __name__ == "__main__":
    app = create_app()
