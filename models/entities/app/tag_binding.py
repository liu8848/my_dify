from extensions.ext_database import db
from models import StringUUID


class TagBinding(db.Model):
    __tablename__ = 'tag_bindings'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='tag_binding_pkey'),
        db.Index('tag_bind_target_id_idx', 'target_id'),
        db.Index('tag_bind_tag_id_idx', 'tag_id'),
    )

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    tenant_id = db.Column(StringUUID, nullable=True)
    tag_id = db.Column(StringUUID, nullable=True)
    target_id = db.Column(StringUUID, nullable=True)
    created_by = db.Column(StringUUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
