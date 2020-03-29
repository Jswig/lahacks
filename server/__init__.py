import os
from flask import Flask
from server.config import DevelopmentConfig, ProductionConfig

chosen_config = DevelopmentConfig if "FLASK_RUN_FROM_CLI" in os.environ and os.environ["FLASK_RUN_FROM_CLI"] else ProductionConfig

def create_app(config_class = chosen_config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from server.routes import router
    app.register_blueprint(router)

    from server.dash import time_forecast
    app = time_forecast.add_dash(app)

    return app

