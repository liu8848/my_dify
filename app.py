from flask import Flask
from flask_cors import CORS

from config import Config

from extensions import (
    ext_database,
    ext_migrate,
)
from extensions.ext_database import db

from models import (
    StringUUID,
    account,
)

from models.entities.app import (
    app_entity,
    app_model_config,
    site
)


class DifyApp(Flask):
    pass


def create_app() -> Flask:
    app = DifyApp(__name__)
    app.config.from_object(Config())

    initialize_extensions(app)
    register_blueprints(app)

    return app


def initialize_extensions(app):
    ext_database.init_app(app)  # 创建数据库连接
    ext_migrate.init(app, db)


def register_blueprints(app):
    from controllers.hello import bp

    CORS(
        bp,
        allow_headers=['Content-Type', 'Authorization', 'X-App-Code'],
        methods=['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS', 'PATCH']
    )
    app.register_blueprint(bp)


app = create_app()


@app.after_request
def after_request(response):
    """Add Version headers to the response."""
    response.set_cookie('remember_token', '', expires=0)
    response.headers.add('X-Version', app.config['CURRENT_VERSION'])
    response.headers.add('X-Env', app.config['DEPLOY_ENV'])
    return response


if __name__ == '__main__':
    app.run()
