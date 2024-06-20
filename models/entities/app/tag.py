from extensions.ext_database import db
from models import StringUUID


class Tag(db.Model):
    __tablename__ = 'tags'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='tag_pkey'),
        db.Index('tag_type_idx', 'type'),
        db.Index('tag_name_idx', 'name'),
    )

    TAG_TYPE_LIST = ['knowledge', 'app']

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    tenant_id = db.Column(StringUUID, nullable=True)
    type = db.Column(db.String(16), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    created_by = db.Column(StringUUID, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP(0)'))
