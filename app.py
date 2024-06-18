from flask import Flask

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


class DifyApp(Flask):
    pass


def create_app() -> Flask:
    app = DifyApp(__name__)
    app.config.from_object(Config())

    initialize_extensions(app)

    return app


def initialize_extensions(app):
    ext_database.init_app(app)  # 创建数据库连接
    ext_migrate.init(app, db)


app = create_app()

if __name__ == '__main__':
    app.run()
