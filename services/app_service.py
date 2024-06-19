from flask_sqlalchemy.pagination import Pagination


class AppService:

    def get_paginate_apps(self, tenant_id: str, args: dict) -> Pagination | None:
        filters = [
            App.tenant_id == tenant_id,
            App.is_universal == False
        ]
