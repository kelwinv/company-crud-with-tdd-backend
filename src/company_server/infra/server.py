"""server api"""

from flask import Flask

from company_server.application.controllers.company_blueprint import company_blueprint

app = Flask(__name__)

app.register_blueprint(company_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
