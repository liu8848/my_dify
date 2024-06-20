from extensions.ext_database import db
from models import StringUUID


class Workflow(db.Model):
    __tablename__ = 'workflows'
    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='workflow_pkey'),
        db.Index('workflow_version_idx', 'tenant_id', 'app_id', 'version')
    )

    id = db.Column(StringUUID, server_default=db.text('gen_random_uuid()'))
    tenant_id = db.Column(StringUUID, nullable=False)
    app_id = db.Column(StringUUID, nullable=False)
    type = db.Column(db.String(255), nullable=False)
    version = db.Column(db.String(255), nullable=False)
    graph = db.Column(db.Text)
    feature = db.Column(db.Text)
    created_by = db.Column(StringUUID, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.text('CURRENT_TIMESTAMP(0)'), nullable=False)
    updated_by = db.Column(StringUUID, nullable=False)
    updated_at = db.Column(db.DateTime)


