from flask_sqlalchemy.pagination import Pagination

from extensions.ext_database import db
from models.entities.app.app_entity import App
from models.enums.app_mode import AppMode


class AppService:

    def get_paginate_apps(self, tenant_id: str, args: dict) -> Pagination | None:
        """
        获取应用列表分页
        :param tenant_id:
        :param args:
        :return:
        """
        filters = [
            App.tenant_id == tenant_id,
            App.is_universal == False
        ]

        if args['mode'] == 'workflow':
            filters.append(App.mode.in_([AppMode.WORKFLOW.value, AppMode.COMPLETION.value]))
        elif args['mode'] == 'chat':
            filters.append(App.mode.in_([AppMode.CHAT.value, AppMode.ADVANCED_CHAT.value]))
        elif args['mode'] == 'agent-chat':
            filters.append(App.mode == AppMode.AGENT_CHAT.value)
        elif args['mode'] == 'channel':
            filters.append(App.mode == AppMode.CHANNEL.value)

        if args.get('name'):
            name = args['name'][:30]
            filters.append(App.name.ilike(f'%{name}%'))
        if args.get('tag_ids'):
            target_ids = TagService.get_target_ids_by_tag_ids('app',
                                                              tenant_id,
                                                              args['tag_ids'])
            if target_ids:
                filters.append(App.id.in_(target_ids))
            else:
                return None

        app_models = db.paginate(
            db.select(App).where(*filters).order_by(App.created_at.desc()),
            page=args['page'],
            per_page=args['limit'],
            error_out=False
        )