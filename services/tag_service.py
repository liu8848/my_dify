import uuid

from sqlalchemy import func
from werkzeug.exceptions import NotFound

from extensions.ext_database import db
from models.entities.app.app_entity import App
from models.entities.app.tag import Tag
from models.entities.app.tag_binding import TagBinding


class TagService:
    @staticmethod
    def get_tags(tag_type: str, current_tenant_id: str, keyword: str = None) -> list:
        query = db.session.query(
            Tag.id, Tag.type, Tag.name, func.count(TagBinding.id).label('binding_count')
        ).outerjoin(
            TagBinding, Tag.id == TagBinding.tag_id
        ).filter(
            Tag.type == tag_type,
            Tag.tenant_id == current_tenant_id
        )

        if keyword:
            query = query.filter(db.and_(Tag.name.like(f'%{keyword}%')))
        query = query.group_by(
            Tag.id
        )
        result = query.order_by(Tag.created_at.desc()).all()
        return result

    @staticmethod
    def get_target_ids_by_tag_ids(tag_type: str, current_tenant_id: str, tag_ids: list) -> list:
        tags = db.session.query(Tag).filter(
            Tag.id.in_(tag_ids),
            Tag.tenant_id == current_tenant_id,
            Tag.type == tag_type
        ).all()
        if not tags:
            return []
        tag_ids = [tag.id for tag in tags]
        tag_bindings = db.session.query(
            TagBinding.target_id
        ).filter(
            TagBinding.tag_id.in_(tag_ids),
            TagBinding.tenant_id == current_tenant_id
        ).all()
        if not tag_bindings:
            return []
        results = [tag_binding.target_id for tag_binding in tag_bindings]
        return results

    @staticmethod
    def get_tags_by_target_ids(tag_type: str, current_tenant_id: str, target_id: str) -> list:
        tags = db.session.query(Tag).join(
            TagBinding,
            Tag.id == TagBinding.tag_id
        ).filter(
            TagBinding.target_id == target_id,
            TagBinding.tenant_id == current_tenant_id,
            Tag.tenant_id == current_tenant_id,
            Tag.type == tag_type
        ).all()

        return tags if tags else []

    @staticmethod
    def save_tags(args: dict) -> Tag:
        tag = Tag(
            id=str(uuid.uuid4()),
            name=args['name'],
            type=args['type'],
            created_at='admin',
            tenant_id='admin'
        )
        db.session.add(tag)
        db.session.commit()
        return tag

    @staticmethod
    def update_tags(args: dict, tag_id: str) -> Tag:
        tag = db.session.query(Tag).filter(Tag.id == tag_id).first().first()
        if not tag:
            raise NotFound('Tag not found')
        tag.name = args['name']
        db.session.commit()
        return tag

    @staticmethod
    def get_tag_binding_count(tag_id: str) -> int:
        count = db.session.query(TagBinding).filter(TagBinding.tag_id == tag_id).count()
        return count

    @staticmethod
    def delete_tag(tag_id: str):
        tag = db.session.query(Tag).filter(Tag.id == tag_id).first()
        if not tag:
            raise NotFound('Tag not found')
        db.session.delete(tag)
        # 同时删除标签绑定信息
        tag_bindings = db.session.query(TagBinding).filter(TagBinding.tag_id == tag_id).all()
        if tag_bindings:
            for tag_binding in tag_bindings:
                db.session.delete(tag_binding)
        db.session.commit()

    @staticmethod
    def save_tag_binding(args):
        # 检查target是否存在
        TagService.check_target_exists(args['type'], args['tenant_id'])
        # 保存标签绑定
        for tag_id in args['tag_ids']:
            tag_binding = db.session.query(TagBinding).filter(
                TagBinding.tag_id == tag_id,
                TagBinding.tenant_id == args['tenant_id']
            ).first()
            if tag_binding:
                continue
            new_tag_binding = TagBinding(
                tag_id=tag_id,
                target_id=args['target_id'],
                tenant_id='admin',
                created_at='admin'
            )
            db.session.add(new_tag_binding)
        db.session.commit()

    @staticmethod
    def delete_tag_binding(args):
        # 检查目标是否存在
        TagService.check_target_exists(args['type'], args['tenant_id'])
        # 删除标签关联
        tag_binding = db.session.query(TagBinding).filter(
            TagBinding.target_id == args['target_id'],
            TagBinding.tag_id == args['tag_id']
        ).first()
        if tag_binding:
            db.session.delete(tag_binding)
            db.session.commit()

    @staticmethod
    def check_target_exists(type: str, target_id: str):
        if type == 'knowledge':
            pass
        elif type == 'app':
            app = db.session.query(App).filter(
                App.tenant_id == target_id,
                App.id == target_id
            ).first()
            if not app:
                raise NotFound('App not found')
        else:
            raise NotFound("Invalid binding type")
