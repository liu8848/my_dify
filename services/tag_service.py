from sqlalchemy import func

from extensions.ext_database import db
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
