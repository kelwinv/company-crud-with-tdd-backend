"""Main function"""
from company_server.config.env import SERVER_CONFIG
from flask_cors import CORS
from waitress import serve
from company_server.infra.server import app


CORS(app)


def start():
    """Start the application"""
    serve(app, host=SERVER_CONFIG['host'], port=SERVER_CONFIG['port'])


def start_dev():
    """Start the application with debug"""
    app.run(debug=True, port=SERVER_CONFIG['port'])


if __name__ == "__main__":
    start()
