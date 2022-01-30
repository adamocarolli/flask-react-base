from flask import Flask, jsonify


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    @app.route('/api/hello')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return jsonify({
            "msg": f"Hello {app.config.get('NAME')}"
        })

    return app
